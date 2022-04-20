import re, sys
from urllib.request import urlopen

# fl_in=open("../FilesOut/test.txt","r",encoding="utf-8")
##

#Testing how to handle 
url="https://en.wiktionary.org/wiki/run#English"
page=urlopen(url)
html_bytes=page.read()
html=html_bytes.decode("utf-8")
# out_name="./FilesOut/"+name+".txt"

lst_in=html

#If you want to read it it as 
# if (len(sys.argv)<3):
#     sys.exit("Error")
# fl_in=open(str(sys.argv[1]),"r",encoding="utf-8")


# commented out for test...
# lst_in=fl_in.read()
# fl_in.close()

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

level1="toclevel\-1\stocsection\-1\">" #Makes sure it's a language-level item
eng_label=r'a href="#English' #label that says it's English
translation_label=r'a href="#Translations' #Label that says it's a translation
translation_hits=[] #For storing hits to get stuff; needed in case there are two items with translations


#Iterate through each new element to see if it's English...
while (i<len(new)):
    curr=new[i]
    if(bool(re.search(level1,curr))):
        # print("Match on "+curr)
        if(bool(re.search(eng_label,curr))):
            if (bool(re.search(translation_label,curr))):
                translation_hits.append(curr)
    else:
        # print("Something else")
        pass
    i=i+1

print(translation_hits)

# contains_hits=[]
# while (i<len(new)):
#     curr=new[i]
#     if(bool(re.search("a href=\"\#"+"",curr))):

#Works, but only gives you the first example.
# while (i<len(new)):
#     curr=new[i]
#     if (re.search(r'\#Translation',curr)):
#         trans=curr
#         break
#     i=i+1


# # x=re.findall(r'tocsection-\d',trans)
# # x=x[0]
# # x=x[-1]
# # int(x)

# # ="https://en.wiktionary.org/w/index.php?title=also&action=edit&section=7"

# wrapper_left="https://en.wiktionary.org/w/index.php?title="
# wrapper_right="&action=edit&section="

# #Need a way to get the title...
# url=wrapper_left+"also"+wrapper_right+x

# page=urlopen(url)
# html_bytes=page.read()
# html=html_bytes.decode("utf-8")
# out_name="../FilesOut/"+"alsoTest"+".txt" # 

# fl_out=open(out_name,"w",encoding="utf-8")
# fl_out.write(html)
# fl_out.close()
