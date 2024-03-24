from bs4 import BeautifulSoup


def read_file(file_name):
    file = open(file_name, 'r')
    data = file.read()
    return data


html_file = read_file('three_sisters.html')

soup = BeautifulSoup(html_file, 'lxml')

# side ways

body = soup.body
p = soup.body.p
# print(body.prettify)
# print(p.prettify)

# next siblings

p = soup.body.p

# print(p.next_sibling) # '\n\ new line
#print(p.next_sibling.next_sibling)  # next sibling tag will return


# try from top
head = soup.head
# print(head.next_sibling) # '\n'
# print(head.next_sibling.next_sibling) # body tag


# previous sibling

# p_tag = soup.find('p', class_='last-story')
# print(p_tag.previous_sibling)
# print(p_tag.previous_sibling.previous_sibling)
# print(p_tag.previous_sibling.previous_sibling.previous_sibling.previous_sibling)



# next_siblings
p = soup.body.p
# print(p)

# all_p_tag_next_siblings = p.next_siblings
# for next_tag in all_p_tag_next_siblings:
#     print(next_tag)

# or/

# for sibling in p.next_siblings:
#     print(sibling.name if sibling != '\n' else '')
#     # print(sibling if sibling != '\n' else '')


# previous_siblings
p = soup.find('p', class_='last-story')
for sibling in p.previous_siblings:
    print(sibling.name if sibling  != '\n' else '')