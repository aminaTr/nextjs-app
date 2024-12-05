import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Set up the Selenium WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

def test_comment_success():
    # Log in to the application
    driver.get("http://54.82.209.59:3000/login")
    email_input = driver.find_element(By.XPATH, "//input[@placeholder='Email Address']")
    password_input = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
    submit_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Log in')]")
    
    # Replace with valid credentials
    email_input.send_keys("test@example.com")
    password_input.send_keys("password")
    submit_button.click()
    
    # Wait for redirection to feed page
    time.sleep(3)  # Adjust if necessary

    # Navigate to a specific post where comments are allowed
    driver.get("http://localhost:3000/posts/your-post-id")  # Replace with an actual post ID

    # Find the comment input field and submit button
    comment_input = driver.find_element(By.XPATH, "//input[@placeholder='Add your comment']")
    comment_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Comment')]")

    # Enter a comment and submit
    comment_input.send_keys("This is a test comment.")
    comment_button.click()

    # Wait for the comment submission response
    time.sleep(3)  # Adjust if necessary

    # Check if the comment is visible on the page
    comment_display = driver.find_element(By.XPATH, "//div[contains(text(), 'This is a test comment.')]")
    assert comment_display.is_displayed()

    # Close the browser
    driver.quit()

def test_prompt_login_to_comment():
    # Navigate directly to the post page without logging in
    driver.get("http://localhost:3000/posts/your-post-id")  # Replace with an actual post ID

    # Check if the prompt to log in is displayed
    login_prompt = driver.find_element(By.XPATH, "//div[contains(text(), 'Please sign in to comment')]")
    assert login_prompt.is_displayed()

    # Close the browser
    driver.quit()

# Run the tests
if __name__ == "__main__":
    test_comment_success()
    test_prompt_login_to_comment()
