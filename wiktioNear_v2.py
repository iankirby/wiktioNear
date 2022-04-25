from urllib.request import urlopen
# import csv, re, datetime, sys, subprocess, os
import re, datetime, sys, subprocess, os

#I'm revising the flow of my scripts, because the first version isn't particularly modular and is annoying to edit.

#This function scrapes the pages
def scrape_pages(lst):

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
            section=str(secs[i])
            nurl="https://en.wiktionary.org/w/index.php?title="+name+"&action=edit&section="+section
            npage=urlopen(nurl)
        # print(toc_section)

        i=i+1

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

    scrape_pages(verified_lst)


def main():

    #utc time the script was called
    d=datetime.datetime.utcnow()
    day_month="{:%h%d}".format(d)
    day_month=day_month+"-"
    hour_min="{:%H%M}".format(d)
    day_month_hour_min=day_month+hour_min

    x=open("./wkn_v2_pre_cleaned/bigList"+day_month_hour_min+".txt",'a',encoding="utf8")
    x.truncate(0)
    x.close()

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