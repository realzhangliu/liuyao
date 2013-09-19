#coding:utf-8
from Tkinter import *
import tkMessageBox
import time
from bs4 import BeautifulSoup
import urllib,urllib2


tiangan={'甲':1,'乙':2,'丙':3,'丁':4,'戊':5,'己':6,'庚':7,'辛':8,'壬':9,'癸':10}
dizhi={'子':1,'丑':2,'寅':3,'卯':4,'辰':5,'巳':6,'午':7,'未':8,'申':9,'酉':10,'戌':11,'亥':12}
a='亥'
b='丁'
print dizhi[a]-tiangan[b]
