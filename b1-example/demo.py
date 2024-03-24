from bs4 import BeautifulSoup
import requests

url = "https://www.wikipedia.org/"

# Getting the webpage, creating a Response object.
response = requests.get(url)
print(response.status_code)

headers = response.headers

for key , value in headers.items():
    print(f'{key} --{value}')

# Extracting the source code of the page.
data = response.text

# Passing the source code to Beautiful Soup to create a BeautifulSoup object for it.
soup = BeautifulSoup(data, 'html.parser')

# Extracting all the <a> tags into a list.
tags = soup.find_all('a')

# Extracting URLs from the attribute href in the <a> tags.
# for tag in tags[:10]:
#     print(tag.get('href'))
