Criteria C: Development:
=====================

### Early Development:

**Converting from UI to Python File:** 

There are a few steps which are necessary to begin the development of the user interface for this project. After creating the [design](https://github.com/rikiod/unit3/blob/master/criteriaB_design.md) on QtDesigner, I began development in order to convert the files to Python files in which all of the buttons and functions work properly. To convert a UI file to a Python file, I used the command `pyuic5 <name of UI file> -o <desired name of Python file>`. This can only be done after downloading the PyQt5 package using the command `pip install pyqt5`. From there, all of the commands from QtDesigner need to be imported as well. This includes QtWidgets, QtApplication, QMainWindow, QAction, QDialog, and QTableWidgetItem. 

**Importing Files to One Central File:**

Once the Python file is created for each individual window, they must all be merged so that you can work on one file. To do so, all of the classes must be imported into a main application file that can be run. Since there is only one window, this is the only command necesarry: 
```py
class Home(QMainWindow, homePage):  # this is the main parent, and as such, it takes the library QMainWindow
    def __init__(self, parent=None):
        super(Home, self).__init__(parent)
        self.setupUi(self)  # creating the window by running the self function as defined in the UI file 
```
     
**Adding Functions:**

After setting up the main window, it is important to define functions which are necessary for the program. Firstly, we have the function "change table" which defines the row, column, and item variables. It also enables the "save changes" and "cancel" buttons so that they are visible only after editing the information.

The save function works by cycling through each cell (row by row, column by column) and putting it into the database file. Since the database is a csv, each value is joined by commas so that it can be separated properly. 
   
```py
    for row in range(row_count): #  cycling through each row
        row_data = []
        for col in range(col_count):
            widgetItem = self.tableWidget.item(row, col) #  cycling through each column (working left to right)
            if widgetItem and widgetItem.text: #  since item doesn't have the attribute 'text,' this step is necessary
                row_data.append(widgetItem.text())
            else:
                row_data.append(' ') #. in the case that the cell is empty 
        f.write(', '.join(row_data) + '\n') #  comma is necessary for csv files 
```

This save function is necessary for the load function to work properly. It takes the information from the database file, and places it back into the table using the function setItem. It employs the enumerate function as well which is crucial because it uses the row and column variables to represent the position of the data, making sure that the table can be accurate. 

```py
     def load(self):
        data = []
        with open('db.csv') as db:
            file = csv.reader(db, delimiter=',') 
            for r, row in enumerate(file): #. taking each point from the db.csv file 
                for c, col in enumerate(row): #  cycling through each cell in the table
                    data.append([r, c, col])
                    self.tableWidget.setItem(r, c, QTableWidgetItem(col))
```

Lastly, the cancel function is important to delete any changes. It works simply by reloading the table with the load function. 

```py
    def cancel(self):
        self.load()
        return
```

      
