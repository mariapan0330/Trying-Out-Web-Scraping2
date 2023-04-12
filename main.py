import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Parakeet'
response = requests.get(url)
html_content = response.text
print(response)
soup = BeautifulSoup(html_content, 'html.parser')
# print(soup.prettify())

# find the job title and company name elements using Beautiful Soup's selector syntax
title = soup.find(class_='mw-page-title-main')
print(title)

# use the job title and company name in your app