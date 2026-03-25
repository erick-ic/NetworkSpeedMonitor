# NetworkSpeedMonitor

![alt text](image.png)
*图示：打包后的应用在菜单栏显示*

# 编译流程
```bash
python3 network_speed_monitor.py
```

# 打包流程
## 步骤 1：安装打包工具
```bash
pip3 install py2app
```

## 步骤 2：创建打包配置文件
在代码文件夹下新建 setup.py，复制以下内容：

```python
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
    'iconfile':'speed_wave.png',     # 应用图标
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
```

## 步骤 3：打包成 APP
终端执行（进入代码文件夹后）：
```bash
python3 setup.py py2app -A
``` 

打包完成后，文件夹会生成 dist 目录，里面的 网速监控.app 就是独立应用。

## 步骤 4：一键使用
把 网速监控.app 拖到桌面 / 启动台 / 应用程序文件夹，双击即可运行。
运行后无终端窗口，仅菜单栏显示网速，和原生 macOS 应用完全一致。
