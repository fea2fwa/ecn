from urllib.request import urlopen
from bs4 import BeautifulSoup

output=open("output.txt", "w+", encoding="UTF-8")

def getThreadtitle(threadId):
 try:
  html=urlopen("https://community.emc.com/thread/"+str(threadId))
 except:
  print("Thread#"+str(threadId)+"is invalid for ECN title scraping.")
 else:
  bsObj=BeautifulSoup(html)
  title=bsObj.title.get_text()
  title=title.strip("EMC Community Network - ECN")
  title=title.strip(": ")
  print(title+"\n")
  output.write(title+"\n")

def getThreadtext(threadId):
 try:
  html=urlopen("https://community.emc.com/thread/"+str(threadId))
 except:
  print("Thread#"+str(threadId)+"is invalid for ECN thread-text scraping.")
 else: 
  bsObj=BeautifulSoup(html)
  bodylist=bsObj.findAll("div", {"class":"jive-rendered-content"})
  for body in bodylist: 
   print(body.get_text()+"\n")
   output.write(body.get_text()+"\n")

file=open('thread.txt', 'r', encoding="UTF-8")

for line in file:
 line = line.rstrip()
 getThreadtitle(line)
 getThreadtext(line)

file.close()
output.close()


