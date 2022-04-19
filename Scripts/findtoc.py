import re, sys
from urllib.request import urlopen

fl_in=open("../FilesOut/test.txt","r",encoding="utf-8")
lst_in=fl_in.read()
fl_in.close()

lst=re.split("\n",lst_in)
i=0
new=[]

while (i<len(lst)):
    curr=lst[i]
    if (re.search(r'\#English\"',curr)):
        j=i+60
        new.append(lst[i:j])
        break
    i=i+1
# print(new)
i=0
new=new[0]
while (i<len(new)):
    curr=new[i]
    if (re.search(r'\#Translation',curr)):
        trans=curr
        break
    i=i+1


x=re.findall(r'tocsection-\d',trans)
x=x[0]
x=x[-1]
int(x)

# ="https://en.wiktionary.org/w/index.php?title=also&action=edit&section=7"

wrapper_left="https://en.wiktionary.org/w/index.php?title="
wrapper_right="&action=edit&section="

#Need a way to get the title...
url=wrapper_left+"also"+wrapper_right+x

page=urlopen(url)
html_bytes=page.read()
html=html_bytes.decode("utf-8")
out_name="../FilesOut/"+"alsoTest"+".txt"

fl_out=open(out_name,"w",encoding="utf-8")
fl_out.write(html)
fl_out.close()
