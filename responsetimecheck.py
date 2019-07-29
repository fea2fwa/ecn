import datetime

while True:

 starttime=input("Enter the question time: ")
 replytime=input("Enter the reply time: ")

 starttime=starttime.split()
 replytime=replytime.split()

 sdate=starttime[0]
 stime=starttime[1]

 sdate=sdate.split("/")
 stime=stime.split(":")

 sy=int(sdate[0])
 sm=int(sdate[1])
 sd=int(sdate[2])

 sh=int(stime[0])
 smm=int(stime[1])

 rdate=replytime[0]
 rtime=replytime[1]

 rdate=rdate.split("/")
 rtime=rtime.split(":")

 ry=int(rdate[0])
 rm=int(rdate[1])
 rd=int(rdate[2])

 rh=int(rtime[0])
 rmm=int(rtime[1])


 a=datetime.datetime(sy,sm,sd,sh,smm,0)
 b=datetime.datetime(ry,rm,rd,rh,rmm,0)
 c=b-a
 d=(c.days*86400+c.seconds)/60
 print(d)


