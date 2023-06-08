import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt




class LockScreenWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("锁屏工具")
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)  # 隐藏标题栏、边框并置顶显示
        self.showFullScreen()  # 全屏化

        background_label = QLabel(self)
        pixmap = QPixmap("wallhaven-gppgzd.png")  # 替换为实际的背景图片路径
        background_label.setPixmap(pixmap)
        background_label.setScaledContents(True)

        password_label = QLabel("请输入密码：\n请联系陈安帮", self)
        password_label.setFont(QFont("Arial", 18))
        password_label.setAlignment(Qt.AlignCenter)

        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)

        unlock_button = QPushButton("解锁", self)
        unlock_button.clicked.connect(self.unlock_screen)

        layout = QVBoxLayout(self)
        layout.addWidget(background_label, stretch=1)
        layout.addWidget(password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(unlock_button)
        self.setLayout(layout)

    def unlock_screen(self):
        password = self.password_input.text()
        # 在这里进行密码验证的逻辑判断
        if password == "111":  # 替换为实际的密码
            self.close()
        else:
            self.password_input.clear()
            self.password_input.setFocus()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LockScreenWindow()
    window.show()
    sys.exit(app.exec_())
