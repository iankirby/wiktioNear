import re, sys
from urllib.request import urlopen


url="https://en.wiktionary.org/wiki/run#English"
page=urlopen(url)
html_bytes=page.read()
html=html_bytes.decode("utf-8")

lst=re.split("\n",html)
i=0
new=[]

#This is the old way... let's try something else (below)
# while (i<len(lst)):
#     curr=lst[i]
#     if (re.search(r'\#English\"',curr)):
#         j=i+60
#         new.append(lst[i:j])
#         break
#     i=i+1
# new=new[0]
# print(new)
# print(len(new))
# i=0
# new=new[0]


level1="toclevel\-1\stocsection\-1\">" #Makes sure it's a language-level item
eng_label=r'a href="#English' #label that says it's English
translation_label=r'a href="#Translations' #Label that says it's a translation
translation_hits=[] #For storing hits to get stuff; needed in case there are two items with translations

# Let's try splitting the entire array wherever it says "level"
# print(isinstance(html,str))
sth=re.split(level1,html)

print(sth[0])
print(len(sth))