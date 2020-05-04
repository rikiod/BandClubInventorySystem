import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QDialog, QTableWidgetItem
import csv
from csv import writer

from OOP.Lingye.homePage import homePage


class Home(QMainWindow, homePage):  # this is the main parent, and as such, it takes the library QMainWindow
    def __init__(self, parent=None):
        super(Home, self).__init__(parent)
        self.setupUi(self)  # creating the window by running the self function as defined in the UI file
        self.load()

        self.tableWidget.cellChanged.connect(self.changeTable)

        self.changes_btn.clicked.connect(self.save)
        self.revert_btn.clicked.connect(self.cancel)


    def changeTable(self):
        item = self.tableWidget.currentItem()  # cell clicked
        row = self.tableWidget.currentRow()  # row clicked
        col = self.tableWidget.currentColumn()  # column selected
        self.changes_btn.setDisabled(False)
        self.revert_btn.setDisabled(False)

    def save(self):
        col_count = self.tableWidget.columnCount()
        row_count = self.tableWidget.rowCount()

        with open('db.csv', 'w') as f:
            for row in range(row_count): #  cycling through each row
                row_data = []
                for col in range(col_count):
                    widgetItem = self.tableWidget.item(row, col) #  cycling through each column (working left to right)
                    if widgetItem and widgetItem.text: #  since item doesn't have the attribute 'text,' this step is necessary
                        row_data.append(widgetItem.text())
                    else:
                        row_data.append(' ')
                f.write(', '.join(row_data) + '\n')
        f.close()
        return

    def load(self):
        data = []
        with open('db.csv') as db:
            file = csv.reader(db, delimiter=',')
            for r, row in enumerate(file):
                for c, col in enumerate(row):
                    data.append([r, c, col])
                    self.tableWidget.setItem(r, c, QTableWidgetItem(col))

        return data


    def cancel(self):
        self.load()
        return

        #  if i wanted a login: login = loginApp(self)
        #  login.show() this would cause the login class, and thus its window, to pop up over the Home
        #  check_in_app = In(self)
        #  check_in_app.show()
        #  to change it so this window can't be moved, you must change the window modality from
        #  non modal to window modal

        #  self.out_btn.clicked.connect(self.OpenCheckOut)  # if the "out" button is pressed, redirect to "Open Check out" function





app = QApplication(sys.argv)  # creating the application with arguments from user
main_window = Home()  # setting the main window to the Home UI
main_window.show()
app.exec_()
