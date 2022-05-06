from urllib.request import urlopen
# import csv, re, datetime, sys, subprocess, os
import re, datetime, sys, subprocess, os

#I'm revising the flow of my scripts, because the first version isn't particularly modular and is annoying to edit.



##Here
def send_to_perl_script(time_tag):
    dir=os.listdir('./Files/wkn_v2_pre_cleaned')
    i=0
    search_dir=[]
    while(i<len(dir)):
        # print(dir[i])
        curr=dir[i]
        i=i+1
        if(curr[-14:]==time_tag+".txt"):
            search_dir.append(curr)
        i=i+1
    
    i=0
    while(i<len(search_dir)):
        file="./Scripts/cleaner_v2.pl"




#This function scrapes the pages
def scrape_pages(lst,time_tag):

    i=0
    while(i<len(lst)):
        curr=lst[i]
        
        name=curr[0]
        label=curr[1]
        url=curr[2]

        page=urlopen(url)
        html_bytes=page.read()
        html=html_bytes.decode("utf-8")

        as_lst=re.split("\n",html)

        #I don't know why I have this...
        # j=0
        # new=[]
        # # while(j<len(as_lst)):
        # #     item=as_lst[j]
        # #     if(bool(re.search(r'toclevel-\d',item))):
        # #         new.append(item)
        # #         j=j+1
        # #     else:
        # #         j=j+1
        

        toc_level=re.findall(r'toclevel-([\d]+)',html)
        toc_section=re.findall(r' tocsection-([\d]+)',html)
        cat=re.findall(r'a href=\"\#([^\"]+)',html)

        secs=[]
        j=0
        while(j<len(toc_level)):
            bloop=cat[j]
            if(bool(re.match("English|Translation",bloop))):
                if(bool(re.match("English",bloop))):
                    j=j+1
                else:
                    secs.append(toc_section[j])
            j=j+1
        
        j=0
        while(j<len(secs)):
            section=str(secs[j])
            nurl="https://en.wiktionary.org/w/index.php?title="+name+"&action=edit&section="+section
            npage=urlopen(nurl)
            nhtml_bytes=npage.read()
            nhtml=nhtml_bytes.decode("utf-8")
            x=re.split(r'\{\{trans-bottom\}\}',nhtml)
            x=x[0]
            x=re.split("===Translations===",x)

            file_out=open("./Files/wkn_v2_pre_cleaned/"+label,"a",encoding="utf-8")
            file_out.write(x[1])
            file_out.close()

            file_out=open("./Files/wkn_v2_pre_cleaned/BigList-"+time_tag+".txt",'a', encoding="utf-8")
            file_out.write(x[1])
            
            file_out.close()


            j=j+1
        i=i+1
    print("Making log...")

    x=open("./Files/log.txt",'a',encoding="utf8")
    x.write("*"*45)
    x.write("\n")
    # x.readlines()

    i=0
    while(i<len(lst)):
        curr=lst[i]
        x.write(curr[0]+", "+curr[1]+", "+curr[2]+"\n")
        i=i+1
    x.write("*"*45)
    x.write("\n")
    x.close()
    print("Cleaning pages...")
    send_to_perl_script(time_tag)
    

def verify_urls(lst,time_tag):

    verified_lst=[]
    i=0
    while(i<len(lst)):
        sub_verified=[]
        lst_item=lst[i]
        lst_item=re.split(', ', lst_item)

        lemma=lst_item[0]
        label_tagged=lemma+"-"+time_tag+".txt"

        if(len(lst_item)==1):
            url_to_fetch="https://en.wiktionary.org/wiki/"+lemma+"#English"
        else:
            url_to_fetch=lst_item[1]

            if(url_to_fetch[-6:]!="nglish"):
                url_to_fetch=url_to_fetch+"#English"
        
        
        sub_verified.append(lemma)
        sub_verified.append(label_tagged)
        sub_verified.append(url_to_fetch)

        verified_lst.append(sub_verified)

        i=i+1
    # print(verified_lst)
    print("Scraping pages...")

    scrape_pages(verified_lst,time_tag)


def main():

    #utc time the script was called
    d=datetime.datetime.utcnow()
    day_month="{:%h%d}".format(d)
    day_month=day_month+"-"
    hour_min="{:%H%M}".format(d)
    day_month_hour_min=day_month+hour_min

    # x=open("./Files/wkn_v2_pre_cleaned/bigList"+day_month_hour_min+".txt",'a',encoding="utf8")
    # x.truncate(0)
    # x.close()

    if(len(sys.argv)==2):
        lst_in=sys.argv[1]
    else:
        lst_in="list.csv"

    fl_in=open(lst_in,'r',encoding="utf8")
    lst_in=fl_in.read()
    fl_in.close()

    lst_in=re.sub("\n\n","",lst_in) #Remove empty line breaks

    lst_in=re.split("\n",lst_in)

    print("Verifying urls...")
    verify_urls(lst_in,day_month_hour_min)

main()