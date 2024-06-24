import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QWidget,QLineEdit,QLabel 
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('F5语法校验工具')  # 设置窗口标题
         # 获取脚本文件的目录
        script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
        icon_path = os.path.join(script_dir,'image','f5-logo-rgb.png')  # 确保icon.png文件存在于脚本目录中
        self.setWindowIcon(QIcon(icon_path))  # 设置窗口图标（确保icon.png文件存在）
        self.resize(800, 600)  # 设置窗口大小

        # 创建一个总体的垂直布局
        layout = QVBoxLayout()

        # 添加头部部分布局
        header_layout = self.createHeaderLayout()
        layout.addLayout(header_layout)

        # 添加中间部分布局
        middle_layout = self.createMiddleLayout()
        layout.addLayout(middle_layout)

        # 添加底部部分布局
        bottom_layout = self.createBottomLayout()
        layout.addLayout(bottom_layout)

        # 添加一个伸缩因子，将所有部件推到窗口的顶部和底部
        layout.addStretch()

        # 创建一个中央小部件并将总体布局设置为中央小部件的布局
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # 将窗口居中显示
        self.center()

    def createHeaderLayout(self):
        # 创建一个水平布局用于放置头部部分的控件
        header_layout = QHBoxLayout()

         # 创建一个文本标签
        label = QLabel('请上传变更文件将存储在程序中进行翻译优化后生成对应的配置文件进行加载！')
        header_layout.addWidget(label)

        # 添加上传按钮到头部布局
        button_upload = QPushButton('点击上传', self)
        header_layout.addWidget(button_upload)
        # 添加停止按钮到头部布局
        button_stop = QPushButton('停止运行', self)
        header_layout.addWidget(button_stop)
        header_layout.addStretch() #添加弹簧
        return header_layout

    def createMiddleLayout(self):
        # 创建一个垂直布局用于放置中间部分的内容
        middle_layout = QHBoxLayout()
        input_ip = QLineEdit()
        input_ip.setPlaceholderText('请输入连接f5 mgmt IP地址: 例如:192.168.1.245')
        input_ip.setFixedWidth(300)  # 设置输入框宽度为200像素
        middle_layout.addWidget(input_ip)

        input_port = QLineEdit()
        input_port.setPlaceholderText('22')
        input_port.setFixedWidth(50)  # 设置输入框宽度为200像素
        middle_layout.addWidget(input_port)

        input_user = QLineEdit()
        input_user.setPlaceholderText('user name')
        middle_layout.addWidget(input_user)

        input_passwd = QLineEdit()
        input_passwd.setPlaceholderText('password')
        middle_layout.addWidget(input_passwd)

        connect_button = QPushButton('连接设备',self)
        middle_layout.addWidget(connect_button)
        return middle_layout

    def createBottomLayout(self):
        # 创建一个垂直布局用于放置底部部分的内容
        bottom_layout = QVBoxLayout()
        # 这里可以添加底部部分的控件和布局
        return bottom_layout

    def center(self):
        # 计算并设置窗口在屏幕中的居中位置
        screen_geometry = self.screen().geometry()
        window_geometry = self.geometry()
        x = (screen_geometry.width() - window_geometry.width()) // 2
        y = (screen_geometry.height() - window_geometry.height()) // 2
        self.move(x, y)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
