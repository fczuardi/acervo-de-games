set shell := ["bash", "-eu", "-o", "pipefail", "-c"]

# Query the small, public Prospero Patches version list. This does not fetch a
# Sony manifest or PKG. Pass an output path to retain the response as JSON.
inspect-prospero title_id output="":
    if [[ -n "{{ output }}" ]]; then \
      python3 scripts/inspect_prospero.py "{{ title_id }}" --output "{{ output }}"; \
    else \
      python3 scripts/inspect_prospero.py "{{ title_id }}"; \
    fi

# Fetch and validate only the small Sony manifest before deciding to download.
inspect-patch url manifest:
    python3 scripts/inspect_patch.py \
      "{{ url }}" \
      "{{ manifest }}"

# Download through a safe .part file and validate size against our manifest.
download-patch fetchpkg manifest output url:
    python3 scripts/download_patch.py \
      "{{ fetchpkg }}" \
      "{{ manifest }}" \
      "{{ output }}" \
      "{{ url }}"

# Resume split Sony manifests safely. Complete leading pieces are verified;
# only a trailing fragment that cannot match a manifest piece is discarded.
download-patch-resumable manifest output:
    python3 scripts/download_patch_resumable.py \
      "{{ manifest }}" \
      "{{ output }}" \
      --discard-incomplete-tail

# Named entry point for PS4 manifests (SHA-1 pieces, SHA-256 final record).
download-patch-ps4 manifest output:
    python3 scripts/download_patch_resumable.py \
      "{{ manifest }}" \
      "{{ output }}" \
      --discard-incomplete-tail

# Create matching SHA-256 and apparent-size manifests outside an extracted dump.
dump-manifests game_dir output_dir stem *flags:
    python3 scripts/create_dump_manifests.py \
      "{{ game_dir }}" \
      "{{ output_dir }}" \
      "{{ stem }}" \
      {{ flags }}

# Create or validate the retained checksum for a Sony manifest.
ensure-patch-manifest patch_dir stem:
    python3 scripts/ensure_manifest_checksum.py "{{ patch_dir }}" "{{ stem }}"

# Complete a patch record: validate the manifest, fingerprint the retail PKG,
# verify every Sony-manifest piece in one read, and finalize all sidecars.
# Example:
# just verify-patch "/run/media/fcz/PS5_DUMPS/Acervo/patches/Astro Bot - PPSA21564" astro-bot-01.019.000
verify-patch patch_dir stem:
    python3 scripts/ensure_manifest_checksum.py "{{ patch_dir }}" "{{ stem }}"
    python3 scripts/verify_patch.py \
      "{{ patch_dir }}/{{ stem }}.json" \
      "{{ patch_dir }}/{{ stem }}.pkg" \
      "{{ patch_dir }}/{{ stem }}.pieces.sha256.tsv" \
      "{{ patch_dir }}/{{ stem }}.verification.json"
    python3 scripts/finalize_patch.py "{{ patch_dir }}" "{{ stem }}"

# Migrate a former monolithic record and rebuild the aggregate manifest.
migrate-patch-record legacy_record:
    python3 scripts/migrate_patch_record.py "{{ legacy_record }}" --remove-legacy
    stem="$(basename "{{ legacy_record }}" .preservation.json)"; \
      python3 scripts/finalize_patch.py "$(dirname "{{ legacy_record }}")" "$stem"

# Verify the retained checksum of a small Sony manifest without reading the PKG.
check-patch-manifest patch_dir stem:
    cd "{{ patch_dir }}" && sha256sum -c "{{ stem }}.manifest.sha256"

# Show the files currently retained for one patch set.
list-patch patch_dir:
    find "{{ patch_dir }}" -maxdepth 1 -type f -printf '%f\t%s bytes\n' | LC_ALL=C sort
