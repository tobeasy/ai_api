# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['Streamlit_ai.py'],
    pathex=['/Users/tobias/dev/ai_api-1'],
    binaries=[],
    datas=[
        ('/Users/tobias/dev/ai_api-1/venv/lib/python3.12/site-packages/streamlit', 'streamlit'),
        ('/Users/tobias/dev/ai_api-1/venv/lib/python3.12/site-packages/pkg_resources', 'pkg_resources')
    ],
    hiddenimports=[
        'streamlit'
        'pkg_resources',
    ],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='uni_ai_client',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='Streamlit_ai',
)