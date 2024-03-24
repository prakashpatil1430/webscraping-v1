from bs4 import BeautifulSoup


def read_file(file_name):
    file = open(file_name, 'r')
    data = file.read()
    return data


html_file = read_file('intro_to_soup_html.html')
# print(html_file)

# syntax = BeautifulSoup(html_data, parser)
soup = BeautifulSoup(html_file, 'lxml')
# print(soup)


# preiftfy
# print(soup.prettify)

# to check class of body tag
print(soup.body['class'])

# tags

title = soup.title.string
# print(title)

# to change title
soup.title.string.replace_with('new title added patil')
# print(soup.title.string)


# finding all div elements
divs = soup.find_all('div')
# print(divs)

# find div elemmet with class name
divs = soup.find_all('div', class_='first-div')
# print(divs)


# find div elemmet with class name p tage inside
divs = soup.find('div', class_='first-div').find('p').text
# print(divs)

# find all pages and its values

all_p_tags = soup.find_all('p')
for ptag in all_p_tags:
    print(ptag.text)

