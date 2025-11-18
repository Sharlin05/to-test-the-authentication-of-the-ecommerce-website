from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys
from selenium.common.exceptions import InvalidSessionIdException

# Test credentials matching the demo app
USERNAME = "testuser"
PASSWORD = "testpass"

def run_test():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    try:
        driver.get('http://localhost:5000/login')
        driver.maximize_window()

    # If called with args 'auto' or username/password, perform auto-fill (optional)
        if len(sys.argv) >= 3 and sys.argv[1] == 'auto':
            # usage: python test_selenium_auth.py auto <username> <password>
            if len(sys.argv) < 4:
                print('Auto mode requires username and password: auto <username> <password>')
            else:
                user = sys.argv[2]
                pwd = sys.argv[3]
                driver.find_element(By.ID, 'username').send_keys(user)
                driver.find_element(By.ID, 'password').send_keys(pwd + Keys.RETURN)
        else:
            # Manual mode: open login page and let the user sign in manually.
            # Provide two ways to continue:
            #  - Press Enter here in the terminal after you've signed in, or
            #  - Wait up to TIMEOUT seconds for the protected page to appear automatically.
            TIMEOUT = 600  # seconds (10 minutes)
            print('\nPlease sign in manually in the opened browser window.')
            print('When finished, press Enter here to continue, or wait up to {} seconds for auto-detect.'.format(TIMEOUT))

            # Start a background waiter that will detect login by looking for product elements or welcome heading
            wait = WebDriverWait(driver, TIMEOUT)
            detected = False
            try:
                # Check for product list first
                wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.product')))
                detected = True
            except InvalidSessionIdException:
                print('Browser session lost (browser window may have been closed). Aborting wait.')
            except Exception:
                # fallback to welcome heading
                try:
                    wait.until(EC.presence_of_element_located((By.XPATH, "//h2[contains(.,'Welcome') ]")))
                    detected = True
                except InvalidSessionIdException:
                    print('Browser session lost (browser window may have been closed). Aborting wait.')
                except Exception:
                    # timed out — but we'll allow the user to press Enter to continue anyway
                    pass

            # Allow the user to press Enter to continue early
            try:
                input('Press Enter to continue (or wait for auto-detect to finish)...')
            except Exception:
                # In non-interactive environments input may fail; ignore and proceed
                pass

        time.sleep(1)
        # Check for product list on the protected page
        products = driver.find_elements(By.CSS_SELECTOR, '.product')
        if products:
            print('Login detected — product page reached. Found products:')
            for p in products:
                print(' -', p.text)
        else:
            body = driver.find_element(By.TAG_NAME, 'body').text
            if 'Welcome' in body:
                print('Login detected — welcome page reached (no products found)')
            else:
                print('Login may have failed — protected page not reached')

        # Click logout and verify redirected to login
        try:
            driver.find_element(By.LINK_TEXT, 'Logout').click()
            time.sleep(1)
            if 'Login' in driver.title or 'Login' in driver.find_element(By.TAG_NAME, 'body').text:
                print('Logout successful')
            else:
                print('Logout may have failed')
        except Exception:
            print('Could not find Logout link to click; maybe not on protected page.')

    finally:
        driver.quit()

if __name__ == '__main__':
    run_test()
