# trying out selenium for dynamic pages like the one looking for.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Start the browser and load the webpage
browser = webdriver.Edge('./msedgedriver.exe')
browser.get('https://stalwart-tiramisu-dee856.netlify.app/')

# Find the input element and extract its value
# input_element = browser.find_element_by_css_selector('input[aria-label="Company"]')
# company_value = input_element.get_attribute('value')
element = browser.find_element_by_css_selector("a[class=navbar-brand]")
print(element)

# Close the browser
browser.quit()