# -*- mode: python ; coding: utf-8 -*-
import sys
sys.setrecursionlimit(20000) #or more
block_cipher = None


a = Analysis(['test_python.py'],
             pathex=['C:\\Users\\krish\\Documents\\GitHub\\PythonInstallable'],
             binaries=[],#mention the IBM_db.dll location
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='test_python',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
