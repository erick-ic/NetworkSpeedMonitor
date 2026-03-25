from setuptools import setup

APP = ['network_speed_monitor.py']  # 你的脚本名
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'plist': {
        'LSUIElement': True,  # 隐藏Dock图标，只显示菜单栏
        'CFBundleName': '网速监控',  # APP名称
        'CFBundleDisplayName': '网速监控',
        'CFBundleVersion': '1.0',
    },
    'packages': ['rumps', 'psutil'],  # 打包依赖库
    'includes': ['time'],
    'iconfile':'speed_wave.png',  # 应用图标
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)