import random
import sys
from PySide6.QtWidgets import QApplication , QMainWindow ,  QMessageBox
from PySide6.QtUiTools import QUiLoader
from ui_mainwindow import Ui_MainWindow 
from functools import partial



class MainWindow(QMainWindow):
    def __init__(self) :
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self) 

        self.buttons = [[self.ui.k1 , self.ui.k2 , self.ui.k3 , self.ui.k4],
                        [self.ui.k5 , self.ui.k6 , self.ui.k7 , self.ui.k8],
                        [self.ui.k9 , self.ui.k10 , self.ui.k11 , self.ui.k12],
                        [self.ui.k13 , self.ui.k14 , self.ui.k15 , self.ui.k16]]

        nondup_list = nonduplicatearray(4,4)
        for i in range(4):
            for j in range(4):
                r = nondup_list[i][j]
                self.buttons[i][j].setText(str(r))
                self.buttons[i][j].clicked.connect(partial(self.play , i , j))
                if r == 16 : 
                    self.buttons[i][j].setVisible(False)
                    self.RowOfEmptyCell = i
                    self.ColOfEmptyCell = j



    def play(self , i , j):
        if (i == self.RowOfEmptyCell and (j == self.ColOfEmptyCell -1  or j == self.ColOfEmptyCell +1)) or ( j == self.ColOfEmptyCell and (i == self.RowOfEmptyCell -1 or i == self.RowOfEmptyCell +1  )): # اگر خونه ایی که کلیک کردیم همسایه خونه خالی بود
            self.buttons[self.RowOfEmptyCell][self.ColOfEmptyCell].setText(self.buttons[i][j].text()) # 16 <-- n 
            self.buttons[i][j].setText("16") #  n <--16
            self.buttons[self.RowOfEmptyCell][self.ColOfEmptyCell].setVisible(True)
            self.buttons[i][j].setVisible(False)

            self.RowOfEmptyCell = i
            self.ColOfEmptyCell = j
        else :
            pass 
            
        if self.check_win() == True :
            message =  QMessageBox()
            message.setText("🔴🟠🟡🟢🔵🟣🔵🟢🟡🟠🔴\n🔴🟠😍⚡You Won ⚡😍🟠🔴\n🔴🟠🟡🟢🔵🟣🔵🟢🟡🟠🔴")
            message.exec()


    def check_win(self):
        index = 1
        for i in range(4):
            for j in range(4):
                if int (self.buttons[i][j].text()) != index :
                    return False
                index += 1
        return True


def nonduplicatearray(row , col):
    array = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    for row in range(4):
        for col in range(4):
            flag = True
            while flag == True :
                c= 0
                randnum =random.randint(1,16)
                for i in range(4) :
                    for j in range(4) :
                        temp = array[i][j]
                        if temp != randnum : 
                            c+=1
                if c == 16 :              
                    array[row][col] = randnum
                    flag = False
                else :
                    flag = True
                
    return array   


app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()


app.exec()

