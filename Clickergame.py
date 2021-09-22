from tkinter import *
import time

root = Tk()



class Click():
    def __init__(self,Dollars,CPS,Manualclickrate,upgradestate):
        self.Dollars = 0
        self.Manualclickrate = 1
        self.CPS = 15
        self.upgradestate = 0

ClickObject = Click(0,1,0,0)
###FUNCTIONS
def displayclick():
    Moneylabel = Label(root,text="You have $" + str(ClickObject.Dollars))
    Moneylabel.grid(row=1,column=0)

def firstclickupgrade():
    global ClickObject
    ClickObject.Dollars = ClickObject.Dollars-50
    displayclick()
    ClickObject.Manualclickrate += 2
    ClickObject.upgradestate = 1

def firstcpsupgrade():
    global ClickObject
    ClickObject.CPS = 2

def CPS():
    global ClickObject
    ClickObject.Dollars += ClickObject.CPS
    displayclick()

def Newupgrade(text,minmoney,upgradestate,row,column,CPS,Dollars,Manualclick,command):
    global ClickObject
    if ClickObject.Dollars >= minmoney and ClickObject.upgradestate == upgradestate:
        upgradebutton = Button(root,text=str(text), command=command)
        upgradebutton.grid(row=row, column=column)
    elif ClickObject.Dollars < minmoney and ClickObject.upgradestate == upgradestate:
        upgradestate

#TODO finishthe newupgrade function to simpify the creation of iupgrades

def basicclick():
    global ClickObject
    ClickObject.Dollars += ClickObject.Manualclickrate
    #CPS()
    displayclick()
    if ClickObject.Dollars >= 50 and ClickObject.upgradestate == 0:
        upgradebutton1 = Button(root, text="Upgrade to $2 per click for $50", command=firstclickupgrade)
        upgradebutton1.grid(row=2, column=0)
    elif ClickObject.Dollars < 50 and ClickObject.upgradestate == 0:
        upgradebutton1 = Button(root, text="Upgrade to $2 per click for $50", state=DISABLED)
        upgradebutton1.grid(row=2,column=0)
    elif ClickObject.upgradestate >= 1:
        upgradebutton1 = Button(root, text="(ALREADY PURCHASED)Upgrade to $2 per click for $50", command=firstclickupgrade, state=DISABLED)
        upgradebutton1.grid(row=2,column=0)

mainbutton = Button(root, text="Click", command=basicclick, padx=50,pady=50)



mainbutton.grid(row=0,column=0)


root.mainloop()
