import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import Image
import ImageDraw
import ImageFont

class Area(object):
	def __init__(self,left,top,right,bottom):
		self.left=left
		self.top=top
		self.right=right
		self.bottom=bottom

class OLED(object):
	'''oled module'''
	def __init__(self,RST,DC,SPI_PORT,SPI_DEVICE):
		self.disp=Adafruit_SSD1306.SSD1306_128_64(rst=RST,dc=DC,spi=SPI.SpiDev(SPI_PORT,SPI_DEVICE,max_speed_hz=8000000))
		self.image=Image.new('1',(self.disp.width,self.disp.height))
		self.draw=ImageDraw.Draw(self.image)
		self.area1=Area(0,0,127,15)
		self.area2=Area(0,16,127,33)
		self.area3=Area(0,31,127,48)
		self.area4=Area(0,46,127,63)
		self.font=ImageFont.truetype('VCR_OSD_MONO_1.001.ttf',15)


	def setup(self):
		self.disp.begin()
		self.disp.clear()
		self.disp.display()
		
	def clearArea1(self):
		self.draw.rectangle((self.area1.left,self.area1.top,self.area1.right,self.area1.bottom),outline=0,fill=0)
		self.disp.image(self.image)
		self.disp.display()
		
	def clearArea2(self):
		self.draw.rectangle((self.area2.left,self.area2.top,self.area2.right,self.area2.bottom),outline=0,fill=0)
		self.disp.image(self.image)
		self.disp.display()
		
	def clearArea3(self):
		self.draw.rectangle((self.area3.left,self.area3.top,self.area3.right,self.area3.bottom),outline=0,fill=0)
		self.disp.image(self.image)
		self.disp.display()
		
	def clearArea4(self):
		self.draw.rectangle((self.area4.left,self.area4.top,self.area4.right,self.area4.bottom),outline=0,fill=0)
		self.disp.image(self.image)
		self.disp.display()
		
	def writeArea1(self,text):
		self.clearArea1()
		self.draw.text((self.area1.left,self.area1.top),text,font=self.font,fill=1)
		self.disp.image(self.image)
		self.disp.display()
		
	def writeArea2(self,text):
		self.clearArea2()
		self.draw.text((self.area2.left,self.area2.top),text,font=self.font,fill=1)
		self.disp.image(self.image)
		self.disp.display()
		
	def writeArea3(self,text):
		self.clearArea3()
		self.draw.text((self.area3.left,self.area3.top),text,font=self.font,fill=1)
		self.disp.image(self.image)
		self.disp.display()
		
	def writeArea4(self,text):
		self.clearArea4()
		self.draw.text((self.area4.left,self.area4.top),text,font=self.font,fill=1)
		self.disp.image(self.image)
		self.disp.display()
		
	def clear(self):
		self.disp.clear()
		self.disp.display()

