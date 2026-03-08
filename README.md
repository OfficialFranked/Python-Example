# Hello Franked — Example Template

A minimal example showing how to add Franks licenses validations to your app.  
**Pick your language, copy the config, run.**

---

## Quick start (Python)

1. **Get App Secret** from [franked.xyz](https://franked.xyz): create a project → copy App Secret.
2. **Copy config:**
   ```bash
   cd python
   cp config.example config.py
   ```
3. **Edit `config.py`** — set `APP_SECRET` only. (No license key needed to set up.)
4. **Run:**
   ```bash
   pip install -r requirements.txt
   python main.py
   ```
   If you haven’t set a license key in config, you’ll be prompted to enter one at runtime.

---

## Quick start (C++)

See **[license-demo](../license-demo/)** — set your App Secret, build, run. Enter the license key when prompted (or set it in code).

---

## What the code does

1. **Init** — connects to Franked, fetches project info.
2. **Activate** — validates the license key; fails if expired, revoked, or max devices reached.
3. **Run app** — your real logic runs only if the license is valid.

---

## Adding to your project

| Step | Python | C++ |
|------|--------|-----|
| 1. Validate at startup | `validate(api_url, app_secret, license_key)` | `client.validate(license_key)` |
| 2. Periodic check (optional) | `lp.check(license_key)` | `client.check(license_key)` |

See [INTEGRATION.md](../../docs/INTEGRATION.md) for the full reference.
