from IPython.display import clear_output
class drivers():
    def __init__(self,tag):
        self.tag=tag
        self.driventime=0
        self.drivendistance=0
        self.pos='A'
        self.status=0
        self.earnings=0
    
    def updatestatus(self,a,b,c):
        temp=abs(ord(b)-ord(a))
        self.driventime+=temp
        self.drivendistance+=15*temp
        self.pos=b
        self.status=c+temp
        self.earnings+=(100 if temp<5 else 100+(temp-5)*10)
    
    def printing(self):
        print("driver id",self.tag,"   Driven Time:",self.driventime,"   Driven Distance:",self.drivendistance,"  Earnings:",self.earnings)
    
    def posreturn(temp):
        return [temp.pos,temp.earning]

class trip():
    def __init__(self,a,b,c,d):
        temp=abs(ord(b)-ord(a))
        self.taxi=d
        self.start=a
        self.destination=b
        self.starttime=c
        self.endtime=c+temp
        self.fare=(100 if temp<5 else 100+(temp-5)*10)
    
    def printing(self):
        print(self.taxi,self.start,self.destination,self.starttime,self.endtime,self.fare)

choice=6 #this is for dummy to enter into the loop
taxilist=[]
triplist=[]
while choice!=5:
    choice=int(input("1:Add taxi\n2:Booking\n3:History\n4:Driver Details\n5:Exit"))
    clear_output(wait=False)
    if choice==1:
        taxilist.append(drivers(len(taxilist)+1))
        print("Taxi",len(taxilist),"Added")
    
    if choice==2:
        a,b,c=input("Enter pickup and Drop locations with Time of Pickup").split()
        taxilocations=[]
        for i in taxilist:
            if i.status<=int(c):
                taxilocations.append([abs(ord(a)-ord(i.pos)),i.earning,i.tag,i])
        taxilocations.sort()
        if len(taxilocations)==0:
            print("No Taxi is available at this moment Try changing the Time of Pickup")
        else:
            print("Taxi",taxilocations[0][3].tag,"is coming to Pickup You")
            taxilocations[0][3].updatestatus(a,b,int(c))
            triplist.append(trip(a,b,int(c),taxilocations[0][3].tag))

    if choice==3:
        for trip in triplist:
            trip.printing() 

    if choice==4:
        for taxi in taxilist:
            taxi.printing()                              

