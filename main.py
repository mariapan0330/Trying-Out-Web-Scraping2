import requests
from bs4 import BeautifulSoup

url = 'https://example.com'  # replace with the URL of the website you want to extract HTML from
response = requests.get(url)
html_content = response.text
soup = BeautifulSoup(html_content, 'html.parser')

# find the job title and company name elements using Beautiful Soup's selector syntax
job_title = soup.select_one('.job-title').text
company_name = soup.select_one('.company-name').text

# use the job title and company name in your app