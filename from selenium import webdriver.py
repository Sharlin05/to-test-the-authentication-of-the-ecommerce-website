from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_login_logout():
    # User inputs
    username_input = input("Enter username: ")
    password_input = input("Enter password: ")

    # Setup browser (NO HEADLESS NEEDED)
    driver = webdriver.Chrome(ChromeDriverManager().install())

    try:
        # Open login page
        driver.get("https://the-internet.herokuapp.com/login")
        driver.maximize_window()

        # Enter username
        driver.find_element(By.ID, "username").send_keys(username_input)

        # Enter password
        driver.find_element(By.ID, "password").send_keys(password_input + Keys.RETURN)

        time.sleep(2)

        # Check result
        result = driver.find_element(By.ID, "flash").text
        print("\nLogin Result:", result)

        # If login successful → logout
        if "secure area" in result:
            logout_button = driver.find_element(By.XPATH, "//a[@class='button secondary radius']")
            logout_button.click()
            time.sleep(2)

            logout_msg = driver.find_element(By.ID, "flash").text
            print("Logout Result:", logout_msg)

    finally:
        driver.quit()


if __name__ == "__main__":
    test_login_logout()
