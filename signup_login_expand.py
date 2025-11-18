from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

# =========================
#  USER INPUTS (optional CLI)
# =========================
if len(sys.argv) >= 3:
    email_input = sys.argv[1]
    password_input = sys.argv[2]
else:
    email_input = input("Enter email for signup: ")
    password_input = input("Enter password for signup: ")

# =========================
#  START SELENIUM
# =========================
service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
# options.add_argument('--headless=new')  # uncomment to run headless
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()
wait = WebDriverWait(driver, 15)

try:
    # =========================
    #  STEP 1 — SIGN UP
    # =========================
    driver.get("https://practice.expandtesting.com/notes/app/register")

    # wait for form fields
    wait.until(EC.presence_of_element_located((By.ID, 'email')))
    driver.find_element(By.ID, "email").clear()
    driver.find_element(By.ID, "email").send_keys(email_input)
    driver.find_element(By.ID, "password").send_keys(password_input)
    driver.find_element(By.ID, "confirmPassword").send_keys(password_input)
    driver.find_element(By.XPATH, "//button[text()='Create Account']").click()

    # wait for redirect/confirmation
    time.sleep(60)
    print("✔ Account creation step finished (check browser for success message).")

    # =========================
    #  STEP 2 — LOG IN
    # =========================
    driver.get("https://practice.expandtesting.com/notes/app/login")

    wait.until(EC.presence_of_element_located((By.ID, 'email')))
    driver.find_element(By.ID, "email").clear()
    driver.find_element(By.ID, "email").send_keys(email_input)
    driver.find_element(By.ID, "password").send_keys(password_input)
    driver.find_element(By.XPATH, "//button[text()='Login']").click()

    # wait for possible redirect to notes
    try:
        wait.until(EC.url_contains('notes'))
    except Exception:
        pass

    time.sleep(60)

    if "notes" in driver.current_url:
        print("✔ Successfully logged in!")
    else:
        print("✘ Login may have failed. Current URL:", driver.current_url)

except Exception as e:
    print("Exception during run:", repr(e))

finally:
    driver.quit()
