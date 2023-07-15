from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# Driver
options = webdriver.ChromeOptions()
options.add_argument('executable_path=C:/Users/Administrator/project/selenium/chromedriver.exe')
driver = webdriver.Chrome(options=options)
driver.get('https://www.facebook.com/')
driver.maximize_window()

time.sleep(5)

# For email or phone
# //*[@id="email"]  :- this is a xpath of email_or _phone
wait = WebDriverWait(driver,10)
enter_email = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='email']")))
enter_email.send_keys("1234567890")  # enter a email-id or phone

# For password
# //input[@id='pass'] :- this is a xpath of password
enter_password = wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@id='pass']")))
enter_password.send_keys("abcd132456")  # enter a password

# Log in button
# //button[@class="_42ft _4jy0 _6lth _4jy6 _4jy1 selected _51sy"] :- this is a xpath of log-in
log_in_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@class="_42ft _4jy0 _6lth _4jy6 _4jy1 selected _51sy"]')))
log_in_button.click()

time.sleep(5)

# To open a post section
post_button = wait.until(EC.element_to_be_clickable((By.XPATH,'//div[@class="x1i10hfl x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8 x1hl2dhg xggy1nq x87ps6o x1lku1pv x1a2a7pz x6s0dn4 xmjcpbm x107yiy2 xv8uw2v x1tfwpuw x2g32xy x78zum5 x1q0g3np x1iyjqo2 x1nhvcw1 x1n2onr6 xt7dq6l x1ba4aug x1y1aw1k xn6708d xwib8y2 x1ye3gou"]')))

time.sleep(5)

post_button.click()

time.sleep(5)

# Post statement
post_state = wait.until(EC.element_to_be_clickable((By.XPATH,'//div[@class="xzsf02u x1a2a7pz x1n2onr6 x14wi4xw x9f619 x1lliihq x5yr21d xh8yej3 notranslate"]')))
post_state.send_keys("hii,there!")

time.sleep(0)

# Create post - part button
post_button1 = wait.until(EC.element_to_be_clickable((By.XPATH,'//div[@class="x6s0dn4 x9f619 x78zum5 x1qughib x1pi30zi x1swvt13 xyamay9 xh8yej3"]')))
time.sleep(2)
post_button1.click()

time.sleep(5)


driver.quit()