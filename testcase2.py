import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Set up the Selenium WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

def test_login_success():
    # Open the login page
    driver.get("http://localhost:3000/login")

    # Find email and password input fields
    email_input = driver.find_element(By.XPATH, "//input[@placeholder='Email Address']")
    password_input = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
    submit_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Log in')]")

    # Enter valid credentials
    email_input.send_keys("test@example.com")
    password_input.send_keys("password")
    
    # Click the submit button
    submit_button.click()

    # Wait for the page to load and check if redirected to the feed page
    time.sleep(3)  # Adjust time as needed for your app
    assert "feed" in driver.current_url

    # Close the browser
    driver.quit()

def test_login_failure():
    # Open the login page
    driver.get("http://localhost:3000/login")

    # Find email and password input fields
    email_input = driver.find_element(By.XPATH, "//input[@placeholder='Email Address']")
    password_input = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
    submit_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Log in')]")

    # Enter invalid credentials
    email_input.send_keys("wrong@example.com")
    password_input.send_keys("wrongpassword")
    
    # Click the submit button
    submit_button.click()

    # Wait for the error message to appear
    time.sleep(3)  # Adjust time as needed for your app

    # Check for the error message
    error_message = driver.find_element(By.XPATH, "//div[contains(text(), 'Incorrect email or password')]")
    assert error_message.is_displayed()

    # Close the browser
    driver.quit()

# Run the tests
if __name__ == "__main__":
    test_login_success()
    test_login_failure()
