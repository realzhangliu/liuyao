#-*- coding:utf-8 -*-
from distutils.core import setup
import glob
import py2exe,sys,os
 
options = {"py2exe":
           {"dll_excludes": ["MSVCP90.dll"],
            "compressed": 1, #压缩
            "optimize": 2,
            #"ascii": 1,
            #"includes":includes,
            #"bundle_files": 1 #所有文件打包成一个exe文件 }
            }
           }
'''
setup(windows=[{"script": "nliuyao.py","icon_resources": [(1,"f1.ico")]}],
      #console
      options=options,
      zipfile=None,#不生成library.zip文件
 
      )
'''
setup(version = "0.1.0", 
      options = {"py2exe" :
          {"bundle_files": 1, }},  #表示把所有的文件打包成唯一一个.exe
      zipfile = None, 
      windows=[{"script" : "nliuyao.py", "icon_resources" : [(1, "f1.ico")]}])
#图标f1.ico
