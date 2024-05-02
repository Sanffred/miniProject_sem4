# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['MainApplication.py'],
    pathex=[],
    binaries=[],
    datas=[('credentials.json', '.'), ('token.json', '.')],

    hiddenimports=[
    'google_auth_oauthlib.flow',
    'googleapiclient.discovery',
    'googleapiclient.errors',
    'googleapiclient.http',
    'google.auth.transport.requests'
    ],

    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['PyQt6', 'PySide6'],
    noarchive=False,
    optimize=0,
    log_level='DEBUG'
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='MainApplication',
    debug=True,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
