""" Manages the emulation of the Game Boy Color """
import constants as const


class GBC():
	""" Virtual Machine emulating a Game Boy Color """
	def __init__(self,screen):
		self.buttonA=0
		self.buttonB=0
		self.buttonStart=0 
		self.buttonSelect=0
		self.screen=screen
		#self.adresses=[0]*65536
		self.registers={"A":[0]*8,"B":[0]*8,"C":[0]*8,"D":[0]*8,"E":[0]*8,
		"F":[0]*8,"H":[0]*8,"L":[0]*8,"PC":[0]*16,"SP":[0]*16}
		#NOP LD 

class Screen():
	""" Screen of a Game Boy Color """
	def __init__(self,size,**kwargs):
		"""super(Screen,self).__init__(**kwargs)
		self.size=size
		self.pixels=[Pixel((x*const.SIZE_PIXEL,y*const.SIZE_PIXEL)) for x in range(size[0])
		 for y in range(size[1])]
		for pixel in self.pixels:
			self.add_widget(pixel)"""

class Pixel():
	""" Pixel of the Game Boy Color screen """
	def __init__(self,position,**kwargs):
		"""super(Pixel, self).__init__(**kwargs)
		self.position=position #tuple of coordinates (x,y)
		with self.canvas:
			if not position[0]%(position[1]+1):
				Color(0,0,0,1)
				self.color="black"
			else:
				Color(1,1,1,1)
				self.color="white"
			self.border=Rectangle(pos=self.position,size=(const.SIZE_PIXEL,const.SIZE_PIXEL))"""



		
		
		