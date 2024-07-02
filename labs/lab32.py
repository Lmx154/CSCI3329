import requests
from bs4 import BeautifulSoup

url = 'https://www.utrgv.edu/csci/faculty/index.htm'
response = requests.get(url)
if response.status_code == 200:
    print("Web page fetched successfully!")
else:
    print("Failed to retrieve the web page. Status code:", response.status_code)

soup = BeautifulSoup(response.content, 'html.parser')
listings = soup.find_all('div', {"class": "listing"})

# Find all 'a' tags with 'href' containing 'mailto:'
for listing in listings:
    email_tags = listing.find_all('a', href=lambda x: x and x.startswith('mailto:'))
    for email_tag in email_tags:
        print(email_tag['href'].split(':')[1])
