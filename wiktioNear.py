from urllib.request import urlopen
import csv, re, datetime, sys, subprocess, os

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
day_month_hour_min=day_month+hour_min

out_csv=""

i=0
print("Scraping pages...")
while (i<len(new_lst)):
    temp=new_lst[i]
    #label for the page, with the UTC time appended for file name
    label_assigned=temp[0]+"-"+day_month_hour_min
    url_to_fetch=temp[1]
    if (url_to_fetch[-6:]!="nglish"): #Verifying that it ends with #English
        url_to_fetch=url_to_fetch+"#English"
    # out_csv=temp[0]+","+url_to_fetch+","+temp[1]+"\n"
    subprocess.call(['python','./Scripts/findTOC2.py',url_to_fetch,temp[0],label_assigned])
    i=i+1
# else:
    # print("Making a record in file \"record\"")

# print("Cleaning tables...")
# dir=os.listdir('./FilesOut')
# print(dir)
print("Cleaning the files")
dir=os.listdir('.')
i=0
while(i<len(dir)):
    curr=dir[i]
    if(curr[-4:]==".txt"):
        subprocess.call(['perl','cleaner.pl',curr])
    i=i+1

print("Moving the files")
subprocess.call(['sh','toCSV.sh'])

print("Done!")

# test="./too-Apr20-0025.txt"
# subprocess.call(['perl','./Scripts/cleaner.pl',test])
