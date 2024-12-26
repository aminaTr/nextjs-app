import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_simple_login():
    # Set up WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    
    try:
        # Step 1: Navigate to the login page
        driver.get("http://3.80.95.81/login") 
        
        # Step 2: Enter login credentials
        email_input = driver.find_element(By.XPATH, "//input[@placeholder='Email Address']")
        password_input = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
        email_input.send_keys("amina.tahir.pk@gmail.com")
        password_input.send_keys("Amina123")
        
        # Step 3: Submit the login form
        login_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Log in')]")
        login_button.click()
        
        # Step 4: Verify successful login
        time.sleep(3)  # Wait for redirection
        welcome_message = driver.find_element(By.XPATH, "//h1[contains(text(), 'Welcome')]")
        assert welcome_message.is_displayed(), "Login failed. Welcome message not found."
        print("Test Passed: User logged in successfully.")
    
    except Exception as e:
        print(f"Test Failed: {e}")
    
    finally:
        # Close the browser
        driver.quit()

# Run the test
if __name__ == "__main__":
    test_simple_login()
