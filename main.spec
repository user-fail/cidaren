# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_data_files

# 收集spacy数据文件和模型
spacy_data = collect_data_files('spacy', include_py_files=True)
spacy_models = collect_data_files('en_core_web_sm', include_py_files=True)

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[('./config/config.json','config')] + spacy_data+spacy_models,
    hiddenimports=['spacy_legacy','charset_normalizer.md__mypyc'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='github6',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='main',
)
