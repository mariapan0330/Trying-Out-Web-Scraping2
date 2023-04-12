# trying out selenium for dynamic pages like the one looking for.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



# Start the browser and load the webpage
browser = webdriver.Edge('./msedgedriver.exe')
browser.get('https://huntr.co/track/boards/6331de3de9d9500028431820/board')
username_input = browser.find_element(By.NAME, 'email')
username_input.send_keys("maria.pan0330@gmail.com")
password_input = browser.find_element(By.NAME, 'password')
password_input.send_keys('mP))#$2060')
submit_button = browser.find_element(By.CLASS_NAME, 'Button__BtnComponent-a7uspp-0')
submit_button.click()

welcome_message = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'ReactVirtualized__Grid'))
)

# Extract the text content of the welcome message
# welcome_text = welcome_message.text


# Find the input element and extract its value
# input_element = browser.find_element_by_css_selector('input[aria-label="Company"]')
# company_value = input_element.get_attribute('value')
# elements = browser.find_elements(By.CLASS_NAME,"Text__Paragraph-sc-1rtclo2-1")
el = browser.find_element(By.CSS_SELECTOR, "#react-container > div > div:nth-child(2) > div:nth-child(2) > section > div > div > div > div > div > main > div > div > div > div:nth-child(2) > div:nth-child(3) > div:nth-child(1) > div > div > div:nth-child(1)")

# element = browser.find_element(By.XPATH, '//p[@color="#000024" and @title="test title"]')

# find_element_by_class_name("a[class=navbar-brand]")
print("==========~+~+~+~+~+~+==========")
# for el in elements[20:30]:
#     print(el.text)
# # print(elements[20:30].text)
spl = el.text.split("\n")
print(el.text)
print(spl)

# Close the browser
browser.quit()