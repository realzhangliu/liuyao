#coding=utf-8
from liuyaodata import *
from Tkinter import *
from ttk import *
cntoint={u'少阳-----':'1',u'少阴-- --':'2',u'老阳--O--':'3',u'老阴--X--':'4'}
gua=[]
guax=200
guay=100
def paipan():
	global gua
	for i in xrange(6):
		gua.append(cntoint[com[i].get()])
	guastr=''.join(gua)
	print guastr
	# print gua64[guastr]
	draw(gua,guastr)

def draw(gua,guastr):
	for i in xrange(6):
		if gua[i]==1:
			canvas.create_image(guax,100+30*i,image=picyang)
		else:
			canvas.create_image(guax,100+30*i,image=picyin)
	for i in xrange(6):
		canvas.create_text(guax-60,100+30*i,text=gua64[guastr][i])
	gua=[]
	guastr=''

root=Tk()
root.title(u'===[六爻排盘===淮南内部专用]')
root.minsize(550,380)
root.maxsize(550,380)
canvas=Canvas(root,width=460,height=380,bg='gray')
picyang=PhotoImage(file='tk\\yang.gif')
picyin=PhotoImage(file='tk\\yin.gif')
canvas.place(relx=0,rely=0)
com={}
for i in xrange(6):
	com[i]=Combobox(root,state='readonly')
	com[i]['values']=(u'少阳-----',u'少阴-- --',u'老阳--O--',u'老阴--X--')
	com[i].current(0)
	com[i].place(relx=0.85,rely=0.07*i,width=80)
bt1=Button(root,text=u'排盘',command=paipan)
# bt1.place(relx=0.85,rely=0.35+0.7)
bt1.pack(side='right')
root.mainloop()
# canvas.create_image(150,100,image=picyang)
# canvas.create_text(150-60,100,text='官子水')
# canvas.create_image(150,100+30,image=picyin)
# canvas.create_image(150,100+60,image=picyin)
# canvas.create_image(150,100+90,image=picyin)
# canvas.create_image(150,100+120,image=picyin)
# canvas.create_image(150,100+150,image=picyin)
# canvas.pack(side='left')