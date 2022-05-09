#!/usr/bin/python3


############################################################################
#            iii kk     tt    iii        NN   NN                           #
# ww      ww     kk  kk tt         oooo  NNN  NN   eee    aa aa rr rr      #
# ww      ww iii kkkkk  tttt  iii oo  oo NN N NN ee   e  aa aaa rrr  r     #
#  ww ww ww  iii kk kk  tt    iii oo  oo NN  NNN eeeee  aa  aaa rr         #
#   ww  ww   iii kk  kk  tttt iii  oooo  NN   NN  eeeee  aaa aa rr         #
#                                                                          #
# _v1.2.1 May 2022                                                         # 
# A program written by Ian Kirby (ianlkirby@vivaldi.net) for scraping      #
# translation data from wiktionary.org and generating lists to compare     #
#       Modifications: rather than writing a bunch of new files, this      #
#       version only makes a single temp.txt file that passes stuff        #
#       between Python and Perl.                                           #
#                                                                          #
#                                                                          #
#                                                                          #
#                                                                          #
#                                                                          #
############################################################################

from urllib.request import urlopen
import re, datetime, sys, subprocess, os, time


# def cheating_recursion1(part,file):

# def cheating_recursion2(part,file):

def final_clean(file):
      fl=open(file+".txt",'r+',encoding="utf8")
      x=fl.read()
      fl.truncate(0)
      fl.close()
      #delete the place-holder file
      

      x=re.split("\n",x)
      x.pop()
      if(not(len(x)%2)==0):
            sys.exit("Error...")
      else:
            i=0
            new=[]
            while(i<len(x)):
                  temp=[]
                  ln1=x[i]
                  ln2=x[i+1]
                  ln1=re.split(",",ln1)
                  ln2=re.split(",",ln2)
                  j=0
                  while(j>len(ln1)):
                        temp.append(ln1[j])
                        j=j+1
                  j=0
                  while(j<len(ln2)):
                        temp.append(ln2[j])
                        j=j+1
                  new.append(temp)
                  i=i+2
            # print(new)


      subprocess.call(['rm',file+".txt"])
      fl=open(file+".csv",'a+',encoding="utf8")

      #Now it's ready to print out the rest
      i=0
      while(i<len(new)):
            temp=new[i]
            as_string=""
            j=0
            while(j<len(temp)):
                  temp2=temp[j]
                  temp2=re.sub(r'\"', '',temp2)
                  temp2=re.sub("[\s\s]*",'',temp2)
                  temp2=re.sub("[\s\s]*",'',temp2)
                  # if(j==)
                  as_string=as_string+" , "+temp2
                  j=j+1
            else:
                  fl.write(as_string+"\n")
            i=i+1


      

def scrape_for_translations(lst,time):


      # bigTemp=open("bigTemp.txt",'a',encoding="utf8")
      # bigTemp=open("bigTemp.txt",'a',encoding="utf8")
      # bigTemp.truncate(0)
      name="Output_Lists/Ouput"+time
      output=open(name+".txt",'a',encoding="utf8")
      


      i=0
      while(i<len(lst)):
      # while(i<1):
            sub_lst=lst[i]
            english_item=sub_lst[0]

            # temp_file=open("temp.txt",'a',encoding="utf8")          
            temp_file=open("Scripts/temp.txt",'a',encoding="utf8")
            temp_file.truncate(0)
            # temp_file.write(english_item+"\n")
            # bigTemp.write(english_item+"\n")

            j=1
            while(j<len(sub_lst)):
                  npage=urlopen(sub_lst[j])
                  nhtml_bytes=npage.read()
                  nhtml=nhtml_bytes.decode("utf8")
                  x=re.split(r'\{\{trans-bottom\}\}',nhtml)
                  x=x[0]
                  x=re.split("===Translations===",x)
      
      
                  
                  temp_file.write(x[1])
                  # temp_file.close()
                  # bigTemp.write(x[1])
                  j=j+1
            else:
                  temp_file.close()
                  perl_out=open("perlOut.txt",'a',encoding='utf8')
                  perl_out.truncate(0)
                  perl_out.close()

                  # per_item_name="Output_Lists/"+english_item+time+".txt"
                  # per_item=open(per_item_name,'a',encoding='utf8')
                  # per_item.truncate(0)
                  
                  # subprocess.call(['perl','Scripts/clean_translation_tables.pl','Scripts/temp.txt',per_item_name])
                  subprocess.call(['perl','Scripts/clean_translation_tables.pl','Scripts/temp.txt',english_item])
                  file=open("perlOut.txt",'r+',encoding="utf8")
                  to_write=file.read()
                  # print(to_write)
                  output.write(to_write+"\n")
                  file.truncate(0)
                  file.close()
                  # per_item.close()

            i=i+1
      subprocess.call(['rm','perlOut.txt'])
      # subprocess.call([rm])
      output.close()
      print("Cleaning up the files and converting to .csv")
      final_clean("Output_Lists/Ouput"+time)




#Find the table of contents number...
def get_TOC(html,word):
      toc_level=re.findall(r'toclevel-([\d]+)',html)
      toc_section=re.findall(r' tocsection-([\d]+)',html)
      cat=re.findall(r'a href=\"\#([^\"]+)',html)

      #This will get you the section numbers
      secs=[]
      i=0
      while(i<len(toc_level)):
            ident=cat[i]
            if(bool(re.match("English|Translation",ident))):
                  if(bool(re.match("English",ident))):
                        i=i+1
                  else:
                        # secs.append(cat[i])
                        secs.append(toc_section[i])
            i=i+1

      #Let's go through and see if I can get the categories...
      # syntactic_categories=[]
      # i=0
      # while(i<len(cat)):
      #       itm=cat[i]
      #       if(bool(re.match("English|Alternative|Pronunciation|Etymology|Synonym|Antonym|Derived|Conjunction|Anagram|Pronoun|Noun|Verb|Adverb|Adjective|Particle|Article|Determiner|Numeral|Number",itm))):
      #             # i=i+1
      #             if("Conjunction|Pronoun|Noun|Verb|Adverb|Adjective|Particle|Article|Determiner|Numeral|Number",itm))):
      #                   syntactic_categories.append(itm)
      #                   i=i+1
      #                   print(itm)
      #             else:
      #                   break
      #       i=i+1
      # print(syntactic_categories)
      ## No, I could not figure out how to get this to work.

      i=0
      new_lst=[]
      new_lst.append(word)
      while(i<len(secs)):
            section=str(secs[i])
            nurl="https://en.wiktionary.org/w/index.php?title="+word+"&action=edit&section="+section
            new_lst.append(nurl)
            # secs.remove(secs[i])
            # secs.append(nurl)
            i=i+1
      # print(new_lst)


      return new_lst



def scrape_raw_page(lst,time):
      #Iterate through the list, then search each file, save that to temp.txt
     
      # bigFile=open("bigTemp.txt",'a',encoding="utf8")
      # bigFile.truncate(0)

      i=0
      new_lst=[]
      while(i<len(lst)):
      # while(i<7):
            sub_lst=lst[i]

            # file=open("tempRaw.txt",'a',encoding="utf8")
            # file.truncate(0)
            

            page=urlopen(sub_lst[1])
            html_bytes=page.read()
            html=html_bytes.decode("utf-8")
            
            # toc_level=re.findall(r'toclevel-([\d]+)',html)
            toc_urls=get_TOC(html,sub_lst[0])
            new_lst.append(toc_urls)

            i=i+1

      # print(new_lst)
      print("Scraping wiktionary for the url to the translation table")
      scrape_for_translations(new_lst,time)





#This function opens the list, and then checks to see if they are formatted properly.
def open_list(x):
      #Get the current time, to be suffixed to the filename
      d=datetime.datetime.utcnow()
      day_month="{:%h%d}".format(d)
      day_month=day_month+"-"
      hour_min="{:%H%M}".format(d)
      time_suffix=day_month+hour_min
      
      fl=open("./Input_Lists/"+x,'r',encoding="utf8")
      x=fl.read()#Read in the CSV file as a string
      fl.close()
      x=re.split("\n",x)

      i=0
      lst_as_array=[]
      while(i<len(x)):
            curr=x[i]
            curr=re.split(",",curr)
            if(curr[0]==''):
                  pass
            elif(len(curr)==1):
                  curr.append("https://en.wikipedia.org/wiki/"+curr[0]+"#English")
                  lst_as_array.append(curr)
            elif(len(curr)>1):
                  url=curr[1]
                  if(url[-8]!="#English"):
                        curr.pop()
                        url=url+"#English"
                        curr.append(url)
                  lst_as_array.append(curr)
            i=i+1
      print(("-"*76)+"\nScraping pages ...")
      # print(lst_as_array)
      scrape_raw_page(lst_as_array,time_suffix)


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

def start(logo, version):
      print(logo+"\n"+"wiktioNear_"+version+"\nA program written by Ian L. Kirby (ianlkirby@vivaldi.net) for extracting wordlists from wiktionary.org.\n"+("#"*76)+"\n")
      if (not(len(sys.argv)>1)):
            print("You did not enter a file.  I will check in the \"Input_Lists\" directory...\nType the number of the file for your wordlists.")
            lst=check_list_dir()
      else:
            lst=sys.argv[1]
      open_list(lst)


dir=os.listdir('.')
has_output=False
i=0
while(i<len(dir)):
      if(dir[i]=="Output_Lists"):
            has_output=True
            break
      i=i+1
if(has_output==False):
      subprocess.call(['mkdir','Output_Lists'])

version="v1.2.1"
logo="""
           iii kk     tt    iii        NN   NN                       
ww      ww     kk  kk tt         oooo  NNN  NN   eee    aa aa rr rr  
ww      ww iii kkkkk  tttt  iii oo  oo NN N NN ee   e  aa aaa rrr  r 
 ww ww ww  iii kk kk  tt    iii oo  oo NN  NNN eeeee  aa  aaa rr     
  ww  ww   iii kk  kk  tttt iii  oooo  NN   NN  eeeee  aaa aa rr     
                                                                     
"""
t0=time.time()
start(logo,version)
t1=time.time()
print("Time elapsed: "+str(t1-t0))

There once was a a man from nantucket