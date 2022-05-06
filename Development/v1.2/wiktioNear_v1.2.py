#!/usr/bin/python3

from urllib.request import urlopen
import re, datetime, sys, subprocess, os


############################################################################
#            iii kk     tt    iii        NN   NN                       
# ww      ww     kk  kk tt         oooo  NNN  NN   eee    aa aa rr rr  
# ww      ww iii kkkkk  tttt  iii oo  oo NN N NN ee   e  aa aaa rrr  r 
#  ww ww ww  iii kk kk  tt    iii oo  oo NN  NNN eeeee  aa  aaa rr     
#   ww  ww   iii kk  kk  tttt iii  oooo  NN   NN  eeeee  aaa aa rr     
#                                                                          #
# _v1.2 May 2022                                                           # 
# A program written by Ian Kirby (ianlkirby@vivaldi.net) for scraping      #
# translation data from wiktionary.org and generating lists to compare     #
#                                                                          #
############################################################################


def scrape_pages(lst,time):

      

      i=0
      while(i<len(lst)):
            sub_lst=lst[i]
            #Initialize the file that will be written to.
            file=open("./Raw_Files/Raw_HTML/"+sub_lst[2],'a',encoding="utf8")
            
            page=urlopen(sub_lst[1])
            html_bytes=page.read()
            html=html_bytes.decode("utf-8")
            # file.write(html)
            # file.close()
            
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
                  nurl="https://en.wiktionary.org/w/index.php?title="+sub_lst[0]+"&action=edit&section="+section
                  npage=urlopen(nurl)
                  nhtml_bytes=npage.read()
                  nhtml=nhtml_bytes.decode("utf-8")
                  x=re.split(r'\{\{trans-bottom\}\}',nhtml)
                  x=x[0]
                  x=re.split("===Translations===",x)

                  file.write(x[1])
                  file.close()

                  # bigLst_file=open("./Raw_Files/Raw_HTML/BigList_"+time,'a',encoding="utf8")
                  # bigLst_file.write(x[1])
                  # bigLst_file.close()

                  # file_out=open("./Files/wkn_v2_pre_cleaned/"+label,"a",encoding="utf-8")
                  # file_out.write(x[1])
                  # file_out.close()

                  # file_out=open("./Files/wkn_v2_pre_cleaned/BigList-"+time_tag+".txt",'a', encoding="utf-8")
                  # file_out.write(x[1])
                  
                  # file_out.close()


                  j=j+1
           

            i=i+1




def open_list(x):

      #Get the current time, to be suffixed to the filename
      d=datetime.datetime.utcnow()
      day_month="{:%h%d}".format(d)
      day_month=day_month+"-"
      hour_min="{:%H%M}".format(d)
      time_suffix=day_month+hour_min

      fl=open("./Input_Lists/"+x,'r',encoding="utf8")
      x=fl.read() #read the CSV file in as a string
      fl.close()
      x=re.split("\n",x) #split the string to an array, sort by linebreaks

      i=0
      lst_as_array=[]
      while(i<len(x)):
            curr=x[i]
            curr=re.split(",",curr)
            if(curr[0]==''):
                  pass
            elif(len(curr)==1):
                  curr.append("https://en.wikipedia.org/wiki/"+curr[0]+"#English")
                  curr.append(curr[0]+time_suffix+".txt")#Making the output filename
                  lst_as_array.append(curr)
            elif(len(curr)>1):
                  url=curr[1]
                  if(url[-8:]!="#English"):
                        curr.pop()
                        url=url+"#English"
                        curr.append(url)
                  curr.append(curr[0]+time_suffix+".txt")
                  lst_as_array.append(curr)
            i=i+1

      # print(lst_as_array)
      print("Scraping pages...\n"+("-"*76))
      scrape_pages(lst_as_array,time_suffix+".txt")


      
      

def check_list_dir():
      dir=os.listdir('./Input_Lists')
      i=0
      csv_in_dir=[]
      while(i<len(dir)):
            curr=dir[i]
            if(len(curr)>4 and curr[-4:]==".csv"):
                  csv_in_dir.append(curr)
            # else:
                  # print("\t"+curr+" is not a .csv file, so is being ignored")
            i=i+1
      print("-"*76+"\n")
      i=0
      while(i<len(csv_in_dir)):
            print(str(i+1)+") "+csv_in_dir[i])
            i=i+1
      answer=input("Enter the number of the file:\n")
      answer=(int(answer)-1)
      # print(answer)
      if(answer<0 or (answer>(len(csv_in_dir)-1))):
            print("I don't recognize that, please enter number.")
            check_list_dir()
      else:
            lst=csv_in_dir[answer]
            return lst
      
                  


def start(logo,version,bar):
      print(logo+"\n"+"wiktioNear_"+version+"\nA program written by Ian Kirby (ianlkirby@vivaldi.net)\n"+bar+"\n")

      if(not (len(sys.argv)>1)):
            print("You did not enter a file.  I will check in the \"Input_Lists\" directory.")
            lst=check_list_dir()
            # print(lst)
      else:
            lst=sys.argv[1]
      open_list(lst)

version="v1.2"
logo="""             
           iii kk     tt    iii        NN   NN                       
ww      ww     kk  kk tt         oooo  NNN  NN   eee    aa aa rr rr  
ww      ww iii kkkkk  tttt  iii oo  oo NN N NN ee   e  aa aaa rrr  r 
 ww ww ww  iii kk kk  tt    iii oo  oo NN  NNN eeeee  aa  aaa rr     
  ww  ww   iii kk  kk  tttt iii  oooo  NN   NN  eeeee  aaa aa rr     
                                                                     
"""
bar="############################################################################"
start(logo,version,bar)
