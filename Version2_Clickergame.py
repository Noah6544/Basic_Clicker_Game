from tkinter import *
import time

root = Tk()



class Click():
    def __init__(self,Dollars,CPS,Manualclickrate,Clickupgradestate,CPSupgradestate):
        self.Dollars = 0
        self.Manualclickrate = 1
        self.CPS = 0
        self.Clickupgradestate = 0
        self.CPSupgradestate = 0

ClickObject = Click(0,1,0,0,0)


###FUNCTIONS
def displayclick():
    global ClickObject
    Moneylabel = Label(root,text="You have ${} total".format(str(ClickObject.Dollars)))
    CPSLabel = Label(root,text="You have ${} of autoclicker".format(str(ClickObject.CPS)))
    MoneyperclickLabel = Label(root,text="You are making ${} per click".format(str(ClickObject.Manualclickrate)))
    Moneylabel.grid(row=1,column=0)
    CPSLabel.grid(row=2,column=0)
    MoneyperclickLabel.grid(row=3,column=0)

###CLICK UPGRADES
def firstclickupgrade():
    global ClickObject
    ClickObject.Dollars = ClickObject.Dollars-50
    displayclick()
    ClickObject.Manualclickrate += 2
    ClickObject.Clickupgradestate = 1

def secondclickupgrade():
    global ClickObject
    ClickObject.Dollars = ClickObject.Dollars - 150
    ClickObject.Manualclickrate += 10
    ClickObject.Clickupgradestate = 2
    displayclick()

###CPS UPGRADES

def firstcpsupgrade():
    global ClickObject
    ClickObject.Dollars = ClickObject.Dollars - 3000
    ClickObject.CPS += 5
    displayclick()

#ToDo get this function working in correlation with the FirstClickupgrade variable and the Newupgrade funcion. There are too many bugs with this funtion currently and it is only to make the code cleaner.
"""
def clickupgrade(manualclickrateincrease,cost,upgradestate):
    global ClickObject
    ClickObject.Dollars = ClickObject.Dollars - cost
    displayclick()
    ClickObject.Manualclickrate += manualclickrateincrease
    ClickObject.upgradestate = upgradestate
    displayclick()
FirstClickupgrade = clickupgrade(2,50,1)

"""

def CPS():
    global ClickObject
    global CPS
    ClickObject.Dollars += ClickObject.CPS
    root.after(1000,CPS)
    displayclick()

def Newclickupgrade(text, minmoney, Clickupgradestate, row, column, command):
    global ClickObject
    displayclick()
    if ClickObject.Dollars >= minmoney and ClickObject.Clickupgradestate == Clickupgradestate and (ClickObject.Dollars - minmoney) >= 0:
        upgradebutton = Button(root,text=str(text), command=command)
        upgradebutton.grid(row=row, column=column)
    elif ClickObject.Dollars < minmoney and ClickObject.Clickupgradestate == Clickupgradestate:
        upgradebutton = Button(root, text=str(text), state=DISABLED)
        upgradebutton.grid(row=row,column=column)
    elif ClickObject.Clickupgradestate >= Clickupgradestate:
        upgradebutton = Button(root,text="(ALREADY PURCHASED)\n" + str(text),state=DISABLED)
        upgradebutton.grid(row=row,column=column)

def NewCPSupgrade(text, minmoney ,CPSupgradestate,row,column,command):
    global ClickObject
    displayclick()
    if ClickObject.Dollars >= minmoney and ClickObject.CPSupgradestate == CPSupgradestate and (ClickObject.Dollars - 50) > 0:
        upgradebutton = Button(root,text=str(text), command=command)
        upgradebutton.grid(row=row, column=column)
    elif ClickObject.Dollars < minmoney and ClickObject.CPSupgradestate == CPSupgradestate:
        upgradebutton = Button(root, text=str(text), state=DISABLED)
        upgradebutton.grid(row=row,column=column)
    elif ClickObject.CPSupgradestate >= CPSupgradestate:
        upgradebutton = Button(root,text="(ALREADY PURCHASED)\n" + str(text),state=DISABLED)
        upgradebutton.grid(row=row,column=column)


def basicclick():
    global root
    global ClickObject
    ClickObject.Dollars += ClickObject.Manualclickrate
    displayclick()
    Newclickupgrade("Buy +$10 per click\nCOST: $500",500,1,5,0,secondclickupgrade)

    Newclickupgrade("Buy +$2 per click\nCOST: $50",50,0,4,0,firstclickupgrade)
    NewCPSupgrade("But +5 per second\nCOST: $3000",3000,1,6,0,firstcpsupgrade)

"""
    if ClickObject.Dollars >= 50 and ClickObject.upgradestate == 0:
        upgradebutton1 = Button(root, text="Upgrade to $2 per click for $50", command=firstclickupgrade)
        upgradebutton1.grid(row=3, column=0)
    elif ClickObject.Dollars < 50 and ClickObject.upgradestate == 0:
        upgradebutton1 = Button(root, text="Upgrade to $2 per click for $50", state=DISABLED)
        upgradebutton1.grid(row=3,column=0)
    elif ClickObject.upgradestate >= 1:
        upgradebutton1 = Button(root, text="(ALREADY PURCHASED)Upgrade to $2 per click for $50", state=DISABLED)
        upgradebutton1.grid(row=3,column=0)
"""

mainbutton = Button(root, text="Click", command=basicclick, padx=50,pady=50,borderwidth="15", bg="blue",fg="black")
CPS()
time.sleep(.1)



mainbutton.grid(row=0,column=0)

root.mainloop()
