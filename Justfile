set shell := ["bash", "-eu", "-o", "pipefail", "-c"]

# Download through a safe .part file and validate size against our manifest.
download-patch fetchpkg manifest output url:
    python3 scripts/download_patch.py \
      "{{ fetchpkg }}" \
      "{{ manifest }}" \
      "{{ output }}" \
      "{{ url }}"

# Fingerprint a retail patch and verify every Sony-manifest piece in one read.
# Example:
# just verify-patch "/run/media/fcz/PS5_DUMPS/Acervo/patches/Astro Bot - PPSA21564" astro-bot-01.019.000
verify-patch patch_dir stem:
    python3 scripts/verify_patch.py \
      "{{ patch_dir }}/{{ stem }}.json" \
      "{{ patch_dir }}/{{ stem }}.pkg" \
      "{{ patch_dir }}/{{ stem }}.pieces.sha256.tsv" \
      "{{ patch_dir }}/{{ stem }}.verification.json"

# Verify the retained checksum of a small Sony manifest without reading the PKG.
check-patch-manifest patch_dir stem:
    cd "{{ patch_dir }}" && sha256sum -c "{{ stem }}.manifest.sha256"

# Show the files currently retained for one patch set.
list-patch patch_dir:
    find "{{ patch_dir }}" -maxdepth 1 -type f -printf '%f\t%s bytes\n' | LC_ALL=C sort
