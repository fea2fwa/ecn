import re
import collections
from html import unescape
from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

startId=input("Enter the first thread#: ")
endId=input("Enter the last thread#: ")

communityidaccum=[]

f=open("questionNum.txt", "w+", encoding="UTF-8")

for i in range(int(startId), int(endId)+1):
    try:
        htmltemp=urlopen("https://community.emc.com/thread/"+str(i))
    except:
        print("Thread#"+str(i)+" has been deleted or is an invalid or private thread.")
    else:
        bsObjTemp=BeautifulSoup(htmltemp)
        templist=bsObjTemp.findAll("script", {"type":"text/javascript"})
        templist=str(templist)
        communityid=re.findall(r"communityID = '[0-9][0-9][0-9][0-9]'",templist)
        communityid=re.findall(r"[0-9][0-9][0-9][0-9]",str(communityid))
        communityidaccum=communityidaccum+communityid

count_dict=collections.Counter(communityidaccum)

for k,v in count_dict.most_common():
    f.write("{};{}\n".format(k,v))

f.close()


