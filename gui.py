""" Defines the GUI of the application """ 
import gbc
from tkinter import *
from constants import *

def loadGame():
	""" Load a game which the ROM is stored in the emulator """
	print("load")
def saveGame():
	""" Save a game in the emulator """
	print("save")
def uploadROM():
	""" Upload a ROM file of a GBC game in the emulator """
	print("rom")
def changeParameters():
	""" Open a window to modify the parameters like controls """
	pass

def makeGUI():
	""" Manages the GUI of the application """
	root=Tk()
	root.geometry(f"{SIZE_WINDOW[0]}x{SIZE_WINDOW[1]}+100+200")
	root["bg"]="chocolate"
	root.title("Emulator GBC")
	sound=IntVar(0)
	gb=Canvas(root,bg="#008b8b",width=SIZE_GBC[0],height=SIZE_GBC[1])
	gb.place(x=POS_GBC[0],y=POS_GBC[1])
	gb.create_rectangle(20,15,SIZE_GBC[0]-20,380,fill="black")
	gb.create_rectangle(50,35,SIZE_GBC[0]-50,350,fill="grey")
	gb.create_text(SIZE_GBC[0]/2-30,370,text="GAME BOY ",fill="grey",font="Helvetica 15 bold italic")
	colors=[("C","red"),("O","purple"),("L","green"),("O","yellow"),("R","blue")]
	for i,(letter,color) in enumerate(colors):
		gb.create_text(SIZE_GBC[0]/2+(i*15)+40,370,text=letter,fill=color,
			font="Helvetica 15 bold italic")
	gb.create_oval(25,100,40,115,fill="red")
	#cross
	gb.create_rectangle(SIZE_GBC[0]/5,SIZE_GBC[1]/2+80,SIZE_GBC[0]/4,
		SIZE_GBC[1]/2+200,fill="black")
	gb.create_rectangle(SIZE_GBC[0]/5-50,SIZE_GBC[1]/2+124,SIZE_GBC[0]/4+50,
		SIZE_GBC[1]/2+156,fill="black")
	#A and B buttons
	gb.create_oval(SIZE_GBC[0]-100,SIZE_GBC[1]/2+100,SIZE_GBC[0]-40,
		SIZE_GBC[1]/2+170,fill="black")
	gb.create_oval(SIZE_GBC[0]-185,SIZE_GBC[1]/2+140,SIZE_GBC[0]-120,
		SIZE_GBC[1]/2+210,fill="black")
	gb.create_text(SIZE_GBC[0]-70,SIZE_GBC[1]/2+133,text="A",fill="grey",
			font="Helvetica 30 bold")
	gb.create_text(SIZE_GBC[0]-150,SIZE_GBC[1]/2+175,text="B",fill="grey",
			font="Helvetica 30 bold")
	#start and select buttons
	gb.create_rectangle(SIZE_GBC[0]/2-70,SIZE_GBC[1]-100,SIZE_GBC[0]/2-10,
		SIZE_GBC[1]-80,fill="black")
	gb.create_rectangle(SIZE_GBC[0]/2+10,SIZE_GBC[1]-100,SIZE_GBC[0]/2+70,
		SIZE_GBC[1]-80,fill="black")
	gb.create_arc(20,350,SIZE_GBC[0],350,fill="black",start=180,extent=180)
	#menu containing buttons to load a game,save...
	menu=Frame(root,bg="grey",width=200)
	dataButtons=[("Charger 1 jeu",loadGame),("Sauvegarder",saveGame),
	("Ajouter 1 ROM",uploadROM),("Paramètres",changeParameters)]
	for text,function in dataButtons:
		Button(menu,text=text,command=function,bg="#DAA520",fg="white").pack(fill=X)
	menu.place(x=POS_GBC[0]+SIZE_GBC[0]+10,y=100)
	scaleSound=Scale(root,variable=sound)
	scaleSound.place(x=100,y=50)
	root.mainloop()

