from urllib.request import urlopen
from bs4 import BeautifulSoup

output=open("output-space_text.txt", "w+", encoding="UTF-8")

def getThreadtitle(threadId):
 html=urlopen("https://community.emc.com/thread/"+str(threadId))
 bsObj=BeautifulSoup(html)
 title=bsObj.title.get_text()
 title=title.strip("EMC Community Network - ECN: ")
 print(title+"\n")
 output.write(title+"\n")

def getThreadtext(threadId):
 html=urlopen("https://community.emc.com/thread/"+str(threadId))
 bsObj=BeautifulSoup(html)
 bodylist=bsObj.findAll("div", {"class":"jive-rendered-content"})
 for body in bodylist: 
  print(body.get_text()+"\n")
  output.write(body.get_text()+"\n")

startId=input("Enter the first thread#: ")
endId=input("Enter the last thread#: ")
spaceId=input("Enter the space# from which we crawl the text data: ")

for i in range(int(startId), int(endId)):
 try:
  htmltemp=urlopen("https://community.emc.com/thread/"+str(i))
 except:
  print("Thread#"+str(i)+" has been deleted or is an invalid or private thread.")
 else:
  bsObjTemp=BeautifulSoup(htmltemp)
  templist=bsObjTemp.findAll("script", {"type":"text/javascript"})
  templist=str(templist)
  judge=("communityID = '"+spaceId+"';" in templist)
  if judge == True: 
   getThreadtitle(i)
   getThreadtext(i)

output.close()


