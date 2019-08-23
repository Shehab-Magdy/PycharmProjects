'''referance .... https://beautiful-soup-4.readthedocs.io/en/latest/ '''
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
attributs_dict_a = {};
attributs_dict_p = {}
for tg in list_tags:
    txt = "soup.find_all('{0}')".format(tg)
    tag_list = eval(txt)
    if tg == 'a':
        A = tag_list
        for tag in A:
            attributs_dict_a[tag] = tag.attrs
    elif tg == 'p':
        P = tag_list
        for tag in P:
            attributs_dict_p[tag] = tag.attrs

for k in list(attributs_dict_a.keys()):
    attributs_dict_a[k] = {key: val for key, val in attributs_dict_a[k].items() if key in ['class', 'id']}

for k in list(attributs_dict_p.keys()):
    attributs_dict_p[k] = {key: val for key, val in attributs_dict_p[k].items() if key in ['class', 'id']}

print(attributs_dict_a)
print(attributs_dict_p)
