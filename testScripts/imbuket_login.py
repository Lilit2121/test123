from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

login_url = 'https://imbucket.vercel.app/'
username = 'test@gmail.com'
password = 'Test123!'

chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-gpu")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

try:

    driver.get(login_url)

    # Wait for the page to load
    time.sleep(3)  # Adjust wait time as necessary

    # Click the login button
    login_button = driver.find_element(By.CLASS_NAME, 'user-utility_modal_open_block__FtKIt')
    login_button.click()

    # Wait for the login modal to appear
    time.sleep(3)  # Adjust wait time as necessary

    # Enter username and password
    username_field = driver.find_element(By.CLASS_NAME, 'log_in_inputs__Wj4tL')
    password_field = driver.find_element(By.CLASS_NAME, 'password'),

    username_field.send_keys(username),
    password_field.send_keys(password)

    password_field.submit()
    login_submit_button = driver.find_element(By.CSS_SELECTOR,  '.log_in_button__Nw3ls.button_main_button__bagVO'
                                                                '.button_disabled__wzXfC')
    login_submit_button.click()
    time.sleep(5)

    print("Login attempted")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    driver.quit()
