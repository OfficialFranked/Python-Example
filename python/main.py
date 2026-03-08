"""
Hello Franked — minimal Python example.
Validates a license before running your app.
You only need APP_SECRET to set up; license key can be entered at runtime.
"""

import sys
from pathlib import Path

# Use lp_sdk from the repo (run from examples/hello-franked/python/)
_root = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_root / "packages" / "sdk" / "python"))
from lp_sdk import validate

try:
    from config import API_URL, APP_SECRET, LICENSE_KEY
except ImportError:
    print("Copy config.example to config.py and add your App Secret.")
    sys.exit(1)

if __name__ == "__main__":
    license_key = LICENSE_KEY
    if not license_key:
        license_key = input("Enter license key: ").strip()
    if not license_key:
        print("No license key provided.")
        sys.exit(1)

    print("Checking license...")
    if not validate(API_URL, APP_SECRET, license_key):
        print("Invalid or expired license.")
        sys.exit(1)

    print("License valid!")
    print("Hello from your licensed app.")
