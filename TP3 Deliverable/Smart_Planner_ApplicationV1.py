#Planner Term Project Starter File
#Adam Nurlign andrewID: ain

import math, copy, random
import tkinter

from cmu_112_graphics import *
from datetime import date


#Stores the model
def appStarted(app):
    app.margin=5
    app.calendarMode="Week"
    app.days=[]
    app.numDays=12
    app.numHours=12
    app.days=["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]
    app.dayCounter=0
    app.spaceBetweenHorizontal=(app.width/7)-(app.margin/2)
    app.spaceBetweenVertical=(app.height/12)-(app.margin/2)
    app.numDays=7
    app.startTime=0

    app.eventDict=dict()
    app.eventList=[]
    app.eventsCoordinates=[]
    
    app.startAppButton=Button(app,"Start",(app.width/2,app.height/1.5),"light green","startApplication")
    app.learnMoreButton=Button(app,"Learn More",(app.width/2,app.height/1.5),"fuchsia","learnMore")
    app.drawLearnMoreText=False
    app.returnHomeButton=Button(app,"Return Home",
    (app.margin+7.5*app.spaceBetweenHorizontal+25,app.margin+11*app.spaceBetweenVertical),
    "light blue","returnHome")
    



    app.createEventButton=Button(app,"Create Event",
    (app.margin+7.5*app.spaceBetweenHorizontal+25,app.margin+3*app.spaceBetweenVertical),
    "yellow","create")

    app.editEventButton=Button(app,"Edit Event",(app.margin+8.5*app.spaceBetweenHorizontal+50,
    app.margin+3*app.spaceBetweenVertical),"light green","edit")

    app.deleteEventButton=Button(app,"Delete Event",
    (app.margin+7.5*app.spaceBetweenHorizontal+25,app.margin+5*app.spaceBetweenVertical),
    "red","delete")

    app.switchModeButton=Button(app,"Switch Mode",
    (app.margin+7.5*app.spaceBetweenHorizontal+25,app.margin+7*app.spaceBetweenVertical),
    "green","switch")

    app.autoScheduleButton=Button(app,"Auto Schedule",(app.margin+7.5*app.spaceBetweenHorizontal+25,app.margin+9*app.spaceBetweenVertical),"blue","auto")

    app.nextDayButton=smallButton(app,"Next Day",
    (app.margin+8.5*app.spaceBetweenHorizontal+50,app.margin+5*app.spaceBetweenVertical),
    "green","next")
    app.previousDayButton=smallButton(app,"Prev. Day",
    (app.margin+8.5*app.spaceBetweenHorizontal+50,app.margin+7*app.spaceBetweenVertical),
    "orange","previous")

    app.nextWeekButton=smallButton(app,"Next Week",
    (app.margin+8.5*app.spaceBetweenHorizontal+50,app.margin+5*app.spaceBetweenVertical),
    "green","nextWeek")
    app.previousWeekButton=smallButton(app,"Prev. Week",
    (app.margin+8.5*app.spaceBetweenHorizontal+50,app.margin+7*app.spaceBetweenVertical),
    "orange","previousWeek")

    app.goToTodayButton=smallButton(app,"Today",(app.margin+8.5*app.spaceBetweenHorizontal+50,
    app.margin+9*app.spaceBetweenVertical),"light green","goToToday")
    
    app.confirmEventButton=smallButton(app,"Confirm",(750,900),"green","confirm")
    app.cancelEventButton=smallButton(app,"Cancel",(850,900),"red","cancel")


    app.practiceTextBoxQuestions=["What is your event?","When will this event start? (ex:10)",
    "When will this event end? (ex:11)"]
    if (app.calendarMode=="Week"):
            app.practiceTextBoxQuestions.append("Sun,Mon,Tue,Wed,Thu,Fri,Sat?")
    
    app.practiceTextBox=textBox(app,(800,800),500,app.practiceTextBoxQuestions)
    app.clickedPractice=False


    app.autoScheduleTextBoxQuestions=["What is your event?","How long will your event last?",
    "What Day? (ex:Sun)","How many instances?"]
    



    app.autoScheduleTextBox=textBox(app,(800,800),500,app.autoScheduleTextBoxQuestions)
    app.clickedAutoSchedule=False
    app.confirmAutoEventButton=smallButton(app,"Confirm",(750,850),"green","confirm auto")
    app.cancelAutoEventButton=smallButton(app,"Cancel",(850,850),"red","cancel auto")



    app.editEventTextBox=textBox(app,(800,800),400,["Rename Event: "])
    app.clickedEditEvent=False
    app.confirmEditEventButton=smallButton(app,"Confirm",(750,850),"green","confirm edit")
    app.cancelEditEventButton=smallButton(app,"Cancel",(850,850),"red","cancel edit")

    app.currentlyEdited=0
    app.tryingToAddAuto=[]


    app.dates=[]
    app.months=["January","Febuary","March","April","May","June","July","August","September",
    "October","November","December"]
    app.numDaysPerMonth=[["January",31],["Febuary",28],["March",31],["April",30],["May",31],
    ["June",30],["July",31],["August",31],["September",30],["October",31],["November",30],
    ["December",31]]
    for x in range(len(app.numDaysPerMonth)):
        monthDates=[]
        for y in range(1,app.numDaysPerMonth[x][1]+1):
            monthDates.append(y)
        app.dates.append(monthDates)



    #https://docs.python.org/3/library/datetime.html
    app.currentDateString=str(date.today())
    #2022-12-05

    app.dayOfTheWeek=(int(datetime.datetime.today().weekday())+1)

    app.currentYear=int(app.currentDateString[0:4])
    app.currentDay=int(app.currentDateString[8::])
    app.currentMonthString=app.numDaysPerMonth[int(app.currentDateString[5:7])-1][0]
    app.currentMonthInt=app.months.index(app.currentMonthString)
    app.dayOfTheWeekString=app.days[app.dayOfTheWeek]

   





    

def mousePressed(app,event):
        
        app.createEventButton.mousePressed(app,event)
        app.editEventButton.mousePressed(app,event)
        app.deleteEventButton.mousePressed(app,event)
        app.switchModeButton.mousePressed(app,event)
        app.goToTodayButton.mousePressed(app,event)
        app.returnHomeButton.mousePressed(app,event)

        if(app.calendarMode=="Home"):
            app.startAppButton.mousePressed(app,event)
            app.learnMoreButton.mousePressed(app,event)

        if(app.calendarMode=="Day"):
            app.nextDayButton.mousePressed(app,event)
            app.previousDayButton.mousePressed(app,event)
        if(app.calendarMode=="Week"):
            app.autoScheduleButton.mousePressed(app,event)
            app.nextWeekButton.mousePressed(app,event)
            app.previousWeekButton.mousePressed(app,event)

        
        app.deleteEventButton.mousePressedDelete(app,event)
        app.editEventButton.mousePressedEdit(app,event)

        if(app.clickedPractice==True):
            app.practiceTextBox.mousePressed(app,event)
            app.confirmEventButton.mousePressed(app,event)
            app.cancelEventButton.mousePressed(app,event)
        
        if(app.clickedAutoSchedule==True):
            app.autoScheduleTextBox.mousePressed(app,event)
            app.confirmAutoEventButton.mousePressed(app,event)
            app.cancelAutoEventButton.mousePressed(app,event)

        if(app.clickedEditEvent==True):
            app.editEventTextBox.mousePressed(app,event)
            app.confirmEditEventButton.mousePressed(app,event)
            app.cancelEditEventButton.mousePressed(app,event)
           

        
        
        
        

def keyPressed(app,event):
    if (app.clickedPractice==True):
        app.practiceTextBox.keyPressed(app,event)
    if (app.clickedAutoSchedule==True):
        app.autoScheduleTextBox.keyPressed(app,event)
    if (app.clickedEditEvent==True):
        app.editEventTextBox.keyPressed(app,event)


#Commands if user wants to Learn More
def drawLearnMore(app,canvas):
    if (app.drawLearnMoreText==True):
        canvas.create_rectangle(app.width/2,1*app.height/4,3*app.width/4,
        3*app.height/4,fill="light blue")
        canvas.create_rectangle(app.width/2,1*app.height/4,3*app.width/4,
        3*app.height/4)
        readMeText="""
        READ ME:
        Welcome to the Smart Planner 
        Application! The following application
        is a Schedule Planner that allows you 
        to create, edit, and delete events.
        You can create events manually
        using the Create Event Feature 
        or schedule events automatically
        using the Auto Schedule Feature
        which takes in user preferences.
        As normal you can view you events
        in a day view or week view. Hope
        you enjoy!
        """
        canvas.create_text(2.5*app.width/4,1*app.height/2,text=readMeText,fill="black")

#Draw functions for Week Mode
def drawDate(app,canvas):
    if (app.calendarMode=="Day"): #Universal method
        canvas.create_text(app.margin+(app.numDays+1)*app.spaceBetweenHorizontal+30,
        app.margin+app.spaceBetweenVertical,text=app.dayOfTheWeekString+" "+app.currentMonthString+" "+str
        (app.currentDay),font="Helvetica 26 bold")
    if (app.calendarMode=="Week"):
        canvas.create_text(app.margin+(app.numDays+1)*app.spaceBetweenHorizontal+30,
        app.margin+app.spaceBetweenVertical,text=app.currentMonthString+" "+str(app.currentYear),
        font="Helvetica 26 bold")


def drawRectanglesWeek(app,canvas,row,col):
    if (col!=0):
        canvas.create_rectangle(app.margin+row*app.spaceBetweenHorizontal,
        app.margin+col*app.spaceBetweenVertical,app.margin+(row+1)*
        app.spaceBetweenHorizontal,app.margin+(col+1)*app.spaceBetweenVertical)

def drawDateHeadersWeek(app,canvas):
    for x in range(app.numDays):
        canvas.create_text(app.margin+x*app.spaceBetweenHorizontal+
        (app.spaceBetweenHorizontal/2),(app.margin+app.spaceBetweenVertical)/2
        ,text=app.days[x])
    i=0
    for x in range(app.currentDay-app.days.index(app.dayOfTheWeekString),
    app.currentDay+(6-app.days.index(app.dayOfTheWeekString))+1):
        if(x<=app.numDaysPerMonth[app.currentMonthInt][1]):
            canvas.create_text(app.margin+i*app.spaceBetweenHorizontal+
            (app.spaceBetweenHorizontal/2),(app.margin+app.spaceBetweenVertical)/1.2
            ,text=str(x))
            i+=1
        else:
            canvas.create_text(app.margin+i*app.spaceBetweenHorizontal+
            (app.spaceBetweenHorizontal/2),(app.margin+app.spaceBetweenVertical)/1.2
            ,text=str(x%app.numDaysPerMonth[app.currentMonthInt][1]))
            i+=1
    i=0
    

def drawBorderWeek(app,canvas):
    for row in range(app.numDays):
        for col in range (app.numHours+1):
            drawRectanglesWeek(app,canvas,row,col)
    

def drawTimesWeek(app,canvas):
    for y in range(1,app.numHours+2):
        time=y+app.startTime-1
        if(time>=24):
            time=time%24
        if (time==0):
            canvas.create_text((app.margin+app.spaceBetweenHorizontal)/7,
            app.margin+y*app.spaceBetweenVertical+5,text=str(12)+
            " pm",fill="red")
        elif (time==12):
            canvas.create_text((app.margin+app.spaceBetweenHorizontal)/7,
            app.margin+y*app.spaceBetweenVertical+5,text=str(12)+
            " am",fill="red")
        elif (time<=11):
            canvas.create_text((app.margin+app.spaceBetweenHorizontal)/7,
            app.margin+y*app.spaceBetweenVertical+5,text=str(time)+
            " pm",fill="red")
        else:
            canvas.create_text((app.margin+app.spaceBetweenHorizontal)/7,
            app.margin+y*app.spaceBetweenVertical+5,text=str(time%12)+
            " am",fill="red")


def drawButtons(app,canvas):
    if(app.calendarMode=="Home"):
        app.startAppButton.center=(2*app.width/5,app.height/1.5)
        app.startAppButton.drawButton(app,canvas)
        app.learnMoreButton.center=(3*app.width/5,app.height/1.5)
        app.learnMoreButton.drawButton(app,canvas)
    if (app.calendarMode=="Day") or (app.calendarMode=="Week"):
        app.createEventButton.drawButton(app,canvas)
        app.deleteEventButton.drawButton(app,canvas)
        app.editEventButton.drawButton(app,canvas)
        app.switchModeButton.drawButton(app,canvas)
        app.goToTodayButton.drawButton(app,canvas)
        app.returnHomeButton.drawButton(app,canvas)
    

    
    if (app.calendarMode=="Day"):
        app.nextDayButton.drawButton(app,canvas)
        app.previousDayButton.drawButton(app,canvas)
    if (app.calendarMode=="Week"):
        app.autoScheduleButton.drawButton(app,canvas)
        app.nextWeekButton.drawButton(app,canvas)
        app.previousWeekButton.drawButton(app,canvas)

def drawTextBoxes(app,canvas):
    if (app.clickedPractice==True):
        if (app.calendarMode!="Home"):
            app.practiceTextBox.drawTextBox(app,canvas)
            app.confirmEventButton.drawButton(app,canvas)
            app.cancelEventButton.drawButton(app,canvas)
        
    if (app.clickedAutoSchedule==True):
        if (app.calendarMode!="Home"):
            app.autoScheduleTextBox.drawTextBox(app,canvas)
            app.confirmAutoEventButton.drawButton(app,canvas)
            app.cancelAutoEventButton.drawButton(app,canvas)
    
    if (app.clickedEditEvent==True):
        if(app.calendarMode!="Home"):
            app.editEventTextBox.drawTextBox(app,canvas)
            app.confirmEditEventButton.drawButton(app,canvas)
            app.cancelEditEventButton.drawButton(app,canvas)
  


    
def drawEvents(app,canvas): 
    x1=0
    x2=0
    if (app.calendarMode=="Week"):
        x1=0
        x2=2
    elif (app.calendarMode=="Day"):
        x1=4
        x2=5

    for event in app.eventDict:
        if (app.eventDict[event][3]!=app.currentDay) and (app.calendarMode=="Day"):
            continue
        upperBound=app.currentDay+(6-app.days.index(app.dayOfTheWeekString))
        lowerBound=app.currentDay-app.days.index(app.dayOfTheWeekString)

        if (app.eventDict[event][3]>upperBound) and (app.calendarMode=="Week"):
            continue
        if (app.eventDict[event][3]<lowerBound) and (app.calendarMode=="Week"):
            continue
        if (app.calendarMode=="Day"):
            if (app.eventDict[event][2]!=app.dayOfTheWeekString):
                continue
            
        
        number=app.eventList.index(event)

        canvas.create_rectangle(app.eventsCoordinates[number][x1],app.eventsCoordinates[number][1],
        app.eventsCoordinates[number][x2],app.eventsCoordinates[number][3],fill="pink")

        canvas.create_text((app.eventsCoordinates[number][x1]+app.eventsCoordinates[number][x2])/2,
        (app.eventsCoordinates[number][1]+app.eventsCoordinates[number][3])/2,text=str(event))

        if(app.deleteEventButton.clicked==True) or (app.editEventButton.clicked==True):
            canvas.create_rectangle(app.eventsCoordinates[number][x1],app.eventsCoordinates[number][1],
            app.eventsCoordinates[number][x2],app.eventsCoordinates[number][3],outline="red",width=5)
        




#Draw functions for day Mode

def drawRectanglesDay(app,canvas,row):
    canvas.create_rectangle(app.margin,app.margin+row*app.spaceBetweenVertical
    ,app.margin+7*app.spaceBetweenHorizontal,app.margin+(row+1)*app.spaceBetweenVertical)

def drawBorderDay(app,canvas):
    for x in range(1,app.numHours+1):
        drawRectanglesDay(app,canvas,x)



def drawTimesDay(app,canvas):
    drawTimesWeek(app,canvas)


#Draws the Main Home Screen
def drawHomeScreen(app,canvas):
    canvas.create_rectangle(0,0,app.width,app.height,fill="light yellow")
    canvas.create_text(app.width/2,
    app.margin+3*app.spaceBetweenVertical,text="Welcome to Smart"+"\n"+"Planner Application!",font="Times 98 bold italic",
    fill="light blue")
    



def redrawAll(app,canvas):
    if (app.calendarMode=="Home"):
        drawHomeScreen(app,canvas)
        drawLearnMore(app,canvas)
    if (app.calendarMode=="Week") or (app.calendarMode=="Day"):
        canvas.create_rectangle(0,0,app.width,app.height,fill="ivory2")
        canvas.create_rectangle(app.createEventButton.center[0]-app.createEventButton.buttonWidth-10,
                app.createEventButton.center[1]-app.createEventButton.buttonHeight-10,
                app.editEventButton.center[0]+app.editEventButton.buttonWidth+10,
                app.autoScheduleButton.center[1]+app.autoScheduleButton.buttonHeight+10,fill="light yellow")
    drawDate(app,canvas)
    drawButtons(app,canvas)
    drawTextBoxes(app,canvas)
        
    if (app.calendarMode=="Week"):
        drawBorderWeek(app,canvas)
        drawDateHeadersWeek(app,canvas)
        drawTimesWeek(app,canvas)
        drawEvents(app,canvas)
    
    if (app.calendarMode=="Day"):
        drawBorderDay(app,canvas)
        drawTimesDay(app,canvas) 
        drawEvents(app,canvas)

    
    
    



class Button:
        def __init__(self,app,text,center,color,buttonType):
            self.text=text
            self.center=(center[0],center[1])
            self.buttonWidth=0.5*app.spaceBetweenHorizontal
            self.buttonHeight=0.5*app.spaceBetweenVertical
            self.color=color
            self.buttonType=buttonType
            self.clicked=False
            

        def mousePressed(self,app,event):
            if (event.x>=self.center[0]-self.buttonWidth) and (event.y
            >=self.center[1]-self.buttonHeight) and (event.x<=self.center[0]+
            self.buttonWidth) and (event.y<=self.center[1]+self.buttonHeight):
                #Create Button commands
                if(self.buttonType=="startApplication"):
                    app.calendarMode="Week"

                elif(self.buttonType=="create"):
                    app.clickedPractice=True
                #Edit Button commands
                elif(self.buttonType=="edit"):       
                    app.editEventButton.clicked=True

                #Confirm edit button commands
                elif (self.buttonType=="confirm edit"):
                    if (app.clickedEditEvent==True):
                        newKey=app.editEventTextBox.enterTextBoxes[0]         
                        popped=app.eventDict.pop(app.eventList[app.currentlyEdited])
                        i=1
                        while (((newKey+str(i)) in app.eventDict)==True):
                            i+=1
                        newKey=newKey+str(i)
                        app.eventDict[newKey]=popped
                        app.eventList[app.currentlyEdited]=newKey
                        app.editEventButton.clicked=False
                        app.currentlyEdited=0
                    app.clickedEditEvent=False
                    for x in range(len(app.editEventTextBox.enterTextBoxes)):
                        app.editEventTextBox.enterTextBoxes[x]=""     
                    

                #Cancel Edit commands
                elif(self.buttonType=="cancel edit"):
                    app.currentlyEdited=0
                    app.clickedEditEvent=False
                    app.editEventButton.clicked=False
                    for x in range(len(app.editEventTextBox.enterTextBoxes)):
                        app.editEventTextBox.enterTextBoxes[x]=""       
                                



                #Delete Button commands    
                elif(self.buttonType=="delete"):
                    app.deleteEventButton.clicked=True
                
                #Switch Button commands
                elif(self.buttonType=="switch"):
                     if (app.calendarMode=="Week"):
                        app.calendarMode="Day"
                     elif (app.calendarMode=="Day"):
                        app.calendarMode="Week"

                
                
                #Auto Schedule Button commands
                elif (self.buttonType=="auto"):
                    app.clickedAutoSchedule=True
                
                #Confirm auto commands
                elif(self.buttonType=="confirm auto"):
                    if (app.clickedAutoSchedule==True):
                        eventsDesired=[]
                        userPreferences=dict()
                        event1=app.autoScheduleTextBox.enterTextBoxes[0]
                        event2=app.autoScheduleTextBox.enterTextBoxes[1]
                        if (app.calendarMode=="Week"):
                            event3=app.autoScheduleTextBox.enterTextBoxes[2]
                            event4=app.autoScheduleTextBox.enterTextBoxes[3]
                        
                        
                    
                        #Just takes care of cancel case for now
                        if (type(event1)!=str) or (type(int(event2))!=int):
                            if (app.calendarMode=="Week"):
                                if (type(event4)!=str):
                                    return
                            return

                        for x in range(int(event4)):
                            i=1
                            while (((event1+str(i)) in userPreferences)==True) or (((event1+str(i)) in app.eventDict)==True):
                                i+=1
                            
                            userPreferences[event1+str(i)]=(event2,event3,
                            app.currentDay-(app.days.index(app.dayOfTheWeekString)-app.days.index(event3)))#Theproblem is here need to also append a day for event)
                            eventsDesired.append(event1+str(i))


                        #Backtracking methods
                        def isLegalAutoSchedule(event,startTime,endTime,Day,res):
                            if (endTime>app.startTime+app.numHours):
                                return False
                        #Check if it conflicts with start time end time or day
                            if (len(app.eventDict)==0):
                                for resultsSoFar in res:
                                    if (startTime>(res[resultsSoFar][0])) and (startTime<(res[resultsSoFar][1])):    
                                        return False
                                    elif(startTime==(res[resultsSoFar][0])):
                                        return False
                            if (len(app.eventDict)==0):
                                return True
                            dayToCheck=None
                            for eventsAlreadyIn in app.eventDict:
                                if (startTime<int(app.eventDict[eventsAlreadyIn][0])) and (endTime<=int(app.eventDict[eventsAlreadyIn][0])):
                                    if (Day==app.eventDict[eventsAlreadyIn][2]):
                                        #Checks that when adding multiple events at the same time they don't overlap
                                        for resultsSoFar in res:
                                            if (startTime>(res[resultsSoFar][0])) and (startTime<(res[resultsSoFar][1])):         
                                                return False
                                            elif(startTime==(res[resultsSoFar][0])):
                                                return False
                                            else:
                                                dayToCheck=app.eventDict[eventsAlreadyIn][2]
                                                continue             
                                                
                                elif (startTime>=int(app.eventDict[eventsAlreadyIn][1])) and (endTime>int(app.eventDict[eventsAlreadyIn][1])):
                                    if (Day==app.eventDict[eventsAlreadyIn][2]):
                                        for resultsSoFar in res:
                                            if (startTime>(res[resultsSoFar][0])) and (startTime<(res[resultsSoFar][1])):         
                                                return False
                                            elif(startTime==(res[resultsSoFar][0])):
                                                return False
                                            else:
                                                dayToCheck=app.eventDict[eventsAlreadyIn][2]
                                                continue
                                                
                            
                                else:      
                                    return False  

                            for x in range(len(app.tryingToAddAuto)):
                                if (startTime<int(app.tryingToAddAuto[x][0])) and (endTime<=int(app.tryingToAddAuto[x][0])):
                                    if (Day==dayToCheck):
                                        #Checks that when adding multiple events at the same time they don't overlap
                                        for resultsSoFar in res:
                                            if (startTime>(res[resultsSoFar][0])) and (startTime<(res[resultsSoFar][1])):         
                                                return False
                                            elif(startTime==(res[resultsSoFar][0])):
                                                return False        
                                            else:
                                                continue 
                                    elif (startTime>=int(app.tryingToAddAuto[x][1])) and (endTime>int(app.tryingToAddAuto[x][1])):  
                                        if (Day==dayToCheck):
                                            for resultsSoFar in res:
                                                if (startTime>(res[resultsSoFar][0])) and (startTime<(res[resultsSoFar][1])):    
                                                    return False
                                                elif(startTime==(res[resultsSoFar][0])):     
                                                    return False
                                                else:
                                                    continue 
                                        
                                    else:
                                        return False            
                            return True

                    
                        def autoScheduleAlgorithm(eventsDesired,userPreferences):
                            return autoScheduleAlgorithmHelper(eventsDesired,userPreferences,dict())
                            
                        def autoScheduleAlgorithmHelper(eventsDesired,userPreferences,res):
                            if (eventsDesired==[]):                 
                                return res
                            else:
                                event=eventsDesired[0]
                                for x in range(0,app.numHours-int(userPreferences[event][0])+1):
                                    if isLegalAutoSchedule(event,x,x+int(userPreferences[event][0]),userPreferences[event][1],res):
                                        app.tryingToAddAuto.append((x,x+int(userPreferences[event][0]),userPreferences[event][1]))
                                        res[event]=(x,x+int(userPreferences[event][0]),userPreferences[event][1])
                                        possibleSolution=autoScheduleAlgorithmHelper(eventsDesired[1::],userPreferences,res)
                                        if (possibleSolution!=None):
                                            return possibleSolution
                                        del res[event]
                                return None
                        #End of Back tracking methods
                        

                        eventsToAdd=autoScheduleAlgorithm(eventsDesired,userPreferences)
                        if (eventsToAdd!=None):
                            for x in eventsToAdd:
                                app.eventDict[x]=[eventsToAdd[x][0],eventsToAdd[x][1],eventsToAdd[x][2],
                                app.currentDay-(app.days.index(app.dayOfTheWeekString)-app.days.index(event3))]
                                app.eventList.append(x)    
                                leftXMultiplierWeek=app.days.index(app.eventDict[x][2])
                                rightXMultiplierWeek=leftXMultiplierWeek+1
                                leftXWeek=app.margin+leftXMultiplierWeek*app.spaceBetweenHorizontal
                                rightXWeek=app.margin+rightXMultiplierWeek*app.spaceBetweenHorizontal
                                
                                leftXDay=app.width/4
                                rightXDay=app.width/2
                                if (int(app.eventDict[x][0])>=app.startTime) and (int(app.eventDict[x][0])
                    <12):
                                    topY=app.margin+(abs(int(app.eventDict[x][0])-app.startTime)+1
                                    )*app.spaceBetweenVertical
                                    bottomY=app.margin+(abs(int(app.eventDict[x][1])-app.startTime)+1
                                    )*app.spaceBetweenVertical
                                else:
                                    difference=(-1*app.startTime)+13
                                    topY=app.margin+(int(app.eventDict[x][0])+difference
                                    )*app.spaceBetweenVertical
                                    bottomY=app.margin+(int(app.eventDict[x][1])+difference
                                    )*app.spaceBetweenVertical
                                app.eventsCoordinates.append((leftXWeek,topY,rightXWeek,bottomY,leftXDay,rightXDay))
                                for x in range (len(app.autoScheduleTextBox.enterTextBoxes)):
                                    app.autoScheduleTextBox.enterTextBoxes[x]=""
                        app.autoScheduleTextBox.clicked=False
                        app.clickedAutoSchedule=False       
                        app.tryingToAddAuto=[] 
                    
                #Cancel Auto Schedule commands
                elif(self.buttonType=="cancel auto"):
                    app.clickedAutoSchedule=False
                    app.autoScheduleTextBox.clicked=False
                    for x in range (len(app.autoScheduleTextBox.enterTextBoxes)):
                        app.autoScheduleTextBox.enterTextBoxes[x]=""


                #Next Day button commands        
                elif(self.buttonType=="next"):
                    app.dayOfTheWeek+=1
                    app.dayOfTheWeekString=app.days[(app.dayOfTheWeek)%7]
                    app.currentDay+=1
                    if (app.currentDay>(app.numDaysPerMonth[app.currentMonthInt][1])):
                        #Febuary Exception
                        if(app.currentYear%4==0):
                            app.numDaysPerMonth[1][1]=29
                        else:
                            app.numDaysPerMonth[1][1]=28
                        app.currentDay=app.currentDay%(app.numDaysPerMonth[app.currentMonthInt][1])
                        app.currentMonthInt=(app.currentMonthInt+1)%12
                        app.currentMonthString=app.months[app.currentMonthInt]
                    
                    if (app.currentMonthString=="January") and (app.currentDay==1):
                        app.currentYear+=1
                    
    

                #Previous Day button commands
                elif(self.buttonType=="previous"):
                    app.dayOfTheWeek-=1
                    app.dayOfTheWeekString=app.days[(app.dayOfTheWeek)%7]
                    app.currentDay-=1
                    if (app.currentDay<1):
                        #Febuary Exception
                        if(app.currentYear%4==0):
                            app.numDaysPerMonth[1][1]=29
                        else:
                            app.numDaysPerMonth[1][1]=28
                        app.currentDay=app.numDaysPerMonth[(app.currentMonthInt-1)%12][1]
                        app.currentMonthInt=(app.currentMonthInt-1)%12
                        app.currentMonthString=app.months[app.currentMonthInt]
                    if (app.currentMonthString=="December") and (app.currentDay==31):
                        app.currentYear-=1
                
                #Next Week button commands
                elif(self.buttonType=="nextWeek"):
                    app.dayOfTheWeek+=7
                    app.dayOfTheWeekString=app.days[(app.dayOfTheWeek)%7]
                    app.currentDay+=7

                    if (app.currentDay>(app.numDaysPerMonth[app.currentMonthInt][1])):
                        app.currentDay=app.currentDay%(app.numDaysPerMonth[app.currentMonthInt][1])
                        app.currentMonthInt=(app.currentMonthInt+1)%12
                        app.currentMonthString=app.months[app.currentMonthInt]
                        #Febuary Exception
                        if(app.currentYear%4==0):
                            app.numDaysPerMonth[1][1]=29
                        else:
                            app.numDaysPerMonth[1][1]=28
                    if (app.currentMonthString=="January"):
                        if (app.currentDay>=1) and (app.currentDay<=7):
                            app.currentYear+=1

                
                #Previous Week button commands
                elif(self.buttonType=="previousWeek"):
                    app.dayOfTheWeek-=7
                    app.dayOfTheWeekString=app.days[(app.dayOfTheWeek)%7]
                    app.currentDay-=7
                    if (app.currentDay<1):
                        #Febuary Exception
                        if(app.currentYear%4==0):
                            app.numDaysPerMonth[1][1]=29
                        else:
                            app.numDaysPerMonth[1][1]=28
                        app.currentDay=app.numDaysPerMonth[(app.currentMonthInt-1)%12][1]+app.currentDay
                        app.currentMonthInt=(app.currentMonthInt-1)%12
                        app.currentMonthString=app.months[app.currentMonthInt]

                    if (app.currentMonthString=="December"):
                        if (app.currentDay>=24) and (app.currentDay<=31):
                            app.currentYear-=1
                
                #Confirm Event button commands
                elif(self.buttonType=="confirm"):
                    if (app.clickedPractice==True):
                        event1=app.practiceTextBox.enterTextBoxes[0]
                        event2=app.practiceTextBox.enterTextBoxes[1]
                        if (event2=="12") and (app.startTime==0):
                            event2="0"
                        
                        event3=app.practiceTextBox.enterTextBoxes[2]
                        if (app.calendarMode=="Week"):
                            event4=app.practiceTextBox.enterTextBoxes[3]
                            event5=app.days.index(app.practiceTextBox.enterTextBoxes[3])-app.days.index(app.dayOfTheWeekString)+app.currentDay
                        #Just takes care of cancel case right now
                        if (type(event1)!=str) or (type(int(event2))!=int) or (type(int(event3))!=int):
                            if (app.calendarMode=="Week"):
                                if(type(event4)!=str):
                                    return
                            return
                        i=1
                        while (((event1+str(i)) in app.eventDict)==True):
                            i+=1
                        app.eventDict[event1+str(i)]=list()
                        app.eventDict[event1+str(i)].append(event2)
                        app.eventDict[event1+str(i)].append(event3)
                        if (app.calendarMode=="Week"):
                            app.eventDict[event1+str(i)].append(event4)
                            app.eventDict[event1+str(i)].append(event5)
                        elif (app.calendarMode=="Day"):
                            app.eventDict[event1+str(i)].append(app.dayOfTheWeekString)
                            app.eventDict[event1+str(i)].append(app.currentDay)
                        
                        app.eventList.append(event1+str(i))
                        for x in range (len(app.practiceTextBox.enterTextBoxes)):
                            app.practiceTextBox.enterTextBoxes[x]=""
                        


                        leftXMultiplierWeek=app.days.index(app.eventDict[event1+str(i)][2])
                        rightXMultiplierWeek=leftXMultiplierWeek+1
                        leftXWeek=app.margin+leftXMultiplierWeek*app.spaceBetweenHorizontal
                        rightXWeek=app.margin+rightXMultiplierWeek*app.spaceBetweenHorizontal
                        leftXDay=app.margin+app.width/4
                        rightXDay=app.width/2
                        if (int(app.eventDict[event1+str(i)][0])>int(app.eventDict[event1+str(i)][1])):
                            topY=app.margin+(abs(int(app.eventDict[event1+str(i)][0])-app.startTime)+1
                            )*app.spaceBetweenVertical
                            bottomY=app.margin+(12-int(app.startTime)+int
                            (app.eventDict[event1+str(i)][1])+1)*app.spaceBetweenVertical

                        elif (int(app.eventDict[event1+str(i)][0])>=app.startTime) and (int(app.eventDict[event1+str(i)][0])
            <12):
                            topY=app.margin+(abs(int(app.eventDict[event1+str(i)][0])-app.startTime)+1
                            )*app.spaceBetweenVertical
                            bottomY=app.margin+(abs(int(app.eventDict[event1+str(i)][1])-app.startTime)+1
                            )*app.spaceBetweenVertical
                        
                        elif (int(app.eventDict[event1+str(i)][0])==12):
                                topY=app.margin+(12-app.startTime+1)*app.spaceBetweenVertical
                                difference=(-1*app.startTime)+13
                                bottomY=app.margin+(int(app.eventDict[event1+str(i)][1])+difference
                            )*app.spaceBetweenVertical

                        else:
                            difference=(-1*app.startTime)+13
                            topY=app.margin+(int(app.eventDict[event1+str(i)][0])+difference
                            )*app.spaceBetweenVertical
                            bottomY=app.margin+(int(app.eventDict[event1+str(i)][1])+difference
                            )*app.spaceBetweenVertical
                        app.eventsCoordinates.append((leftXWeek,topY,rightXWeek,bottomY,leftXDay,rightXDay))
                        app.clickedPractice=False
                        app.practiceTextBox.clicked=False

                #Cancel regular event commands
                elif(self.buttonType=="cancel"):
                    app.clickedPractice=False
                    app.practiceTextBox.clicked=False

                    for x in range (len(app.practiceTextBox.enterTextBoxes)):
                        app.practiceTextBox.enterTextBoxes[x]=""

                 #Go to today button commands
                elif(self.buttonType=="goToToday"):
                    app.dayOfTheWeek=(int(datetime.datetime.today().weekday())+1)
                    app.currentDay=int(app.currentDateString[8::])
                    app.currentMonthString=app.numDaysPerMonth[int(app.currentDateString[5:7])-1][0]
                    app.currentMonthInt=app.months.index(app.currentMonthString)
                    app.dayOfTheWeekString=app.days[app.dayOfTheWeek]
                
                elif(self.buttonType=="returnHome"):
                    app.calendarMode="Home"
                
                elif(self.buttonType=="learnMore"):
                    if(app.drawLearnMoreText==True):
                        app.drawLearnMoreText=False
                    elif(app.drawLearnMoreText==False):
                        app.drawLearnMoreText=True
                    
                    

                
                    
        def mousePressedDelete(self,app,event):
            if(app.deleteEventButton.clicked==True):
                for x in range(len(app.eventList)):
                    if(app.calendarMode=="Week"):
                        if (event.x>=app.eventsCoordinates[x][0]) and (event.y>=app.eventsCoordinates[x][1]
                ) and (event.x<=app.eventsCoordinates[x][2]) and (event.y<=app.eventsCoordinates[x][3]):
                                if (len(app.eventDict)!=0):
                                    del app.eventDict[app.eventList[x]] 
                                    app.eventList.remove(app.eventList[x]) 
                                    app.eventsCoordinates.pop(x)
                                    app.deleteEventButton.clicked=False  
                    if(app.calendarMode=="Day"):
                        if (event.x>=app.eventsCoordinates[x][4]) and (event.y>=app.eventsCoordinates[x][1]
                ) and (event.x<=app.eventsCoordinates[x][5]) and (event.y<=app.eventsCoordinates[x][3]):
                                if (len(app.eventDict)!=0):
                                    del app.eventDict[app.eventList[x]]
                                    app.eventList.remove(app.eventList[x]) 
                                    app.eventsCoordinates.pop(x)
                                    app.deleteEventButton.clicked=False 



        def mousePressedEdit(self,app,event):
            if(app.editEventButton.clicked==True):
                for x in range(len(app.eventList)):
                    if(app.calendarMode=="Week"):
                        if (event.x>=app.eventsCoordinates[x][0]) and (event.y>=app.eventsCoordinates[x][1]
                ) and (event.x<=app.eventsCoordinates[x][2]) and (event.y<=app.eventsCoordinates[x][3]):
                                if (len(app.eventDict)!=0):
                                    app.clickedEditEvent=True
                                    app.currentlyEdited=x
                                    
                    if (app.calendarMode=="Day"):
                        if (event.x>=app.eventsCoordinates[x][4]) and (event.y>=app.eventsCoordinates[x][1]
                ) and (event.x<=app.eventsCoordinates[x][5]) and (event.y<=app.eventsCoordinates[x][3]):
                                if (len(app.eventDict)!=0):
                                    app.clickedEditEvent=True
                                    app.currentlyEdited=x
                                    
                                    
                                    

            
        def drawButton(self,app,canvas):
            canvas.create_rectangle(self.center[0]-self.buttonWidth,
            self.center[1]-self.buttonHeight,self.center[0]+self.buttonWidth,
            self.center[1]+self.buttonHeight,fill=self.color)
            canvas.create_text(self.center[0],self.center[1],
            text=self.text,fill="black")
            

class smallButton(Button):
    def __init__(self,app,text,center,color,buttonType):
        super().__init__(app,text,center,color,buttonType)
        self.buttonWidth=0.25*app.spaceBetweenHorizontal
        self.buttonHeight=0.25*app.spaceBetweenVertical

class textBox:
    def __init__(self,app,center,length,questions):
        self.center=(center[0],center[1])
        self.length=length
        self.width=length/2
        self.enterTextBoxes=[]
        self.clicked=False
        self.questions=questions
        self.individualBoxBounds=[]
        for x in range(len(self.questions)):
            #x0,y0,x1,y1
            self.individualBoxBounds.append((self.center[0],(self.center[1]-(self.width/2)+0.25*self.width+(x*25))-10,
            self.center[0]+(self.length/2)-10,(self.center[1]-(self.width/2)+0.25*self.width+(x*25))+10))
        self.boxCurrentlyTyping=0
        

    def keyPressed(self,app,event):
            if (app.practiceTextBox.clicked==True):
                if (event.key=="Space"):
                    app.practiceTextBox.enterTextBoxes[app.practiceTextBox.boxCurrentlyTyping]+=" "
                elif (event.key=="BackSpace"):
                    length=len(app.practiceTextBox.enterTextBoxes[app.practiceTextBox.boxCurrentlyTyping])
                    if (len(app.practiceTextBox.enterTextBoxes[app.practiceTextBox.boxCurrentlyTyping])>0):
                        app.practiceTextBox.enterTextBoxes[app.practiceTextBox.boxCurrentlyTyping]=app.practiceTextBox.enterTextBoxes[app.practiceTextBox.boxCurrentlyTyping][0:length-1]
                elif (event.key=="Return"):
                    app.practiceTextBox.enterTextBoxes[app.practiceTextBox.boxCurrentlyTyping]+="\n"
                elif (ord(event.key)>=33) and (ord(event.key)<=126):
                   app.practiceTextBox.enterTextBoxes[app.practiceTextBox.boxCurrentlyTyping]+=str(event.key)
            
            if (app.autoScheduleTextBox.clicked==True):
                if (event.key=="Space"):
                    app.autoScheduleTextBox.enterTextBoxes[app.autoScheduleTextBox.boxCurrentlyTyping]+=" "
                elif (event.key=="BackSpace"):
                    app.autoScheduleTextBox.enterTextBoxes[app.autoScheduleTextBox.boxCurrentlyTyping]=app.autoScheduleTextBox.enterTextBoxes[app.autoScheduleTextBox.boxCurrentlyTyping][0::-1]
                elif (event.key=="Return"):
                    app.autoScheduleTextBox.enterTextBoxes[app.autoScheduleTextBox.boxCurrentlyTyping]+="\n"
                elif (ord(event.key)>=33) and (ord(event.key)<=126):
                    app.autoScheduleTextBox.enterTextBoxes[app.autoScheduleTextBox.boxCurrentlyTyping]+=str(event.key)

            if (app.editEventTextBox.clicked==True):  
                if (event.key=="Space"):
                    app.editEventTextBox.enterTextBoxes[app.editEventTextBox.boxCurrentlyTyping]+=" "
                elif (event.key=="BackSpace"):
                    app.editEventTextBox.enterTextBoxes[app.editEventTextBox.boxCurrentlyTyping]=app.editEventTextBox.enterTextBoxes[app.editEventTextBox.boxCurrentlyTyping][0::-1]
                elif (event.key=="Return"):
                    app.editEventTextBox.enterTextBoxes[app.editEventTextBox.boxCurrentlyTyping]+="\n"
                elif (ord(event.key)>=33) and (ord(event.key)<=126):
                    app.editEventTextBox.enterTextBoxes[app.editEventTextBox.boxCurrentlyTyping]+=str(event.key)
            
      
        
    def mousePressed(self,app,event):
        if (app.clickedPractice==True):
            for x in range(len(app.practiceTextBox.individualBoxBounds)):
                if (event.x>=app.practiceTextBox.individualBoxBounds[x][0]) and (event.y>=app.practiceTextBox.individualBoxBounds[x][1]
                ) and (event.x<=app.practiceTextBox.individualBoxBounds[x][2]) and (event.y<=app.practiceTextBox.individualBoxBounds[x][3]):
                    app.practiceTextBox.boxCurrentlyTyping=x
                    app.practiceTextBox.clicked=True
        

        if(app.clickedAutoSchedule==True):
            for x in range(len(app.autoScheduleTextBox.individualBoxBounds)):
                if (event.x>=app.autoScheduleTextBox.individualBoxBounds[x][0]) and (event.y>=app.autoScheduleTextBox.individualBoxBounds[x][1]
                ) and (event.x<=app.autoScheduleTextBox.individualBoxBounds[x][2]) and (event.y<=app.autoScheduleTextBox.individualBoxBounds[x][3]):
                    app.autoScheduleTextBox.boxCurrentlyTyping=x
                    app.autoScheduleTextBox.clicked=True

        if(app.clickedEditEvent==True):
            for x in range(len(app.editEventTextBox.individualBoxBounds)):
                if (event.x>=app.editEventTextBox.individualBoxBounds[x][0]) and (event.y>=app.editEventTextBox.individualBoxBounds[x][1]
                ) and (event.x<=app.editEventTextBox.individualBoxBounds[x][2]) and (event.y<=app.editEventTextBox.individualBoxBounds[x][3]):
                    app.editEventTextBox.boxCurrentlyTyping=x
                    app.editEventTextBox.clicked=True
        


    def drawTextBox(self,app,canvas):
        canvas.create_rectangle(self.center[0]-(self.length/2),
        self.center[1]-(self.width/2),
        self.center[0]+(self.length/2),
        self.center[1]+(self.width/2),fill="light yellow")
        i=0
        if (app.calendarMode=="Day") and (self==app.practiceTextBox):
            i=len(self.questions)-1
        else:
            i=len(self.questions)

        for x in range(i):
            canvas.create_text((self.center[0]+0.25*self.length)-(self.length/2),
            (self.center[1]-(self.width/2)+0.25*self.width)+(x*25),text=self.questions[x],
            fill="black")
            self.enterTextBoxes.append("")
            canvas.create_text(self.center[0]+(self.length/2)-100,
            (self.center[1]-(self.width/2)+0.25*self.width)+(x*25),text=self.enterTextBoxes[x],
            fill="black")
            canvas.create_rectangle(self.individualBoxBounds[x][0],self.individualBoxBounds[x][1],
            self.individualBoxBounds[x][2],self.individualBoxBounds[x][3])


        

runApp(width=1000,height=600)
