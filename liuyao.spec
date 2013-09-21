# -*- mode: python -*-
a = Analysis(['liuyao.py'],
             pathex=['E:\\Codes\\liuyao'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='liuyao.exe',
          debug=False,
          strip=None,
          upx=True,
          console=False , icon='f3.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=None,
               upx=True,
               name='liuyao')
