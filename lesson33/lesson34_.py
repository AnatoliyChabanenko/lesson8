import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QPushButton
import calk22



class ExampleApp(QtWidgets.QMainWindow, calk22.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("калькулятор ")
        self.UiComponents()
        self.show()




    def UiComponents(self):
        self.label = QLabel(self)
        self.label.setGeometry(30, 10, 511, 71)
        self.label.setWordWrap(True)
        self.label.setAlignment(Qt.AlignRight)
        self.label.setStyleSheet("QLabel"
                                 "{"
                                 "border : 4px solid black;"
                                 "background : white;"
                                 "}")


        self.pushButton.clicked.connect(self.action1)
        self.pushButton_2.clicked.connect(self.action2)
        self.pushButton_3.clicked.connect(self.action3)
        self.pushButton_5.clicked.connect(self.action4)
        self.pushButton_6.clicked.connect(self.action5)
        self.pushButton_7.clicked.connect(self.action6)
        self.pushButton_9.clicked.connect(self.action7)
        self.pushButton_10.clicked.connect(self.action8)
        self.pushButton_11.clicked.connect(self.action9)
        self.pushButton_4.clicked.connect(self.action_div)
        self.pushButton_8.clicked.connect(self.action_mul)
        self.pushButton_16.clicked.connect(self.action_plus)
        self.pushButton_13.clicked.connect(self.action_point)
        self.pushButton_17.clicked.connect(self.action_clear)
        self.pushButton_18.clicked.connect(self.action_del)
        self.pushButton_12.clicked.connect(self.action_minus)
        self.pushButton_15.clicked.connect(self.action_equal)
        self.pushButton_14.clicked.connect(self.action0)


    def action_equal(self):
        equation = self.label.text()

        try:
            ans = eval(equation)
            self.label.setText(str(ans))

        except:
            self.label.setText("Wrong Input")



    def action_plus(self):
        text = self.label.text()
        self.label.setText(text + " + ")

    def action_minus(self):
        text = self.label.text()
        self.label.setText(text + "-")


    def action_div(self):
        text =self.label.text()
        self.label.setText(text + " / ")

    def action_mul(self):
        text = self.label.text()
        self.label.setText(text + " * ")

    def action_point(self):
        text = self.label.text()
        if text[-1] != '.':
            self.label.setText(text + ".")
        else:
            self.label.setText(text)

    def action0(self):
        text = self.label.text()
        if text != '':
            self.label.setText(text + "0")

    def action1(self):
        text = self.label.text()
        self.label.setText(text + "1")

    def action2(self):
        text = self.label.text()
        self.label.setText(text + "2")

    def action3(self):
        text = self.label.text()
        self.label.setText(text + "3")

    def action4(self):
        text = self.label.text()
        self.label.setText(text + "4")

    def action5(self):
        text = self.label.text()
        self.label.setText(text + "5")

    def action6(self):
        text = self.label.text()
        self.label.setText(text + "6")

    def action7(self):
        text = self.label.text()
        self.label.setText(text + "7")

    def action8(self):
        text = self.label.text()
        self.label.setText(text + "8")

    def action9(self):
        text = self.label.text()
        self.label.setText(text + "9")

    def action_clear(self):
        self.label.setText("")

    def action_del(self):
        text = self.label.text()
        print(text[:len(text) - 1])
        self.label.setText(text[:len(text) - 1])



if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()
