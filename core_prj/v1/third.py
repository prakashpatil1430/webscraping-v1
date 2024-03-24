from bs4 import BeautifulSoup


def read_file(file_name):
    file = open(file_name, 'r')
    data = file.read()
    return data


html_file = read_file('three_sisters.html')

soup = BeautifulSoup(html_file, 'lxml')

# print(soup.title.string.strip())

### tag.contents return the list of childrens is availiable for the particular tag
# print(soup.head.contents)

# head =  soup.head
# for child in head.contents:
#     print(child if child is not None else ' ')


# body =  soup.body
# for child in body.contents:
#     print(child if child is not None else ' ', end='\n\n')

### .children returns list iterator object
# print(type(body.contents))  #list
# print(type(body.children))  # list-iterator

# for child in body.children:
#     print(child if child is not None else ' ', end='\n\n')


# .contents return the content of direct childreen
# NOTE: but it doest not give proper result bcoz it adds '\n' lines also
# print(soup.head.contents)
# print(len(soup.head.contents))

# print(soup.body.contents)
# print(len(soup.body.contents))


# .descendants use to get all child elements of tag it returnrs generator ojects
# head = soup.head.descendants

# for index, child in enumerate(head):
#     print(index)
#     print(child if child != '\n' else ' ')






# .parent method get a parent of tag

parent = soup.title.parent
# print(parent)   # return the whole content

# .name return the name of the tag
# print(parent.name)  # head


p_tag_parent =  soup.p.parent
# print(p_tag_parent)  # it return whole body tage bcoz p tag parent is body
# print(p_tag_parent.name) # body


html_parent = soup.html.parent
# print(html_parent) # it returns whole html
#print(type(html_parent))  # --> <class 'bs4.BeautifulSoup'>
# NOTE: bs4 is parent obj for parsed page like bs4 --> html

# bs4 parent is None there is no parent for bs4
#print(soup.parent) # None



### .parents it returns list(generator) of parents
link = soup.a.parent
# print(link.name) # p

link = soup.a
for parent in link.parents:
    print(parent)
    print(parent.name)
