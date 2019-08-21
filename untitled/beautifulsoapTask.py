html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

from bs4 import BeautifulSoup as bs
soup = bs(html_doc, 'html.parser')
list_tags=['p','a']
A=[];P=[]
for tg in list_tags:
    txt = "soup.find_all('{0}')".format(tg)
    tag_list = eval(txt)
    if tg == 'a':A=tag_list
    elif tg == 'p':P=tag_list
    # print(tag_list)
for tg in list_tags:
    # print(tg)
    tg=tg.capitalize()
    for i in tg:
        print(A)
    #     dect = i.attrs
    #     print(dect)
# tag=soup.p
# tag_dect=tag.attrs
# print(tag_dect)
