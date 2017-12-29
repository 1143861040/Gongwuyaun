# Anaconda中Python 第三方库的下载和安装
## 方法一：
1. 进入网站：在网站 https://pypi.python.org/pypi/ 中选择需要下载的第三方库，进入其下载 Downloads 页面。
2. 选择版本：选择与电脑系统和Python版本相对应的版本，下载.whl格式的文件。例如 wxPython-4.0.0b2-cp36-cp36m-win32.whl。
3. 下载路径：安装在Python安装的目录下的Scripts文件夹下。例如 D:\Anaconda3\Scripts\。
4. 开始安装：打开命令行窗口cmd.exe进入下载的文件夹下，输入pip install whl名称.whl。例如 D:\Anaconda3\Scripts>pip install wxPython-4.0.0b2-cp36-             cp36m-win32.whl。
5. 检测安装：在Python命令行下，导入第三方库，不报错即代表安装成功。例如>>>import wx。

WHL文件其实是一个压缩包，其中包含.py文件，以及编译过的pdy文件。

## 方法二：
1. 下载zip文件：例如下载jieba分词的压缩包 https://pypi.python.org/pypi/jieba。
2. 解压路径：将下载文件后的文件夹解压到D:\ProgramData\Anaconda3\Lib\site-packages。
3. 开始安装：在cmd窗口中进入当前文件夹下D:\ProgramData\Anaconda3\Lib\site-packages\jieba>然后执行python setuo.py install.
4. 检测安装：在Python命令行下，导入第三方库，不报错即代表安装成功。例如>>>import wx。
