from urllib.request import urlopen
import csv, re, datetime, sys



#Function to scrape the relevant pages.
def wikiScrape(name,url):

    page=urlopen(url)
    html_bytes=page.read()
    html=html_bytes.decode("utf-8")
    out_name="./FilesOut/"+name+".txt"
    
    fl_out=open(out_name,"w",encoding="utf-8")
    fl_out.write(html)
    fl_out.close()





#Verify that there is a command line argument.  Close if there is not.
if (len(sys.argv)<2):
    sys.exit("Please provide command line argument.")

#Later on, once there are more options in the scripts, I will need to verify that more precisely that there is a .csv argument.

fl_in=open(str(sys.argv[1]),"r",encoding="utf8")
lst_in=fl_in.read()
fl_in.close()



lst_in=re.split("\n",lst_in)
i=0
new_lst=[]
while (i<len(lst_in)):
    x=lst_in[i]
    x=re.split(', ',x)  
    new_lst.append(x)
    i=i+1

#get the utc time that it will be retrieved.
d=datetime.datetime.utcnow()
day_month="{:%h%d}".format(d)
day_month=day_month+"-"
hour_min="{:%H%M}".format(d)
day_month=day_month+hour_min

i=0
while (i<len(new_lst)):
    temp=new_lst[i]
    #label for the page, with the UTC time appended for file name
    label_assigned=temp[0]+"-"+day_month
    url_to_fetch=temp[1]
    if (url_to_fetch[-6:]!="nglish"):
        url_to_fetch=url_to_fetch+"#English"
    wikiScrape(label_assigned,url_to_fetch)
    i=i+1
