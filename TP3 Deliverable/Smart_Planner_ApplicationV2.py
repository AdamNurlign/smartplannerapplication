import math, copy, random
import tkinter

from cmu_112_graphics import *
import datetime

def appStarted(app):
    app.calendarMode="Home"
    app.borderWidth=app.width/10
    app.borderHeight=app.height/10
    app.startTime=9
    app.endTime=21


    app.eventDict={}

    app.buttonList=[]
    app.deleteButton=Button(app,"Delete","Delete","red",7,1,None)
    app.buttonList.append(app.deleteButton)

    app.createEventButton=Button(app,"createEvent","createEvent","light green",7,2,"createEventTextBox")
    app.buttonList.append(app.createEventButton)

    app.editEventButton=Button(app,"editEvent","editEvent","yellow",7,3,None)
    app.buttonList.append(app.editEventButton)

    app.nextWeekButton=Button(app,"nextWeek","nextWeek","light blue",7,4,None)
    app.prevWeekButton=Button(app,"prevWeek","prevWeek","pink",7,5,None)
    app.buttonList.append(app.nextWeekButton)
    app.buttonList.append(app.prevWeekButton)

    app.nextDayButton=Button(app,"nextDay","nextDay","light coral",7,6,None)
    app.prevDayButton=Button(app,"prevDay","prevDay","dark slate gray",7,7,None)
    app.switchModeButton=Button(app,"switchMode","switchMode","gray",7,8,None)

    app.buttonList.append(app.nextDayButton)
    app.buttonList.append(app.prevDayButton)
    app.buttonList.append(app.switchModeButton)


    
    app.changeSettingsTextBox=TextBox(app,"changeSettingsTextBox",["What is the earliest time you would like to work? (ex: '8 am')","How long would you like your breaks? (min)","Max # of events per day: "])
    app.changeSettingsButton=Button(app,"changeSettings","changeSettings","pink",2.5,11,"changeSettingsTextBox")
    
    
    app.startApplicationButton=Button(app,"start","start","light green",3.5,11,None)



    app.createEventTextBox=TextBox(app,"createEventTextBox",["What time does your event start? (ex:9:16)","What time does your event end? (ex:9:16)","What day is your event on?","What is the name of the event?","Event Description:"])

   
   
    app.textBoxDict=dict()
    app.textBoxDict["createEventTextBox"]=app.createEventTextBox
 
    app.editEventTextBox=TextBox(app,"editEventTextBox",["What time does your event start? (ex:9:16)","What time does your event end? (ex:9:16)","What day is your event on?","What is the name of the event?","Event Description:"])
    app.textBoxDict["editEventTextBox"]=app.editEventTextBox

    app.textBoxDict["changeSettingsTextBox"]=app.changeSettingsTextBox

    app.autoScheduleTextBox=TextBox(app,"autoScheduleTextBox",["Between what days would you like this event to occur (ex: 11/2/2004 to 11/18/2004 )","What days of the week would you like this event to occur on? (ex: 'Sunday,Monday,Tuesday,Friday')","Max instances per day","Number of instances:", "Event length (hrs):"])
    app.textBoxDict["autoScheduleTextBox"]=app.autoScheduleTextBox


    app.autoScheduleButton=Button(app,"autoSchedule","autoSchedule","blue",7,10,"autoScheduleTextBox")
    app.buttonList.append(app.autoScheduleButton)


    app.jumpToTextBox=TextBox(app,"jumpToTextBox",["What day would you like to jump to? (MM/DD/YYYY)"])
    app.textBoxDict["jumpToTextBox"]=app.jumpToTextBox

    
    app.jumpToButton=Button(app,"jumpTo","jumpTo","white",7,9,"jumpToTextBox")
    app.buttonList.append(app.jumpToButton)

    app.homeButton=Button(app,"home","home","light pink",7,-1.5,None)
    app.buttonList.append(app.homeButton)

    
    
    app.clickedDeleteEvent=False
    app.clickedEditEvent=False

    #Access to the current date
    app.today = datetime.date.today()

    #Access to the current day of the week
    app.currentWeekDay = app.today.weekday()

    #Access to the day of the current Sunday and Saturday
    app.sunday = app.today - datetime.timedelta(days=(app.currentWeekDay + 1)%7)
    app.saturday = app.sunday + datetime.timedelta(days=6)

    app.breakLength=0

    app.numEventsPerDay=100000000


    app.eventToEdit=None

    app.messagePopUpDict=dict()

    app.failAutoSchedulePopUp=MessagePopUp(app,"failAutoSchedule","Failed to schedule events due to your settings and planned events. Please try again.")


    
    app.messagePopUpDict["failAutoSchedule"]=app.failAutoSchedulePopUp


    
    
def convertTime(app,timeString):
    hour,minute=timeString.split(":")
    hour=float(hour)
    if (hour-app.startTime>=0):
        hour=hour-app.startTime
    else:
        hour=hour+(12-app.startTime)
    return hour+(float(minute)/60)

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
    
    for (messagePopUpName,messagePopUp) in app.messagePopUpDict.items():
        messagePopUp.mousePressed(app,event)
    
    if (app.calendarMode=="Home"):
        app.startApplicationButton.mousePressed(app,event)
        app.changeSettingsButton.mousePressed(app,event)
    




def keyPressed(app,event):
    for (textBoxName,textBox) in app.textBoxDict.items():
        textBox.keyPressed(app,event)
    

def drawWeekCalendarTime(app,canvas):
    for i in range(12):
        timeSuffix=""
        if (app.startTime+i)%24>=12:
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
        dateToWrite=app.sunday+datetime.timedelta(days=(i))
        date= "{}/{}".format(dateToWrite.month, dateToWrite.day)

        canvas.create_text(app.borderWidth+((app.width-app.borderWidth*2)/7)*((2*i+1)/2),
        app.borderHeight/2,text=daysOfTheWeek[i]+"\n"+date,fill="black")
    

    
                

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
    canvas.create_text(app.width-0.5*app.borderWidth,app.borderHeight,text=app.today.year,
                       fill="black",font="Helvetica 26 bold")
    
def drawDayCalendarDate(app,canvas):
    dateToWrite=app.today.strftime("%A")
    date= "{}/{}".format(app.today.month, app.today.day)
    canvas.create_text(app.width/2,
        app.borderHeight/2,text=dateToWrite+"\n"+date,fill="black")



def drawDayCalendarTime(app,canvas):
    drawWeekCalendarTime(app,canvas)
    

def drawDayCalendarOutline(app,canvas):
    canvas.create_rectangle(0+app.borderWidth,0+app.borderHeight,app.width-app.borderWidth,
    app.height-app.borderHeight,fill="light blue")
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

def drawMessagePopUps(app,canvas):
    for (messagePopUpName,messagePopUp) in app.messagePopUpDict.items():
        messagePopUp.drawMessagePopUp(app,canvas)  

def drawHomeScreen(app,canvas):
    canvas.create_rectangle(0,0,app.width,app.height,fill="light yellow")
    canvas.create_text(app.width/2,
    app.height/2,text="Welcome to Smart"+"\n"+"Planner Application!",font="Times 98 bold italic",
    fill="light blue")
    app.startApplicationButton.drawButton(app,canvas)
    app.changeSettingsButton.drawButton(app,canvas)

def redrawAll(app,canvas):
    if (app.calendarMode=="Home"):
        drawHomeScreen(app,canvas)
        drawTextBoxes(app,canvas)
        return
    elif (app.calendarMode=="Week"):
        drawWeekCalendarOutline(app,canvas)
        drawWeekCalendarTime(app,canvas)
        drawWeekCalendarDate(app,canvas)
    else:
        drawDayCalendarOutline(app,canvas)
        drawDayCalendarTime(app,canvas)
        drawDayCalendarDate(app,canvas)
    
    
    drawEvents(app,canvas)
    drawButtons(app,canvas)
    drawTextBoxes(app,canvas)
    drawMessagePopUps(app,canvas)

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

def autoScheduleEvents(app,numInstances,maxDateObject,currEventDate,eventLength,startTime,dayInstancesRemaining,maxDayInstances,validDaysList,dayCount,eventsScheduledList):
    breakLengthHours=float(app.breakLength/60)
    if (numInstances==0):
        return eventsScheduledList
    if (currEventDate>maxDateObject):
        #this is our failure case that we are trying to find an event after specified range
        return None
    if (dayInstancesRemaining==0):
        return autoScheduleEvents(app,numInstances,maxDateObject,currEventDate + datetime.timedelta(days=1),eventLength,0,maxDayInstances,maxDayInstances,validDaysList,0,eventsScheduledList)
    if (dayCount==app.numEventsPerDay):
        return autoScheduleEvents(app,numInstances,maxDateObject,currEventDate + datetime.timedelta(days=1),eventLength,0,maxDayInstances,maxDayInstances,validDaysList,0,eventsScheduledList)

    if (not(currEventDate.strftime('%A') in  validDaysList)):
       return autoScheduleEvents(app,numInstances,maxDateObject,currEventDate + datetime.timedelta(days=1),eventLength,0,maxDayInstances,maxDayInstances,validDaysList,0,eventsScheduledList)
        

    for (eventName,existingEvent) in app.eventDict.items():
        if (existingEvent.dateObject!=currEventDate):
            #no conflicts with scheduled event on a different day
            continue
            #Now we have to check the exent times
        
        passTest1=(startTime<=existingEvent.startTime-breakLengthHours) and (startTime+eventLength<=existingEvent.startTime-breakLengthHours)
        passTest2=(startTime>=existingEvent.endTime+breakLengthHours) and (startTime+eventLength>=existingEvent.endTime+breakLengthHours)
        if  (not passTest1)  and (not passTest2):
            #we have a time conflict
            if (max(startTime+eventLength,existingEvent.endTime+breakLengthHours)>12):
                #try event on the next day
                return autoScheduleEvents(app,numInstances,maxDateObject,currEventDate + datetime.timedelta(days=1),eventLength,0,maxDayInstances,maxDayInstances,validDaysList,0,eventsScheduledList)
            else:
                #try event at a different hour
                return autoScheduleEvents(app,numInstances,maxDateObject,currEventDate,eventLength,existingEvent.endTime+breakLengthHours,dayInstancesRemaining,maxDayInstances,validDaysList,dayCount,eventsScheduledList)
        elif (max(startTime+eventLength,existingEvent.endTime+breakLengthHours)>12):
                autoScheduleEvents(app,numInstances,maxDateObject,currEventDate + datetime.timedelta(days=1),eventLength,0,maxDayInstances,maxDayInstances,validDaysList,0,eventsScheduledList)
        else:
            continue
    for existingEvent in eventsScheduledList:
        if (existingEvent.dateObject!=currEventDate):
            #no conflicts with scheduled event on a different day
            continue
            #Now we have to check the exent times
        passTest1=(startTime<=existingEvent.startTime-breakLengthHours) and (startTime+eventLength<=existingEvent.startTime-breakLengthHours)
        passTest2=(startTime>=existingEvent.endTime+breakLengthHours) and (startTime+eventLength>=existingEvent.endTime+breakLengthHours)
        if  (not passTest1)  and (not passTest2):
            #we have a time conflict
            if (max(startTime+eventLength,existingEvent.endTime+breakLengthHours)>12):
                #try event on the next day
                return autoScheduleEvents(app,numInstances,maxDateObject,currEventDate + datetime.timedelta(days=1),eventLength,0,maxDayInstances,maxDayInstances,validDaysList,0,eventsScheduledList)
            else:
                #try event at a different hour
                return autoScheduleEvents(app,numInstances,maxDateObject,currEventDate,eventLength,existingEvent.endTime+breakLengthHours,dayInstancesRemaining,maxDayInstances,validDaysList,dayCount,eventsScheduledList)
        elif (max(startTime+eventLength,existingEvent.endTime+breakLengthHours)>12):
                autoScheduleEvents(app,numInstances,maxDateObject,currEventDate + datetime.timedelta(days=1),eventLength,0,maxDayInstances,maxDayInstances,validDaysList,0,eventsScheduledList)
        else:
            continue

    i=0
  
    while(( ("generatedEvent"+str(i)) in app.eventDict)==True):
        i+=1
    
    eventToAdd=Event(app,"generatedEvent"+str(len(eventsScheduledList)+i),"generatedEvent","default description",
                     currEventDate.strftime("%A"),startTime,startTime+eventLength,"light green")
    eventToAdd.dateObject=currEventDate
    newList=eventsScheduledList
    newList.append(eventToAdd)
    return autoScheduleEvents(app,numInstances-1,maxDateObject,currEventDate,eventLength,startTime+eventLength+breakLengthHours,dayInstancesRemaining-1,maxDayInstances,validDaysList,dayCount+1,newList)

def violatesConstraints(app,startTime,endTime,eventDate):
    count=0
    for (eventName,existingEvent) in app.eventDict.items():
        if (eventDate!=existingEvent.dateObject):
            continue
        count+=1
        if(count==app.numEventsPerDay):
            return True
        if (endTime+(app.breakLength/60)>existingEvent.startTime) and (startTime<existingEvent.startTime):
            return True
        elif startTime-(app.breakLength/60)<existingEvent.endTime and (startTime>existingEvent.startTime):
            return True
    return False
        
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
     
        self.dateObject=app.sunday+datetime.timedelta(days=determineWidthFromDate(date)) 

        
    def mousePressed(self,app,event):
        if (self.dateObject>=app.sunday) and (self.dateObject<=app.saturday):
            startXCord=0
            if (app.calendarMode=="Week"):
                startXCord=app.borderWidth+((app.width-app.borderWidth*2)/7)*determineWidthFromDate(self.date)
            elif (app.calendarMode=="Day"):
                startXCord=app.borderWidth
            else: pass
            endXCord=0
            if (app.calendarMode=="Week"):
                endXCord=app.borderWidth+((app.width-app.borderWidth*2)/7)*(determineWidthFromDate(self.date)+1)
            elif (app.calendarMode=="Day"):
                endXCord=app.width-app.borderWidth
            else: pass

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
            validToDrawWeek=(app.calendarMode=="Week") and (self.dateObject>=app.sunday) and (self.dateObject<=app.saturday)
            validToDrawDay=(app.calendarMode=="Day") and (self.dateObject==app.today)
            if (validToDrawWeek or validToDrawDay): 
                startXCord=0      
                if (app.calendarMode=="Week"):
                    startXCord=app.borderWidth+((app.width-app.borderWidth*2)/7)*determineWidthFromDate(self.date)
                elif (app.calendarMode=="Day"):
                    startXCord=app.borderWidth
                else: pass
                endXCord=0
                if (app.calendarMode=="Week"):
                    endXCord=app.borderWidth+((app.width-app.borderWidth*2)/7)*(determineWidthFromDate(self.date)+1)
                elif (app.calendarMode=="Day"):
                    endXCord=app.width-app.borderWidth
                else: pass
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
            elif (self.buttonType=="nextWeek"):
                app.today=app.today+datetime.timedelta(days=7)
                app.sunday=app.sunday+datetime.timedelta(days=7)
                app.saturday=app.saturday+datetime.timedelta(days=7)
            elif (self.buttonType=="prevWeek"):
                app.today=app.today-datetime.timedelta(days=7)
                app.sunday=app.sunday-datetime.timedelta(days=7)
                app.saturday=app.saturday-datetime.timedelta(days=7)
            elif (self.buttonType=="switchMode"):
                if (app.calendarMode=="Week"):
                    app.calendarMode="Day"
                elif (app.calendarMode=="Day"):
                    app.calendarMode="Week"
                else: pass
            elif (self.buttonType=="nextDay"):
                app.today=app.today+datetime.timedelta(days=1)
                if (app.today.strftime("%A")=="Sunday"):
                    app.sunday = app.sunday + datetime.timedelta(days=7)
                    app.saturday = app.saturday + datetime.timedelta(days=7)

            elif (self.buttonType=="prevDay"):
                app.today=app.today-datetime.timedelta(days=1)
                if (app.today.strftime("%A")=="Saturday"):
                    app.sunday = app.sunday - datetime.timedelta(days=7)
                    app.saturday = app.saturday - datetime.timedelta(days=7)
            
            elif (self.buttonType=="start"):
                app.calendarMode="Week"
            elif (self.buttonType=="home"):
                app.calendarMode="Home"
           

                

                
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

       
class MessagePopUp:
    def __init__(self,app,name,message):
        self.name=name
        self.message=message
        self.activated=False

    def mousePressed(self,app,event):
        if (self.activated==True):
            if (event.x>=0.25*app.width) and (event.y>=0.25*app.height) and (event.x<=0.75*app.width) and (event.y<=0.75*app.height):
                self.activated=False
                
    def drawMessagePopUp(self,app,canvas):
        if (self.activated==True):
            canvas.create_rectangle(0.25*app.width,0.25*app.height,0.75*app.width,0.75*app.height,
            fill="light yellow")
            canvas.create_text(0.5*app.width,0.5*app.height,text=self.message,fill="black")
            
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
            
            dateObject=app.sunday+datetime.timedelta(days=determineWidthFromDate(date)) 

            
            if violatesConstraints(app,time1,time2,dateObject):
                app.failAutoSchedulePopUp.activated=True
            else:
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
        elif (self.name=="changeSettingsTextBox") and (app.changeSettingsTextBox.clicked==True):
            startTime=self.answers[0]
            time,suffix=startTime.split(" ")
            if suffix=="am":
                app.startTime=int(time)%12
            else:
                app.startTime=int(time)+12
            app.breakLength=int(self.answers[1])
            app.numEventsPerDay=int(self.answers[2])
            app.endTime=app.startTime+12
            for i in range(len(self.answers)):
                        self.answers[i]=""
            
        
        elif (self.name=="autoScheduleTextBox") and (app.autoScheduleTextBox.clicked==True):
            #11/2/2004 to 11/18/2004
            rangeOfDatesString=self.answers[0]
            daysOfTheWeekString=self.answers[1]

            validDaysList = daysOfTheWeekString.split(',')



            maxInstancesPerDay=int(self.answers[2])
            numInstances=int(self.answers[3])
            eventLength=float(self.answers[4])

            rangeOfDatesStringSplit=rangeOfDatesString.split()
            minDateString=rangeOfDatesStringSplit[0]
            maxDateString=rangeOfDatesStringSplit[2]

            minDateObject=datetime.datetime.strptime(minDateString, "%m/%d/%Y").date()
            maxDateObject=datetime.datetime.strptime(maxDateString, "%m/%d/%Y").date()
            

            #(app,numInstances,maxDateObject,currEventDate,eventLength,startTime,breakLength,eventsScheduledList)
            eventsToAddList=autoScheduleEvents(app,numInstances,maxDateObject,minDateObject,eventLength,0.0,maxInstancesPerDay,maxInstancesPerDay,validDaysList,0,[])
            
            if (eventsToAddList==None):
                app.failAutoSchedulePopUp.activated=True
            else:
                for j in range(len(eventsToAddList)):
                    app.eventDict[eventsToAddList[j].name]=eventsToAddList[j]
            for i in range(len(self.answers)):
                        self.answers[i]=""

        elif (self.name=="jumpToTextBox") and (app.jumpToTextBox.clicked==True):
            jumpToDate=self.answers[0]
            app.today=datetime.datetime.strptime(jumpToDate, "%m/%d/%Y").date()
            app.currentWeekDay = app.today.weekday()
            app.sunday = app.today - datetime.timedelta(days=(app.currentWeekDay + 1)%7)
            app.saturday = app.sunday + datetime.timedelta(days=6)
            
            for i in range(len(self.answers)):
                        self.answers[i]=""

   

runApp(width=1000,height=600)