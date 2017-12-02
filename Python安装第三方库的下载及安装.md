# Python 第三方库的下载和安装
## 方法一：
1. 进入网站：在网站 https://pypi.python.org/pypi/ 中选择需要下载的第三方库，进入其下载 Downloads 页面。
2. 选择版本：选择与电脑系统和Python版本相对应的版本，下载.whl格式的文件。例如 wxPython-4.0.0b2-cp36-cp36m-win32.whl。
3. 下载路径：安装在Python安装的目录下的Scripts文件夹下。例如 D:\Anaconda3\Scripts\。
4. 开始安装：打开命令行窗口cmd.exe进入下载的文件夹下，输入pip install whl名称.whl。例如 D:\Anaconda3\Scripts>pip install wxPython-4.0.0b2-cp36-             cp36m-win32.whl。
5. 检测安装：在Python命令行下，导入第三方库，不报错即代表安装成功。例如>>>import wx。

WHL文件其实是一个压缩包，其中包含.py文件，以及编译过的pdy文件。
