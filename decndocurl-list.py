from urllib.request import urlopen
from bs4 import BeautifulSoup

csvoutput=open("decnjpdoclist.csv", "w+", encoding="UTF-8")

def getEcnstats(threadId, spaceId):
 html=urlopen("https://community.emc.com/docs/DOC-"+str(threadId))
 bsObj=BeautifulSoup(html)
 title=bsObj.title.get_text()
 title=title.strip("EMC Community Network - DECN")
 title=title.strip(": ")
 bodytext=bsObj.find("div", {"class":"jive-rendered-content"})
 bodytext=bodytext.get_text()

 csvoutput.write("https://community.emc.com/docs/DOC-"+str(threadId)+","+ title+","+bodytext+","+str(spaceId)+"\n")


startId=input("Enter the first doc# which in the Japanese forum site: ")
endId=input("Enter the last doc# which in the Japaneese forum site: ")
endId=int(endId)+1

for i in range(int(startId), int(endId)):
 try:
  htmltemp=urlopen("https://community.emc.com/docs/DOC-"+str(i))
 except:
  print("Doc#"+str(i)+" has been deleted or is an invalid or private doc.")
 else:
  bsObjTemp=BeautifulSoup(htmltemp)
  templist=bsObjTemp.findAll("script", {"type":"text/javascript"})
  templist=str(templist)
  if "communityID = '2814';" in templist:
   getEcnstats(i, 2814)
  elif "communityID = '3093';" in templist:
   getEcnstats(i, 3093)
  elif "communityID = '3094';" in templist:
   getEcnstats(i, 3094)
  elif "communityID = '3095';" in templist:
   getEcnstats(i, 3095)
  elif "communityID = '3096';" in templist:
   getEcnstats(i, 3096)
  elif "communityID = '3504';" in templist:  #GURU
   getEcnstats(i, 3504)
  elif "communityID = '3221';" in templist:  #NECPlus
   getEcnstats(i, 3221)
  elif "communityID = '3696';" in templist:  #PEPortal
   getEcnstats(i, 3696)
  elif "communityID = '3606';" in templist:  #NetworldPlus
   getEcnstats(i, 3606)
  elif "communityID = '3210';" in templist:  #BPP_Kuroki-san
   getEcnstats(i, 3210)
  


csvoutput.close()



