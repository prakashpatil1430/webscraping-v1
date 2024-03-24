import requests
from fake_useragent import UserAgent

ua = UserAgent()

headers = {'user-agent': ua.chrome}
# print(ua.chrome)

url = 'https://google.com'

response = requests.get(url=url, headers=headers)

# print(response)
# print(response.headers)


print(response.content)

