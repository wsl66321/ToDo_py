import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class FirstMainWin(QMainWindow):
    def __init__(self, parent=None):
        super(FirstMainWin, self).__init__(parent)

        self.setWindowTitle("双端同步备忘录系统")
        self.setStyleSheet('QMainWindow{border-image:url(res/registerbg.png)}')
        self.resize(360, 640)
        self.setMinimumSize(360, 640)
        self.setMaximumSize(360, 640)
        self.initUI()

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        newLeft = (screen.width() - size.width()) / 2
        newRight = (screen.height() - size.height()) / 2
        self.move(newLeft, newRight)

    def initUI(self):
        # label1 = QLabel(self)
        # label1.setText('账号')
        # label1.setStyleSheet("font-size:20px;")
        # label1.move(70,100)

        image = QLabel(self)
        image.setPixmap(QPixmap("./res/user.png"))
        image.resize(80, 80)
        image.move(140, 100)

        edit1 = QLineEdit(self)
        edit1.setPlaceholderText("账号")
        edit1.move(70, 240)
        edit1.setMinimumWidth(220)
        edit1.setMaxLength(20)


        edit2 = QLineEdit(self)
        edit2.setMinimumWidth(220)
        edit2.move(70, 290)
        edit2.setPlaceholderText("密码")
        edit2.setMaxLength(20)
        edit2.setEchoMode(QLineEdit.Password)


        edit3 = QLineEdit(self)
        edit3.setMinimumWidth(220)
        edit3.move(70, 340)
        edit3.setPlaceholderText("确认密码")
        edit3.setMaxLength(20)
        edit3.setEchoMode(QLineEdit.Password)


        label3 = QLabel(self)
        label3.setText('注册')
        label3.setStyleSheet("font-size:40px;color:#fff")
        label3.resize(80, 40)
        label3.move(140, 400)


        label4 = QLabel(self)
        label4.setText('登录')
        label4.setStyleSheet("font-size:26px;color:#fff")
        label4.resize(56, 28)
        label4.move(296, 602)


class SecondMainWin(QDialog):
    def __init__(self, parent=None):
        super(SecondMainWin, self).__init__(parent)

        self.setWindowTitle("双端同步备忘录系统")
        self.resize(400, 300)
        self.login()

    def login(self):
        label01 = QLabel(self)
        label01.setText("登陆成功")


# if __name__ == '__main__':

app = QApplication(sys.argv)
app.setWindowIcon(QIcon('res/icon.png'))
main = FirstMainWin()
second = SecondMainWin()
main.show()

sys.exit(app.exec_())
