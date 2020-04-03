import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class FirstMainWin(QMainWindow):
    def __init__(self,parent=None):
        super(FirstMainWin,self).__init__(parent)

        self.setWindowTitle("双端同步备忘录系统")
        self.setStyleSheet('QMainWindow{border-image:url(c:/picture/w.png)}')
        self.resize(300,500)
        self.initUI()

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        newLeft = (screen.width()-size.width())/2
        newRight = (screen.height() - size.height()) / 2
        self.move(newLeft,newRight)

    def initUI(self):
        label1 = QLabel(self)
        label1.setText('账号')
        label1.setStyleSheet("font-size:20px;")
        label1.move(70,100)

        edit1 = QTextEdit(self)
        edit1.move(120,100)

        label2 = QLabel(self)
        label2.setText('密码')
        label2.setStyleSheet("font-size:20px;")
        label2.move(70, 200)

        edit1 = QTextEdit(self)
        edit1.move(120, 200)

        label3 = QLabel(self)
        label3.setText('登陆')
        label3.setStyleSheet("font-size:20px;")
        label3.move(130, 350)

class SecondMainWin(QDialog):
    def __init__(self,parent=None):
        super(SecondMainWin,self).__init__(parent)

        self.setWindowTitle("双端同步备忘录系统")
        self.resize(400,300)
        self.login()

    def login(self):

        label01 = QLabel(self)
        label01.setText("登陆成功")



#if __name__ == '__main__':

app = QApplication(sys.argv)
app.setWindowIcon(QIcon('1.png'))
main = FirstMainWin()
second = SecondMainWin()
main.show()

sys.exit(app.exec_())


