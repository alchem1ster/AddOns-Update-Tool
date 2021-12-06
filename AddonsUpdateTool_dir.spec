# -*- mode: python ; coding: utf-8 -*-


block_cipher = None

a = Analysis(['app.py'],
             pathex=[],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
a_pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

a_exe = EXE(a_pyz,
          a.scripts, 
          [],
          exclude_binaries=True,
          name='app',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )

b = Analysis(['game_updater.py'],
             pathex=[],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
b_pyz = PYZ(b.pure, b.zipped_data,
             cipher=block_cipher)

b_exe = EXE(b_pyz,
          b.scripts, 
          [],
          exclude_binaries=True,
          name='game_updater',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )

c = Analysis(['vault_updater.py'],
             pathex=[],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
c_pyz = PYZ(c.pure, c.zipped_data,
             cipher=block_cipher)

c_exe = EXE(c_pyz,
          c.scripts, 
          [],
          exclude_binaries=True,
          name='vault_updater',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )

coll = COLLECT(a_exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               b_exe,
               b.binaries,
               b.zipfiles,
               b.datas, 
               c_exe,
               c.binaries,
               c.zipfiles,
               c.datas, 
               strip=False,
               upx=True,
               upx_exclude=[],
               name='AddOnsUpdateTool')