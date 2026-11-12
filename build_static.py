"""Render the Flask site to plain HTML files for Cloudflare Pages.

Usage:  python build_static.py        -> writes everything to ./build

Cloudflare Pages serves static files, so this script renders each page with
Flask's test client and copies app/static alongside it. The timeline API is
handled on Cloudflare by functions/api/timeline_post.js (backed by D1).
"""
import os
import shutil
from pathlib import Path

# Use the in-memory SQLite DB so no MySQL server is needed at build time.
os.environ["TESTING"] = "true"

from app import app  # noqa: E402

ROOT = Path(__file__).parent
OUT = ROOT / "build"

# URL path -> output file. Cloudflare Pages serves /hobbies from hobbies.html.
PAGES = {
    "/": "index.html",
    "/hobbies": "hobbies.html",
    "/timeline": "timeline.html",
}


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()

    client = app.test_client()
    for path, filename in PAGES.items():
        response = client.get(path)
        if response.status_code != 200:
            raise SystemExit(f"{path} returned {response.status_code}")
        (OUT / filename).write_bytes(response.data)
        print(f"  {path:<10} -> build/{filename}")

    shutil.copytree(ROOT / "app" / "static", OUT / "static")
    print("  static/    -> build/static/")
    print("Done.")


if __name__ == "__main__":
    main()
