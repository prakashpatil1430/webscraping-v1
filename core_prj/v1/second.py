import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

ua = UserAgent()

headers = {'user-agent': ua.chrome}

url = 'https://www.python.org/'

response = requests.get(url=url, headers=headers)

html_page = response.content

soup = BeautifulSoup(html_page, 'lxml')

main_navigation_menu = soup.find('nav', id='mainnav')
main_menu_items = main_navigation_menu.find_all("li", class_="tier-1")

for li in main_menu_items:
    main_a_tag = li.find('a')
    # or
    # it will get first matched tag
    # main_a_tag = li.a

    menu_text = main_a_tag.get_text(strip=True)
    menu_link = main_a_tag.get('href')
    print(f"Text: {menu_text}, Link: {menu_link}")
