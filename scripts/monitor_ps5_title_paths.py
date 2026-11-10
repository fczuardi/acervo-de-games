#!/usr/bin/env python3
"""Log FTP path-existence transitions without reading file contents."""

import argparse
import datetime
import ftplib
import os
import time


def stamp() -> str:
    return datetime.datetime.now().astimezone().isoformat(timespec="milliseconds")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("host")
    parser.add_argument("title_id")
    parser.add_argument("output")
    parser.add_argument("--port", type=int, default=2121)
    parser.add_argument("--user", default="chiral")
    parser.add_argument("--duration", type=int, default=1200)
    parser.add_argument("--interval", type=float, default=0.5)
    args = parser.parse_args()
    password = os.environ["ACERVO_PS5_FTP_PASSWORD"]
    paths = [
        f"/user/app/{args.title_id}",
        f"/user/patch/{args.title_id}",
        f"/user/appmeta/{args.title_id}",
    ]
    previous: tuple[bool, ...] | None = None
    deadline = time.monotonic() + args.duration

    with open(args.output, "w", encoding="utf-8", newline="") as output:
        output.write("PS5 TITLE PATH TRANSITIONS\n")
        output.write(f"started={stamp()}\n")
        output.write(f"title_id={args.title_id}\n")
        output.write("method=FTP MLST existence checks; no file content read\n")
        output.flush()
        ftp: ftplib.FTP | None = None
        while time.monotonic() < deadline:
            try:
                if ftp is None:
                    ftp = ftplib.FTP()
                    ftp.connect(args.host, args.port, timeout=5)
                    ftp.login(args.user, password)
                current = []
                for path in paths:
                    try:
                        ftp.sendcmd(f"MLST {path}")
                        current.append(True)
                    except ftplib.error_perm as error:
                        if not str(error).startswith("550"):
                            raise
                        current.append(False)
                state = tuple(current)
                if state != previous:
                    line = stamp() + " " + " ".join(
                        f"{path}={'present' if exists else 'absent'}"
                        for path, exists in zip(paths, state, strict=True)
                    )
                    print(line, flush=True)
                    output.write(line + "\n")
                    output.flush()
                    previous = state
            except (OSError, EOFError, ftplib.Error) as error:
                line = f"{stamp()} ftp_error={type(error).__name__}"
                print(line, flush=True)
                output.write(line + "\n")
                output.flush()
                if ftp is not None:
                    try:
                        ftp.close()
                    except OSError:
                        pass
                ftp = None
            time.sleep(args.interval)
        output.write(f"finished={stamp()}\n")


if __name__ == "__main__":
    main()
