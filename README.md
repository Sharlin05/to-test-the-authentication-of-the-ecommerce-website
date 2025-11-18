# to-test-the-authentication-of-the-ecommerce-website
This automation script tests user authentication on a demo shopping website. It first creates a new account by entering user-provided email and password, then logs in using the same credentials to verify successful signup and login. The script uses Selenium WebDriver to automate the entire process.
# Shopping Demo (Authentication test)

This is a minimal Flask app used to demonstrate and test authentication with Selenium.

Demo credentials:
- username: `testuser`
- password: `testpass`

Quick start (Windows PowerShell, using workspace venv):

1. Create and activate a venv (optional, recommended):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Start the Flask app:

```powershell
# From e:\STA practicle\shopping_app
& "E:/STA practicle/.venv/Scripts/python.exe" app.py
```

4. In a separate terminal, run the Selenium test (this will open a Chrome window):

```powershell
& "E:/STA practicle/.venv/Scripts\python.exe" test_selenium_auth.py
```

Notes:
- Make sure Chrome is installed. `webdriver-manager` will download a matching ChromeDriver.
- To run headless, update `test_selenium_auth.py` to set ChromeOptions.
