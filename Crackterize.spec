# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['splash_screen.py'],
    pathex=['.'],
    binaries=[],
    datas=[(C:\Users\Jayvee\PycharmProjects\Crackterize\add_details_of_cracks.py, '.')],
    hiddenimports=['tensorflow.python._pywrap_tensorflow_internal'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
for i in range(len(a.binaries)):
  dest, origin, kind = a.binaries[i]
  if '_pywrap_tensorflow_internal' in dest:
    a.binaries[i] = ('tensorflow.python.' + dest, origin, kind)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='Crackterize',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='Crackterize',
)
