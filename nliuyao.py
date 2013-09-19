#coding=utf-8
from liuyaodata import gua64
from Tkinter import *
from ttk import *
from bs4 import BeautifulSoup
import tkFont
import urllib2

class liuyao:
	def __init__(self,root,gua64):
		self.cntoint={u'少阳-----':'1',u'少阴-- --':'2',u'老阳--O--':'3',u'老阴--X--':'4'}
		self.tfont=tkFont.Font(family='Fixdsys',size=25,weight=tkFont.BOLD)
		self.gfont=tkFont.Font(family='Fixdsys',size=13,weight=tkFont.BOLD)
		self.dgua=[] #动爻
		self.ygua=[] #原始卦
		self.bbgua=[] #变卦
		self.yguastr=[] #原始卦
		self.gua=[] #只有12的卦
		self.pabout=True #右键显示消失淮南标题
		self.guax=200
		self.guay=100
		self.liushen={'甲':0,'乙':0,'丙':1,'丁':1,'戊':2,'己':3,'庚':4,'辛':4,'壬':5,'癸':5}
		self.liushencn=['青龙','朱雀','勾陈','腾蛇','白虎','玄武']
		self.tiangan={'甲':1,'乙':2,'丙':3,'丁':4,'戊':5,'己':6,'庚':7,'辛':8,'壬':9,'癸':10}
		self.dizhi={'子':1,'丑':2,'寅':3,'卯':4,'辰':5,'巳':6,'午':7,'未':8,'申':9,'酉':10,'戌':11,'亥':12}
		self.kongwangzu=['子','丑','寅','卯','辰','巳','午','未','申','酉','戌','亥']
		self.root=root
		self.root.title(u'===六爻排盘===[淮南内部专用]')
		self.root.minsize(550,380)
		self.root.maxsize(550,380)
		self.canvas=Canvas(root,width=460,height=380,bg='gray')
		self.picyang=PhotoImage(file='tk\\yang.gif')
		self.picyin=PhotoImage(file='tk\\yin.gif')
		self.canvas.place(relx=0,rely=0)
		self.com={}
		for i in xrange(6):
			self.com[i]=Combobox(root,state='readonly')
			self.com[i]['values']=(u'少阳-----',u'少阴-- --',u'老阳--O--',u'老阴--X--')
			self.com[i].current(0)
			self.com[i].place(relx=0.85,rely=0.36-0.07*i,width=80)
		bt1=Button(root,text=u'排盘',command=self.paipan)
		# bt1.place(relx=0.85,rely=0.35+0.7)
		bt1.pack(side='right')
		self.date() #干支
		#===========================
		self.root.bind('<Button-3>',self.about)

	def liushenf(self):  #配六神
		xu=self.liushen[self.ritian.encode('utf-8')]
		for i in xrange(6):
			self.canvas.create_text(self.guax-170,100+150-30*i,font=self.gfont,text=self.liushencn[xu],tag='liushen')
			xu+=1
			if xu>5:
				xu-=6

	def date(self):
		turl=urllib2.urlopen('http://www.nongli.com/item4/index.asp',timeout=10).read()
		soup=BeautifulSoup(turl)
		zu=soup.findAll('td',{'width':'74%','bgcolor':'#FFFFFF'})[1].text
		# print zu
		wanzu=[] #wanzu里面是完成的年月日干支
		wanzu.append(zu.split(' ')[0])
		wanzu.append(zu.split(' ')[2])
		wanzu.append(zu.split(' ')[3])
		for i in xrange(3):
			# print u'干支',wanzu[i]
			self.canvas.create_text(self.guax-90+60*i,30,text=wanzu[i],font=self.gfont,tag='riqi')
		ri=wanzu[2]
		self.ritian=list(ri)[0]
		self.ridi=list(ri)[1]
		self.kongwang()

	def kongwang(self):
		print u'日干支：',self.ridi,self.ritian
		cha=self.dizhi[self.ridi.encode('utf-8')]-self.tiangan[self.ritian.encode('utf-8')]
		if cha<0:
			cha+=+10
		self.canvas.create_text(self.guax-90+120+30,30,font=self.gfont,text='(',tag='riqi')
		self.canvas.create_text(self.guax-90+120+30+15,30,font=self.gfont,text=self.kongwangzu[cha-2],tag='riqi')
		self.canvas.create_text(self.guax-90+120+30+30,30,font=self.gfont,text=self.kongwangzu[cha-1],tag='riqi')
		self.canvas.create_text(self.guax-90+120+30+45,30,font=self.gfont,text=')',tag='riqi')

	def about(self,event):
		if self.pabout:
			self.canvas.create_text(self.guax,100+250,text='淮南法教专用水印',fill='tan',font=self.tfont,tag='about')
			self.canvas.create_text(self.guax+140,370,text='--无名',fill='tan',tag='about')
			self.pabout=False
		else:
			self.canvas.delete('about')
			self.pabout=True


	def paipan(self):
		for i in xrange(6):
			self.ygua.append(self.cntoint[self.com[i].get()]) #得到原始爻名，转换为1234，添加入gua
		self.gua=self.ygua
		bbgua=self.gua
		print '======================='
		print 'sel.gua',self.gua
		for i in xrange(6):
			if self.ygua[i]=='3':
				self.gua[i]='1'
				self.dgua.append(str(i))
				self.dgua.append('1') 
			elif  self.ygua[i]=='4':
				self.gua[i]='2'
				self.dgua.append(str(i))
				self.dgua.append('2')
		self.guastr=''.join(self.gua)
		# print u'变卦',bbgua
		print u'字符串卦数',self.guastr
		print u'数列卦',self.gua
		print u'动卦',self.dgua
		# print gua64[guastr]
		self.draw()
		self.liushenf()#六神


	def draw(self):
		self.canvas.delete('pic')   #删除所有上次产生的ITEMS
		self.canvas.delete('liushen')
		print u'当前itme数',self.canvas.find_all()
		#本卦
		for i in xrange(6):
			if self.gua[i]=='1':
				self.canvas.create_image(self.guax,100+150-30*i,image=self.picyang,tag='pic')
			else:
				self.canvas.create_image(self.guax,100+150-30*i,image=self.picyin,tag='pic')	
		
				#下面是六亲
		for i in xrange(6):
			self.canvas.create_text(self.guax-70,100+30*i,font=self.gfont,text=gua64[self.guastr][i],tag='pic')

			#动爻标记
		for i in xrange(0,len(self.dgua),2):
			if self.dgua[i+1]=='1':
				self.canvas.create_text(self.guax+70,250-30*int(self.dgua[i]),font=self.gfont,text='O',tag='pic')
			else:
				self.canvas.create_text(self.guax+70,250-30*int(self.dgua[i]),font=self.gfont,text='X',tag='pic')
			#世
		syw=gua64[self.guastr][6]
		self.canvas.create_text(self.guax+55,280-30*syw,font=self.gfont,text='世',tag='pic')
			#应
		yyw=gua64[self.guastr][7]
		self.canvas.create_text(self.guax+55,280-30*yyw,font=self.gfont,text='应',tag='pic')
			#六合、冲
		hc=gua64[self.guastr][8]
		self.canvas.create_text(self.guax-70,100-30,font=self.gfont,text=hc,tag='pic')
			#游魂、归魂
		zg=gua64[self.guastr][9]
		self.canvas.create_text(self.guax-70,100-30,font=self.gfont,text=zg,tag='pic')
			#卦宫
		gg=gua64[self.guastr][10]
		self.canvas.create_text(self.guax,100-30,font=self.gfont,text=gg,tag='pic')
		#变卦	
		self.biangua()
		self.guastr=''
		self.dgua=[] #动爻
		self.ygua=[] #原始卦
		self.bbgua=[] #变卦
		self.yguastr=[] #原始卦
		self.gua=[] #只有12的卦

	def biangua(self):
		self.bbgua=self.gua
		# print 'biangua',self.bbgua
		'''
sel.gua ['4', '4', '3', '3', '4', '3']
字符串卦数 221121
数列卦 ['2', '2', '1', '1', '2', '1']
动卦 ['0', '2', '1', '2', '2', '1', '3', '1', '4', '2', '5', '1']
当前itme数 (1, 2, 3, 4, 5, 6, 7)
biangua ['1', '1', '2', '2', '1', '2']
bguastr 112212
		'''
		for i in xrange(0,len(self.dgua),2):
			if self.dgua[i+1]=='1':
				self.bbgua[int(self.dgua[i])]='2'
			else:
				self.bbgua[int(self.dgua[i])]='1'
		print 'biangua',self.bbgua
		self.bguastr=''.join(self.bbgua)
		print 'bguastr',self.bguastr
		for i in xrange(6):
			if self.bbgua[i]=='1':
				self.canvas.create_image(self.guax+130,100+150-30*i,image=self.picyang,tag='pic')
			else:
				self.canvas.create_image(self.guax+130,100+150-30*i,image=self.picyin,tag='pic')
						#下面是六亲
		for i in xrange(6):
			self.canvas.create_text(self.guax+200,100+30*i,font=self.gfont,text=gua64[self.bguastr][i],tag='pic')


win=Tk()
wapp=liuyao(win,gua64)
win.mainloop()