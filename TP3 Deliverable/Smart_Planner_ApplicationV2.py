import math, copy, random
import tkinter

from cmu_112_graphics import *
from datetime import date

def appStarted(app):
    app.borderWidth=app.width/10
    app.borderHeight=app.height/10
    app.startTime=9

    app.eventDict={}

    app.buttonList=[]
    app.deleteButton=Button(app,"Delete","Delete","red",7,1,None)
    app.buttonList.append(app.deleteButton)

    app.createEventButton=Button(app,"createEvent","createEvent","light green",7,2,"createEventTextBox")
    app.buttonList.append(app.createEventButton)

    app.editEventButton=Button(app,"editEvent","editEvent","yellow",7,3,None)
    app.buttonList.append(app.editEventButton)

    app.createEventTextBox=TextBox(app,"createEventTextBox",["What time does your event start? (ex:9:16)","What time does your event end? (ex:9:16)","What day is your event on?","What is the name of the event?","Event Description:"])

    app.textBoxDict=dict()
    app.textBoxDict["createEventTextBox"]=app.createEventTextBox

    app.editEventTextBox=TextBox(app,"editEventTextBox",["What time does your event start? (ex:9:16)","What time does your event end? (ex:9:16)","What day is your event on?","What is the name of the event?","Event Description:"])
    app.textBoxDict["editEventTextBox"]=app.editEventTextBox

    app.clickedDeleteEvent=False
    app.clickedEditEvent=False

    app.eventToEdit=None

    #https://docs.python.org/3/library/datetime.html
    app.currentDateString=str(date.today())
    #2022-12-05

    app.days=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    app.dayOfTheWeekInt=(int(datetime.datetime.today().weekday())+1)
    app.dayOfTheWeek=app.days[app.dayOfTheWeekInt]

    app.currentYear=int(app.currentDateString[0:4])
    app.currentDay=int(app.currentDateString[8::])


    app.febNumDays=0
    if (app.currentYear%4==0) and (app.currentYear%100!=0):
        app.febNumDays=29
    elif (app.currentYear%400==0):
        app.febNumDays=29
    else: 
        app.febNumDays=28

    app.months=[["January",31],["Febuary",app.febNumDays],["March",31],["April",30],["May",31],["June",30],["July",31],
            ["August",31],["September",30],["October",31],["November",30],["December",31]]
    app.monthIndex=int(app.currentDateString[5:7])-1
    app.currentMonth=app.months[app.monthIndex][0]

    
def convertTime(app,timeString):
    hour,minute=timeString.split(":")
    hour=float(hour)
    if (hour-9>=0):
        hour=hour-app.startTime
    else:
        hour=hour+(12-app.startTime)
    return hour+(float(minute)/60)

def convertDayOfTheWeek(date):
    if date=="Sunday":return 0
    elif date=="Monday":return 1
    elif date=="Tuesday":return 2
    elif date=="Wednesday":return 3
    elif date=="Thursday":return 4
    elif date=="Friday":return 5
    elif date=="Saturday":return 6
    else: return 0

def mousePressed(app,event):
    app.borderWidth=app.width/10
    app.borderHeight=app.height/10

    dict_copy = app.eventDict.copy()

    for key in dict_copy:
        dict_copy[key].mousePressed(app,event)

    for button in app.buttonList:
        button.mousePressed(app,event)


    for (textBoxName,textBox) in app.textBoxDict.items():
        textBox.mousePressed(app,event)
        textBox.closeButton.mousePressed(app,event)
        textBox.enterButton.mousePressed(app,event)
    



def keyPressed(app,event):
    for (textBoxName,textBox) in app.textBoxDict.items():
        textBox.keyPressed(app,event)
    

def drawWeekCalendarTime(app,canvas):
    for i in range(12):
        timeSuffix=""
        if app.startTime+i>=12:
            timeSuffix="pm"
        else:
            timeSuffix="am"
        timeToWrite=(app.startTime+i)%12
        if timeToWrite==0:
            timeToWrite=12
        canvas.create_text(app.borderWidth/2,app.borderHeight+((app.height-app.borderHeight*2)/12)*i,
        text=str(timeToWrite)+" "+timeSuffix,fill="black")

def drawWeekCalendarDate(app,canvas):
    daysOfTheWeek=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    for i in range(7):
        canvas.create_text(app.borderWidth+((app.width-app.borderWidth*2)/7)*((2*i+1)/2),
        app.borderHeight/2,text=daysOfTheWeek[i],fill="black")

                

def drawWeekCalendarOutline(app,canvas):
    canvas.create_rectangle(0+app.borderWidth,0+app.borderHeight,app.width-app.borderWidth,
    app.height-app.borderHeight,fill="light blue")
    for i in range(7):
        canvas.create_rectangle(app.borderWidth+((app.width-app.borderWidth*2)/7)*i,
        0+app.borderHeight,app.borderWidth+((app.width-app.borderWidth*2)/7)*(i+1),
        app.height-app.borderHeight)
    for i in range (12):
        canvas.create_rectangle(0+app.borderWidth,app.borderHeight+((app.height-app.borderHeight*2)/12)*i,
         app.width-app.borderWidth,
         app.borderHeight+((app.height-app.borderHeight*2)/12)*(i+1))
    
def drawEvents(app,canvas):
    dict_copy = app.eventDict.copy()
    for key in dict_copy:
        dict_copy[key].drawEvent(app,canvas)

def drawButtons(app,canvas):
    for i in range (len(app.buttonList)):
        app.buttonList[i].drawButton(app,canvas)

def drawTextBoxes(app,canvas):
    for (textBoxName,textBox) in (app.textBoxDict.items()):
        textBox.drawTextBox(app,canvas)
    
def redrawAll(app,canvas):
    drawWeekCalendarOutline(app,canvas)
    drawWeekCalendarTime(app,canvas)
    drawWeekCalendarDate(app,canvas)
    drawEvents(app,canvas)
    drawButtons(app,canvas)
    drawTextBoxes(app,canvas)

#These are some helper functions to help us draw date

def determineWidthFromDate(date):
    if date=="Sunday":
        return 0
    elif date=="Monday":
        return 1
    elif date=="Tuesday":
        return 2
    elif date=="Wednesday":
        return 3
    elif date=="Thursday":
        return 4
    elif date=="Friday":
        return 5
    elif date=="Saturday":
        return 6
    else: 
        return 0

def adjustDate(app,dayInt):
    numDaysCurrMonth=app.months[(app.monthIndex)][1]
    if (dayInt<=0):
        numDaysPrevMonth=app.months[(app.monthIndex-1)%12][1]
        howMuchToSubtract=abs(dayInt)
        newDay=numDaysPrevMonth-howMuchToSubtract
        return newDay
    
    elif (dayInt>numDaysCurrMonth):
        #This could potentially need work
        return dayInt-numDaysCurrMonth
    else:
        return dayInt
        
    
class Event:
    def __init__(self,app,name,eventType,description,date,startTime,endTime,color):
        self.name=name
        self.eventType=eventType
        self.description=description
        self.date=date
        self.startTime=startTime
        self.endTime=endTime
        self.color=color

        self.clickedEventDescription=False

        self.day=adjustDate(app,app.currentDay+convertDayOfTheWeek(date)-convertDayOfTheWeek(app.dayOfTheWeek))
        self.month=""
        if (app.currentDay+convertDayOfTheWeek(date)-convertDayOfTheWeek(app.dayOfTheWeek)<=0):
            self.month=app.months[(app.monthIndex-1)%12][0]
        elif(app.currentDay+convertDayOfTheWeek(date)-convertDayOfTheWeek(app.dayOfTheWeek)>app.months[(app.monthIndex)][1]):
            self.month=app.months[(app.monthIndex+1)%12][0]
        else: self.month=app.currentMonth

        self.year=0
        if (app.currentMonth=="January") and (app.currentDay+convertDayOfTheWeek(date)-convertDayOfTheWeek(app.dayOfTheWeek)<=0):
            self.year=app.currentYear-1
        else:
            self.year=app.currentYear

        


    def mousePressed(self,app,event):
        startXCord=app.borderWidth+((app.width-app.borderWidth*2)/7)*determineWidthFromDate(self.date)
        endXCord=app.borderWidth+((app.width-app.borderWidth*2)/7)*(determineWidthFromDate(self.date)+1)
        startYCord=app.borderHeight+((app.height-app.borderHeight*2)/12)*(self.startTime)
        endYCord=app.borderHeight+((app.height-app.borderHeight*2)/12)*(self.endTime)
        if (event.x>=startXCord) and (event.y
                >=startYCord) and (event.x<=endXCord) and (event.y<=endYCord):
            if (app.clickedDeleteEvent==True):
                app.eventDict.pop(self.name)
                app.clickedDeleteEvent=False
            elif (app.clickedEditEvent==True):
                app.editEventTextBox.clicked=True
                app.eventToEdit=self
                app.clickedEditEvent=False
            else:
                if (self.clickedEventDescription==False):
                    self.clickedEventDescription=True
                else:
                    self.clickedEventDescription=False


                
            
                
    def drawEvent(self,app,canvas):
        
        startXCord=app.borderWidth+((app.width-app.borderWidth*2)/7)*determineWidthFromDate(self.date)
        endXCord=app.borderWidth+((app.width-app.borderWidth*2)/7)*(determineWidthFromDate(self.date)+1)
        startYCord=app.borderHeight+((app.height-app.borderHeight*2)/12)*(self.startTime)
        endYCord=app.borderHeight+((app.height-app.borderHeight*2)/12)*(self.endTime)
        if (app.clickedDeleteEvent==False) and (app.clickedEditEvent==False):
            canvas.create_rectangle(startXCord,startYCord,endXCord,endYCord,
            fill=self.color)
        else:
            canvas.create_rectangle(startXCord,startYCord,endXCord,endYCord,
            fill=self.color,outline="red")
        
        canvas.create_text((endXCord+startXCord)/2,(endYCord+startYCord)/2,
                           text=self.name,fill="black")

        if (self.clickedEventDescription==True):
            canvas.create_rectangle(0.25*app.width,0.25*app.height,0.75*app.width,0.75*app.height,
                 fill="light yellow"                   )
            canvas.create_text(0.5*app.width,0.5*app.height,text=self.description,fill="black")
        
        
class Button:
    def __init__(self,app,name,buttonType,color,xPos,yPos,textBoxName):
        self.name=name
        self.buttonType=buttonType
        self.color=color
        self.buttonWidth=50
        self.buttonHeight=25
        self.xPos=xPos
        self.yPos=yPos
        self.textBoxName=textBoxName


    def mousePressed(self,app,event):
        x0=app.borderWidth+(self.xPos*((app.width-2*app.borderWidth)/7))
        y0=app.borderHeight+(self.yPos*((app.height-2*app.borderHeight)/12))
        x1=app.borderWidth+((self.xPos+1)*((app.width-2*app.borderWidth)/7))
        y1=app.borderHeight+((self.yPos+1)*((app.height-2*app.borderHeight)/12))
        if (event.x>=x0) and (
            event.y>=y0) and (
                event.x<=x1) and (
                    event.y<=y1):
            if (self.textBoxName!=None) and (self.buttonType!="closeTextBox") and (self.buttonType!="enterTextBox"):
                app.textBoxDict[self.textBoxName].clicked=True
            else: 
                pass
                
            if (self.buttonType=="Delete"):
                if (len(app.eventDict)!=0):
                    app.clickedDeleteEvent=True
            elif (self.buttonType=="closeTextBox"):
                app.textBoxDict[self.textBoxName].clicked=False
            elif (self.buttonType=="enterTextBox"):
                app.textBoxDict[self.textBoxName].processTextBoxAnswers(app)
                app.textBoxDict[self.textBoxName].clicked=False
 
            elif (self.buttonType=="editEvent"):
                if (len(app.eventDict)!=0):
                    app.clickedEditEvent=True 
                
            else: pass

            
            
    



    def drawButton(self,app,canvas):
        canvas.create_rectangle(app.borderWidth+(self.xPos*((app.width-2*app.borderWidth)/7)),
                                app.borderHeight+(self.yPos*((app.height-2*app.borderHeight)/12)),
                                app.borderWidth+((self.xPos+1)*((app.width-2*app.borderWidth)/7)),
                                app.borderHeight+((self.yPos+1)*((app.height-2*app.borderHeight)/12)),
                                fill=self.color)
    
        textX=((app.borderWidth+(self.xPos*((app.width-2*app.borderWidth)/7)))+(app.borderWidth+((self.xPos+1)*((app.width-2*app.borderWidth)/7))))/2
        textY=((app.borderHeight+(self.yPos*((app.height-2*app.borderHeight)/12)))+(app.borderHeight+((self.yPos+1)*((app.height-2*app.borderHeight)/12))))/2
        canvas.create_text(textX,
                            textY,text=self.name,fill="black")

class TextBox:
    def __init__(self,app,name,questions):
        self.name=name
        self.questions=questions
        self.boxCurrentlyTyping=0
        self.answers=[ ""  for i in range(len(self.questions))]
        self.clicked=False
        #(self,app,name,buttonType,color,xPos,yPos,textBoxName)
        self.closeButton=Button(app,"close","closeTextBox","red",2,9.75,name)
        self.enterButton=Button(app,"enter","enterTextBox","light green",4,9.75,name)



    def mousePressed(self,app,event):
        if (event.x>=0.25*app.width) and (
            event.y>=0.25*app.height) and (
                event.x<=0.75*app.width) and (
                    event.y<=0.75*app.height):
            if (self.clicked):
                for i in range(len(self.questions)*2):
                    y0=0.25*app.height+((i/10)*0.5*app.height)
                    y1=0.25*app.height+(((i+1)/10)*0.5*app.height)
                    x0=0.25*app.width
                    x1=0.75*app.width
                    if (event.x>=x0) and (event.y>=y0) and (event.x<=x1) and (event.y<=y1):
                        if (i%2==1):
                            self.boxCurrentlyTyping=i/2

    def keyPressed(self,app,event):
        if (self.clicked==True):
            i=(int) (self.boxCurrentlyTyping)
            y0=0.25*app.height+((i/10)*0.5*app.height)
            y1=0.25*app.height+(((i+1)/10)*0.5*app.height)
            x0=0.25*app.width
            x1=0.75*app.width
            
            
            if (event.key=="Space"):
                    self.answers[i]+=" "
            elif (event.key=="BackSpace"):
                    length=len(self.answers[i])
                    self.answers[i]=self.answers[i][0:length-1]
            elif (event.key=="Return"):
                    self.answers[i]+="\n"
            elif (ord(event.key)>=33) and (ord(event.key)<=126):
                    self.answers[i]+=str(event.key)

    

    def drawTextBox(self,app,canvas):
        if (self.clicked==True):
            canvas.create_rectangle(0.25*app.width,0.25*app.height,
                                    0.75*app.width,0.75*app.height,
                                    fill="light yellow")
            #5 questions max
            for i in range(len(self.questions)*2):
                y0=0.25*app.height+((i/10)*0.5*app.height)
                y1=0.25*app.height+(((i+1)/10)*0.5*app.height)
                x0=0.25*app.width
                x1=0.75*app.width
                canvas.create_rectangle(x0,y0,x1,y1,outline="black")
                if (i%2==0):
                    listIndex=(int)(i/2)
                    canvas.create_text((x0+x1)/2,(y0+y1)/2,text=self.questions[listIndex],
                                       fill="black")
                if (i%2==1):
                    listIndex=(int)(i/2)
                    canvas.create_text((x0+x1)/2,(y0+y1)/2,text=self.answers[listIndex],
                                       fill="black")
            self.closeButton.drawButton(app,canvas)
            self.enterButton.drawButton(app,canvas)

    def processTextBoxAnswers(self,app):
        if (self.name=="createEventTextBox") and (app.createEventTextBox.clicked==True):
            time1=convertTime(app,self.answers[0])
            time2=convertTime(app,self.answers[1])
            date=self.answers[2]
            name=self.answers[3]
            description=self.answers[4]
            #(self,app,name,eventType,description,date,startTime,endTime,color)
            newEvent=Event(app,name,"newEvent",description,date,time1,time2,"light green")
            app.eventDict[name]=newEvent
            for i in range(len(self.answers)):
                        self.answers[i]=""

        elif (self.name=="editEventTextBox") and (app.editEventTextBox.clicked==True):
            newTime1=convertTime(app,self.answers[0])
            newTime2=convertTime(app,self.answers[1])
            newDate=self.answers[2]
            newName=self.answers[3]
            newDescription=self.answers[4]
            if (app.eventToEdit!=None):
                app.eventDict[newName] = app.eventDict.pop(app.eventToEdit.name)
                app.eventToEdit.name=newName
                app.eventToEdit.startTime=newTime1
                app.eventToEdit.endTime=newTime2
                app.eventToEdit.date=newDate
                app.eventToEdit.description=newDescription


            app.eventToEdit=None
            for i in range(len(self.answers)):
                        self.answers[i]=""
   

runApp(width=1000,height=600)