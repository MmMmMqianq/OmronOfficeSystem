"""

用Web浏览器控件（QWebEngineView）显示网页

PyQt5和Web的交互计数

同时使用Python和Web开发程序，混合开发

Python+JavaScript+HTML5+CSS

"""
import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton, QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl


class WebEngine(QWidget):
    def __init__(self):
        super(WebEngine, self).__init__()

        self.setWindowTitle("用QWebEngineView实例")
        self.resize(1200, 800)

        self.web1 = QWebEngineView()
        self.web2 = QWebEngineView()
        self.web3 = QWebEngineView()
        self.web4 = QWebEngineView()

        self.button = QPushButton("确定")
        self.vLayout = QVBoxLayout()
        self.vLayout.addWidget(self.web4)
        self.vLayout.addWidget(self.button)

        self.hLayout = QHBoxLayout(self)
        self.hLayout.addWidget(self.web1)
        self.hLayout.addWidget(self.web2)
        self.hLayout.addWidget(self.web3)
        self.hLayout.addLayout(self.vLayout)

        # 1. 打开外部页面
        self.web1.load(QUrl("https://www.baidu.com/"))

        # 2. 加载本地HTML页面
        url = os.getcwd() + "/LocalHTML.html"
        self.web2.load(QUrl.fromLocalFile(url))

        # 3. 显示内部的HTML页面
        html = """
        <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>测试页面</title>
</head>
<body>
    <h1>Hello PyQt5</h1>
    <h2>Hello PyQt5</h2>
    <h3>Hello PyQt5</h3>
    <h4>Hello PyQt5</h4>
</body>
</html>
        """
        self.web3.setHtml(html)

        # 4. 调用JavaScript
        urlJavaScript = os.getcwd() + "/JavaScriptPage.html"
        self.web4.load(QUrl.fromLocalFile(urlJavaScript))

        self.button.clicked.connect(self.fullName)

    def js_callback(self, result):
        print(result)

    def fullName(self):
        self.value = "下面将进行全名操作喽"
        self.web4.page().runJavaScript('fullname("' + self.value + '");', self.js_callback)  # 调用JavaScript函数fullname("' + self.value + '")，
                                                                                             # 括号里的是给函数赋值也就是Python给JavaScript传参数，
                                                                                             # 返回值通过回掉函数self.js_callback传给Python


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WebEngine()
    window.show()
    sys.exit(app.exec_())
