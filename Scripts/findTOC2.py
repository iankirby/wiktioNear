import re, sys,subprocess,os
from urllib.request import urlopen



# url="https://en.wiktionary.org/wiki/run#English"
url=(str(sys.argv[1]))
name=(str(sys.argv[2]))
out_name=(str(sys.argv[3]))

page=urlopen(url)
html_bytes=page.read()
html=html_bytes.decode("utf-8")

lst=re.split("\n",html)
i=0
new=[]

while(i<len(lst)):
    curr=lst[i]
    if (bool(re.search(r'toclevel-\d',curr))):
        new.append(curr)
        i=i+1
    else:
        i=i+1
# print(new)

# x=re.findall(r'toclevel-\d',new[5])
# print(x)

# a=r'toclevel-\d'

# x=re.findall("toclevel-\d tosection-([\d]+)|a\shref=\"\#([^\"]+)",html)
toc_level=re.findall(r'toclevel-([\d]+)',html)
toc_section=re.findall(r' tocsection-([\d]+)',html)
cat=re.findall(r'a href=\"\#([^\"]+)',html)
# print(toc_level)
# print(toc_section)
# print(cat)

secs=[]
i=0
while(i<len(toc_level)):
    curr=cat[i]
    if(bool(re.match("English|Translation",curr))):
        if(bool(re.match("English",curr))):
            i=i+1
        else:
            secs.append(toc_section[i])
    i=i+1

# # print(secs)
# wrapper_left="https://en.wiktionary.org/w/index.php?title="
# wrapper_right="&action=edit&section="



i=0
while(i<len(secs)):
    section=str(secs[i])
    nurl="https://en.wiktionary.org/w/index.php?title="+name+"&action=edit&section="+section
    npage=urlopen(nurl)
    nhtml_bytes=npage.read()
    nhtml=nhtml_bytes.decode("utf-8")
    x=re.split(r'\{\{trans-bottom\}\}',nhtml)
    x=x[0]
    x=re.split("===Translations===",x)
    # print(x[0])
    # print(x[1])
    file_name="./FilesOut/"+out_name+".txt"
    # file_name=out_name+".txt"
    # file_out=open(file_name,"x")
    file_out=open(file_name,"a",encoding="utf-8")
    file_out.write(x[1])
    file_out.close()
    i=i+1
# print(nurl)



