from urllib.request import urlopen
from bs4 import BeautifulSoup

csvoutput=open("csvEcnJapanese.csv", "w+", encoding="UTF-8")
output=open("ecnJapanese.txt", "w+", encoding="UTF-8")

def getEcnstats(threadId):
 html=urlopen("https://community.emc.com/thread/"+str(threadId))
 bsObj=BeautifulSoup(html)
 title=bsObj.title.get_text()
 title=title.strip("EMC Community Network - DECN")
 title=title.strip(": ")
 questioner=bsObj.find("a", {"class":"jiveTT-hover-user jive-username-link"})
 questioner=questioner.get_text()
 qpostedtime=bsObj.find("span", {"class":"j-post-author"})
 qpostedtime=qpostedtime.get_text()
 textlist=qpostedtime.split(" ")
 time=textlist[4].split(":")
 hour=time[0]
 minute=time[1]
 hour=int(hour)
 summertime=1
 if textlist[5].count("AM") and hour != 12:
  hour=hour+17-summertime
 else:
  hour=hour+5-summertime
 if hour > 24:
  hour=hour-24-summertime
 print(title+"\n")
 output.write(title+"\n")
 csvoutput.write(str(threadId)+","+ title+","+questioner+","+str(hour)+":"+str(minute)+"\n")

def getThreadtext(threadId):
 html=urlopen("https://community.emc.com/thread/"+str(threadId))
 bsObj=BeautifulSoup(html)
 bodylist=bsObj.findAll("div", {"class":"jive-rendered-content"})
 for body in bodylist: 
  print(body.get_text()+"\n")
  output.write(body.get_text()+"\n")


startId=input("Enter the first thread# which in the Japanese forum site: ")
endId=input("Enter the last thread# which in the Japaneese forum site: ")
endId=int(endId)+1

for i in range(int(startId), int(endId)):
 try:
  htmltemp=urlopen("https://community.emc.com/thread/"+str(i))
 except:
  print("Thread#"+str(i)+" has been deleted or is an invalid or private thread.")
 else:
  bsObjTemp=BeautifulSoup(htmltemp)
  templist=bsObjTemp.findAll("script", {"type":"text/javascript"})
  templist=str(templist)
  if "communityID = '2814';" in templist:
   getEcnstats(i)
   getThreadtext(i)
  elif "communityID = '3093';" in templist:
   getEcnstats(i)
   getThreadtext(i)
  elif "communityID = '3094';" in templist:
   getEcnstats(i)
   getThreadtext(i)
  elif "communityID = '3095';" in templist:
   getEcnstats(i)
   getThreadtext(i)
  elif "communityID = '3096';" in templist:
   getEcnstats(i)
   getThreadtext(i)

csvoutput.close()
output.close()


