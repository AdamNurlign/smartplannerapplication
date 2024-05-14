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

    app.createEventTextBox=TextBox(app,"createEventTextBox",["What time does your event start?","What time does your event end?","What day is your event on?","What is the name of the event?"])
   
   
    app.textBoxDict=dict()
    app.textBoxDict["createEventTextBox"]=app.createEventTextBox




    app.clickedDelete=False
    
    

def mousePressed(app,event):
    app.borderWidth=app.width/10
    app.borderHeight=app.height/10

    dict_copy = app.eventDict.copy()

    for key in dict_copy:
        dict_copy[key].mousePressed(app,event)

    app.deleteButton.mousePressed(app,event)
    app.createEventButton.mousePressed(app,event)


    for (textBoxName,textBox) in app.textBoxDict.items():
        textBox.mousePressed(app,event)
        textBox.closeButton.mousePressed(app,event)
        textBox.enterButton.mousePressed(app,event)
    



def keyPressed(app,event):
    app.createEventTextBox.keyPressed(app,event)
    

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


    
class Event:
    def __init__(self,app,name,eventType,description,date,startTime,endTime,color):
        self.name=name
        self.eventType=eventType
        self.description=description
        self.date=date
        self.startTime=startTime
        self.endTime=endTime
        self.color=color
        

        #0 to 23 is our set of allowable startTime and endTime 

    def mousePressed(self,app,event):
        startXCord=app.borderWidth+((app.width-app.borderWidth*2)/7)*determineWidthFromDate(self.date)
        endXCord=app.borderWidth+((app.width-app.borderWidth*2)/7)*(determineWidthFromDate(self.date)+1)
        startYCord=app.borderHeight+((app.height-app.borderHeight*2)/12)*(self.startTime-app.startTime)
        endYCord=app.borderHeight+((app.height-app.borderHeight*2)/12)*(self.endTime-app.startTime)
        if (event.x>=startXCord) and (event.y
                >=startYCord) and (event.x<=endXCord) and (event.y<=endYCord):
            if (app.clickedDelete==True):
                app.eventDict.pop(self.name)
                app.clickedDelete=False
            
                


    def drawEvent(self,app,canvas):
        
        startXCord=app.borderWidth+((app.width-app.borderWidth*2)/7)*determineWidthFromDate(self.date)
        endXCord=app.borderWidth+((app.width-app.borderWidth*2)/7)*(determineWidthFromDate(self.date)+1)
        startYCord=app.borderHeight+((app.height-app.borderHeight*2)/12)*(self.startTime-app.startTime)
        endYCord=app.borderHeight+((app.height-app.borderHeight*2)/12)*(self.endTime-app.startTime)
        if (app.clickedDelete==False):
            canvas.create_rectangle(startXCord,startYCord,endXCord,endYCord,
            fill=self.color)
        else:
            canvas.create_rectangle(startXCord,startYCord,endXCord,endYCord,
            fill=self.color,outline="red")
        
        canvas.create_text((endXCord+startXCord)/2,(endYCord+startYCord)/2,
                           text=self.name,fill="black")
        
        
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
            if (self.textBoxName!=None) and (self.buttonType!="closeTextBox"):
                app.textBoxDict[self.textBoxName].clicked=True
            else: 
                pass
                
            if (self.buttonType=="Delete"):
                app.clickedDelete=True
            elif (self.buttonType=="closeTextBox"):
                app.textBoxDict[self.textBoxName].clicked=False
            elif (self.buttonType=="enterTextBox"):
                app.textBoxDict[self.textBoxName].processCreateEventAnswers(app)
                app.textBoxDict[self.textBoxName].clicked=False

                
                
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
        self.closeButton=Button(app,"close","closeTextBox","red",2,8.5,name)
        self.enterButton=Button(app,"enter","enterTextBox","light green",4,8.5,name)



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

    def processCreateEventAnswers(self,app):
        time1=int(self.answers[0])
        time2=int(self.answers[1])
        date=self.answers[2]
        name=self.answers[3]
        #(self,app,name,eventType,description,date,startTime,endTime,color)
        newEvent=Event(app,name,"newEvent","newEvent description",date,time1,time2,"light green")
        app.eventDict[name]=newEvent
        for i in range(len(self.answers)):
                    self.answers[i]=""
        
                    

                
        

            



          

    
    
        
   

runApp(width=1000,height=600)