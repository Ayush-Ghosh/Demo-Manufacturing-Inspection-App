from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtChart import QChart, QChartView, QBarSet, QPercentBarSeries, QBarCategoryAxis, QStackedBarSeries
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt
import sys, os, time
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtChart import *
import pymongo
    
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["BottlePlant"]

class App(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # Window Settings
        self.x, self.y, self.w, self.h = 0, 0, 1285, 860
        self.setGeometry(self.x, self.y, self.w, self.h)

        self.window = MainWindow(self)
        self.setCentralWidget(self.window)
        self.setWindowTitle("Test Application") # Window Title
        self.show()
        self.setWindowIcon(QtGui.QIcon('icons/icon.png'))

class GeneralWidget(QtWidgets.QWidget):
    # def __init__(self, parent=None):
    def __init__(self):
        # super(GeneralWidget, self).__init__(parent)
        super(GeneralWidget, self).__init__()
        global lay
        lay = QtWidgets.QVBoxLayout(self)
        font = QtGui.QFont()
        font.setPointSize(9)
        # Dropdown for selecting analytics or sku
        comboBox = QtWidgets.QComboBox()
        comboBox.setObjectName("comboBox")
        comboBox.addItem("SKU Selection")
        comboBox.addItem("Analytics View")
        comboBox.activated[str].connect(self.bargraph)
        comboBox.setToolTip("Select an Option!")    # Message to show when mouse hover
        comboBox.setFont(font)

        label = QLabel()
        font1 = QtGui.QFont()
        font1.setPointSize(12)
        label.setText("Please select an Option From The Above Dropdown!")
        label.setAlignment(Qt.AlignCenter)
        label.setFont(font1)

        lay.addWidget(comboBox,0)
        lay.addWidget(label,1)
        lay.addStretch(0)
    
    def clearLayout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.clearLayout(item.layout())

    def dynamicaly_created_radiobtns(self):
        font = QtGui.QFont()
        font.setPointSize(9)
        coll_list = []
        #list the collections in db
        for coll in mydb.list_collection_names():
            coll_list.append(coll)

        self.button_group = QButtonGroup()
        for i in coll_list:
            self.button_name = QRadioButton("{}".format(i))
            self.button_name.setObjectName("radiobtn_{}".format(i))
            lay.addWidget(self.button_name,0,Qt.AlignTop)
            self.button_group.addButton(self.button_name)
            self.button_name.toggled.connect(self.plotgraph)
            self.button_name.setFont(font)

    def plotgraph(self):
        print(self.button_group.checkedButton().text())
        collection_name = self.button_group.checkedButton().text()
        mycol = mydb[collection_name]
        font = QtGui.QFont()
        font.setPointSize(9)

        ############### Query from the SKU(collection) for total number of good/bad count ##############

        global y1,y2,y3,y4,y5,y6,y7,y8,z1,z2,z3,z4,z5,z6,z7,z8
        ls0 =[]
        myquery0 = {"Status": "Bad", "SKU id":"S1" }
        for x in mycol.find(myquery0):
            ls0.append(x)
        y1 = len(ls0)

        ls1 =[]
        myquery1 = {"Status": "Good", "SKU id":"S1" }
        for x in mycol.find(myquery1):
            ls1.append(x)
        z1 = len(ls1)


        ls2 =[]
        myquery2 = {"Status": "Bad", "SKU id":"S2" }
        for x in mycol.find(myquery2):
            ls2.append(x)
        y2 = len(ls2)

        ls3 =[]
        myquery3 = {"Status": "Good", "SKU id":"S2" }
        for x in mycol.find(myquery3):
            ls3.append(x)
        z2 = len(ls3)


        ls4 =[]
        myquery4 = {"Status": "Bad", "SKU id":"S3" }
        for x in mycol.find(myquery4):
            ls4.append(x)
        y3 = len(ls4)

        ls5 =[]
        myquery5 = {"Status": "Good", "SKU id":"S3" }
        for x in mycol.find(myquery5):
            ls5.append(x)
        z3 = len(ls5)


        ls6 =[]
        myquery6 = {"Status": "Bad", "SKU id":"S4" }
        for x in mycol.find(myquery6):
            ls6.append(x)
        y4 = len(ls6)

        ls7 =[]
        myquery7 = {"Status": "Good", "SKU id":"S4" }
        for x in mycol.find(myquery7):
            ls7.append(x)
        z4 = len(ls7)


        ls8 =[]
        myquery8 = {"Status": "Bad", "SKU id":"S5" }
        for x in mycol.find(myquery8):
            ls8.append(x)
        y5 = len(ls8)

        ls9 =[]
        myquery9 = {"Status": "Good", "SKU id":"S5" }
        for x in mycol.find(myquery9):
            ls9.append(x)
        z5 = len(ls9)


        ls10 =[]
        myquery10 = {"Status": "Bad", "SKU id":"S6" }
        for x in mycol.find(myquery10):
            ls10.append(x)
        y6 = len(ls10)

        ls11 =[]
        myquery11 = {"Status": "Good", "SKU id":"S6" }
        for x in mycol.find(myquery11):
            ls11.append(x)
        z6 = len(ls11)


        ls12 =[]
        myquery12 = {"Status": "Bad", "SKU id":"S7" }
        for x in mycol.find(myquery12):
            ls12.append(x)
        y7 = len(ls12)

        ls13 =[]
        myquery13 = {"Status": "Good", "SKU id":"S7" }
        for x in mycol.find(myquery13):
            ls13.append(x)
        z7 = len(ls13)


        ls14 =[]
        myquery14 = {"Status": "Bad", "SKU id":"S8" }
        for x in mycol.find(myquery14):
            ls14.append(x)
        y8 = len(ls14)

        ls15 =[]
        myquery15 = {"Status": "Good", "SKU id":"S8" }
        for x in mycol.find(myquery15):
            ls15.append(x)
        z8 = len(ls15)

        self.clearLayout(lay)
        #########################################################################
        set0 = QBarSet("Good")
        set1 = QBarSet("Bad")
            
        # set0.append([5400, 4900, 5100, 5400, 5000, 4800, 4500, 3000])
        # set1.append([600, 800, 900, 600, 1000, 1200, 1500, 3000])
        set0.append([z1,z2,z3,z4,z5,z6,z7,z8])
        set1.append([y1,y2,y3,y4,y5,y6,y7,y8])

        series = QStackedBarSeries()
        series.append(set0)
        series.append(set1)
        
        chart = QChart()
        chart.addSeries(series)
        chart.setTitle("Production Count")
        chart.setAnimationOptions(QChart.SeriesAnimations)
            
        categories = ["12:30", "13:00", "13:30", "14:00", "14:30", "15:00", "15:30", "16:00"]
        axis = QBarCategoryAxis()
        axis.append(categories)
        chart.createDefaultAxes()
        chart.setAxisX(axis, series)

        axisY = QValueAxis()
        axisY.setRange(0, 6000)
        axisY.setTitleText("Units")
        chart.setAxisY(axisY)

        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)

        chartView = QChartView(chart)
        chartView.setRenderHint(QPainter.Antialiasing)
        chartView.setToolTip('Good Units v/s Bad Units')

        comboBox = QtWidgets.QComboBox()
        comboBox.setGeometry(QtCore.QRect(20, 20, 171, 31))
        comboBox.setObjectName("comboBox")
        comboBox.addItem("SKU Selection")
        comboBox.addItem("Analytics View")
        comboBox.activated[str].connect(self.bargraph)
        comboBox.setToolTip("Select an Option!")    # Message to show when mouse hover
        comboBox.setFont(font)

        lay.addWidget(comboBox,0)
        lay.addWidget(chartView,1)


    def bargraph(self, text):
        if text == "SKU Selection":
            # print("sku")
            self.clearLayout(lay)
            font = QtGui.QFont()
            font.setPointSize(9)

            comboBox = QtWidgets.QComboBox()
            comboBox.setGeometry(QtCore.QRect(20, 20, 171, 31))
            comboBox.setObjectName("comboBox")
            comboBox.addItem("SKU Selection")
            comboBox.addItem("Analytics View")
            comboBox.activated[str].connect(self.bargraph)
            comboBox.setToolTip("Select an Option!")    # Message to show when mouse hover
            comboBox.setFont(font)
            lay.addWidget(comboBox,0,Qt.AlignTop)

            self.dynamicaly_created_radiobtns()

        else:
            # print("analytics")
            try:
                self.clearLayout(lay)
                font = QtGui.QFont()
                font.setPointSize(9)
                
                set0 = QBarSet("Good")
                set1 = QBarSet("Bad")
                # set0.append([5400, 4900, 5100, 5400, 5000, 4800, 4500, 3000])
                # set1.append([600, 800, 900, 600, 1000, 1200, 1500, 3000])

                set0.append([z1,z2,z3,z4,z5,z6,z7,z8])
                set1.append([y1,y2,y3,y4,y5,y6,y7,y8])

                series = QStackedBarSeries()
                series.append(set0)
                series.append(set1)

                chart = QChart()
                chart.addSeries(series)
                chart.setTitle("Production Count")
                chart.setAnimationOptions(QChart.SeriesAnimations)

                categories = ["12:30", "13:00", "13:30", "14:00", "14:30", "15:00", "15:30", "16:00"]
                axis = QBarCategoryAxis()
                axis.append(categories)
                chart.createDefaultAxes()
                chart.setAxisX(axis, series)

                axisY = QValueAxis()
                axisY.setRange(0, 6000)
                axisY.setTitleText("Units")
                chart.setAxisY(axisY)

                chart.legend().setVisible(True)
                chart.legend().setAlignment(Qt.AlignBottom)

                chartView = QChartView(chart)
                chartView.setRenderHint(QPainter.Antialiasing)
                chartView.setToolTip('Good Units v/s Bad Units')

                comboBox = QtWidgets.QComboBox()
                comboBox.setGeometry(QtCore.QRect(20, 20, 171, 31))
                comboBox.setObjectName("comboBox")
                comboBox.addItem("SKU Selection")
                comboBox.addItem("Analytics View")
                comboBox.activated[str].connect(self.bargraph)
                comboBox.setToolTip("Select an Option!")    # Message to show when mouse hover
                comboBox.setFont(font)

                lay.addWidget(comboBox,0)
                lay.addWidget(chartView,1)
            
            except:

                self.clearLayout(lay)
                font = QtGui.QFont()
                font.setPointSize(9)
                
                set0 = QBarSet("Good")
                set1 = QBarSet("Bad")           
                # set0.append([5400, 4900, 5100, 5400, 5000, 4800, 4500, 3000])
                # set1.append([600, 800, 900, 600, 1000, 1200, 1500, 3000])

                set0.append([0,0,0,0,0,0,0,0])
                set1.append([0,0,0,0,0,0,0,0])

                series = QStackedBarSeries()
                series.append(set0)
                series.append(set1)
        
                chart = QChart()
                chart.addSeries(series)
                chart.setTitle("Production Count")
                chart.setAnimationOptions(QChart.SeriesAnimations)
                
                categories = ["12:30", "13:00", "13:30", "14:00", "14:30", "15:00", "15:30", "16:00"]
                axis = QBarCategoryAxis()
                axis.append(categories)
                chart.createDefaultAxes()
                chart.setAxisX(axis, series)

                axisY = QValueAxis()
                axisY.setRange(0, 6000)
                axisY.setTitleText("Units")
                chart.setAxisY(axisY)

                chart.legend().setVisible(True)
                chart.legend().setAlignment(Qt.AlignBottom)

                chartView = QChartView(chart)
                chartView.setRenderHint(QPainter.Antialiasing)
                chartView.setToolTip('Good Units v/s Bad Units')
                
                comboBox = QtWidgets.QComboBox()
                comboBox.setGeometry(QtCore.QRect(20, 20, 171, 31))
                comboBox.setObjectName("comboBox")
                comboBox.addItem("SKU Selection")
                comboBox.addItem("Analytics View")
                comboBox.activated[str].connect(self.bargraph)
                comboBox.setToolTip("Select an Option!")    # Message to show when mouse hover
                comboBox.setFont(font)

                lay.addWidget(comboBox,0)
                lay.addWidget(chartView,1)

                msgBox = QMessageBox(self)
                msgBox.setIcon(QMessageBox.Information)
                msgBox.setText("Please Select a SKU!")
                msgBox.setWindowTitle("Application Info")
                msgBox.setStandardButtons(QMessageBox.Ok)
                returnValue = msgBox.exec()
                if returnValue == QMessageBox.Ok:
                    print('OK clicked')



class ImagePopup(QLabel):
    def __init__(self, parent):
        super(QLabel, self).__init__(parent)
        
        thumb = parent.pixmap()
        imageSize = thumb.size()
        imageSize.setWidth(imageSize.width()*2)
        imageSize.setHeight(imageSize.height()*2)
        self.setPixmap(thumb.scaled(imageSize,Qt.KeepAspectRatioByExpanding))
        
        # center the zoomed image on the thumb
        position = self.cursor().pos()
        position.setX(position.x() - thumb.size().width())
        position.setY(position.y() - thumb.size().height())
        self.move(position)
        
        # FramelessWindowHint may not work on some window managers on Linux
        # so I had also foreced the flag X11BypassWindowManagerHint
        self.setWindowFlags(Qt.Popup | Qt.WindowStaysOnTopHint 
                            | Qt.FramelessWindowHint 
                            | Qt.X11BypassWindowManagerHint)

    def leaveEvent(self, event):
        """ When the mouse leave this widget, destroy it. """
        self.destroy()
        

class ImageLabel(QLabel):
    """ This widget displays an ImagePopup when the mouse enter its region """
    def enterEvent(self, event):
        self.p = ImagePopup(self)
        self.p.show()
        event.accept() 

class ImageGallery(QDialog):
    
    def __init__(self, parent=None):
        super(QDialog, self).__init__(parent)
        self.setWindowTitle("Image Gallery")
        self.setLayout(QGridLayout(self))
    
    def populate1(self, pics, size, imagesPerRow=6, 
                 flags=Qt.KeepAspectRatioByExpanding):
        global h
        row = col = 0
        for pic in pics:
            # print(pic)
            if pic == "inspected/5419.jpg" or pic == "inspected/5420.jpg" or pic == "inspected/5423.jpg" or pic == "inspected/5425.jpg":
                label = ImageLabel("")
                h = QLabel("Bad")
                h.setStyleSheet("background-color : #F64B31") 
                h.setFixedSize(150, 30)
                h.setAlignment(QtCore.Qt.AlignCenter)
                pixmap = QPixmap(pic)
                pixmap = pixmap.scaled(size, flags)
                label.setPixmap(pixmap)
                self.layout().addWidget(label, row, col)
                self.layout().addWidget(h, row+1, col)
                col +=1
                if col % imagesPerRow == 0:
                    row += 2
                    col = 0
                    
            else:
                label = ImageLabel("")
                h = QLabel("Good")
                h.setStyleSheet("background-color : #38ED52") 
                h.setFixedSize(150, 30)
                h.setAlignment(QtCore.Qt.AlignCenter)
                pixmap = QPixmap(pic)
                pixmap = pixmap.scaled(size, flags)
                label.setPixmap(pixmap)
                self.layout().addWidget(label, row, col)
                self.layout().addWidget(h, row+1, col)
                col +=1
                if col % imagesPerRow == 0:
                    row += 2
                    col = 0
                
    def populate2(self, pics, size, imagesPerRow=6, 
                 flags=Qt.KeepAspectRatioByExpanding):
        global h
        row = col = 0
        for pic in pics:
            label = ImageLabel("")
            h = QLabel("Bad")
            h.setStyleSheet("background-color : #F64B31 ") 
            h.setFixedSize(150, 30)
            h.setAlignment(QtCore.Qt.AlignCenter)
            pixmap = QPixmap(pic)
            pixmap = pixmap.scaled(size, flags)
            label.setPixmap(pixmap)
            self.layout().addWidget(label, row, col)
            self.layout().addWidget(h, row+1, col)
            col +=1
            if col % imagesPerRow == 0:
                row += 2
                col = 0
    
    def populate3(self, pics, size, imagesPerRow=6, 
                 flags=Qt.KeepAspectRatioByExpanding):
        global h
        row = col = 0
        for pic in pics:
            label = ImageLabel("")
            h = QLabel("Good")
            h.setAlignment(QtCore.Qt.AlignCenter)
            h.setFixedSize(150, 30)
            h.setStyleSheet("background-color : #38ED52 ") 
            pixmap = QPixmap(pic)
            pixmap = pixmap.scaled(size, flags)
            label.setPixmap(pixmap)
            self.layout().addWidget(label, row, col)
            self.layout().addWidget(h, row+1, col)
            col +=1
            if col % imagesPerRow == 0:
                row += 2
                col = 0

class OptionsWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(OptionsWidget, self).__init__(parent)

        global hlay, pushButton, pushButton_2, pushButton_3
        hlay = QGridLayout(self)

        font = QtGui.QFont()
        font.setPointSize(9)

        pushButton = QtWidgets.QPushButton("ALL")
        pushButton.setObjectName("pushButton")
        pushButton.move(1070,10)
        pushButton.setFont(font)
        pushButton.clicked.connect(self.pb)
        
        pushButton_2 = QtWidgets.QPushButton("Good")
        pushButton_2.setObjectName("pushButton_2")
        pushButton_2.setFont(font)
        pushButton_2.clicked.connect(self.pb2)
        
        pushButton_3 = QtWidgets.QPushButton("Bad")
        pushButton_3.setObjectName("pushButton_3")
        pushButton_3.setFont(font)
        pushButton_3.clicked.connect(self.pb1)
        
        label = QLabel()
        font = QtGui.QFont()
        font.setPointSize(12)
        label.setText("Please Select an Option!")
        label.setAlignment(Qt.AlignCenter)
        label.setFont(font)

        hlay.addWidget(pushButton,0,0)
        hlay.addWidget(pushButton_2,0,1)
        hlay.addWidget(pushButton_3,0,2)
        hlay.addWidget(label,1,1)
        self.setLayout(hlay)


    def pb(self):
        for i in reversed(range(hlay.count())): 
            hlay.itemAt(i).widget().setParent(None)

        pics = ["inspected/1.jpg", "inspected/5419.jpg","inspected/2.jpg","inspected/5420.jpg","inspected/5.jpg","inspected/6.jpg",
        "inspected/7.jpg","inspected/8.jpg","inspected/9.jpg","inspected/5423.jpg","inspected/11.jpg","inspected/5425.jpg","inspected/13.jpg",
        "inspected/14.jpg","inspected/15.jpg","inspected/16.jpg","inspected/17.jpg","inspected/18.jpg"]
        pushButton.setStyleSheet("background-color : #84C1FB") 
        pushButton_2.setStyleSheet("background-color : light grey") 
        pushButton_3.setStyleSheet("background-color : light grey") 
        pushButton.setFixedSize(100, 30)
        pushButton_2.setFixedSize(100, 30)
        pushButton_3.setFixedSize(100, 30)
        hlay.addWidget(pushButton,0,3)
        hlay.addWidget(pushButton_2,0,4)
        hlay.addWidget(pushButton_3,0,5)
        imgallery = ImageGallery()   
        imgallery.populate1(pics, QSize(150,150))
        hlay.addWidget(imgallery,1,0,1,0)
    
    def pb1(self):
        for i in reversed(range(hlay.count())): 
            hlay.itemAt(i).widget().setParent(None)
        
        pushButton_3.setStyleSheet("background-color : #84C1FB") 
        pushButton_2.setStyleSheet("background-color : light grey") 
        pushButton.setStyleSheet("background-color : light grey") 
        pushButton.setFixedSize(100, 30)
        pushButton_2.setFixedSize(100, 30)
        pushButton_3.setFixedSize(100, 30)
        hlay.addWidget(pushButton,0,3)
        hlay.addWidget(pushButton_2,0,4)
        hlay.addWidget(pushButton_3,0,5)
        pics = ["inspected/5419.jpg","inspected/5423.jpg", "inspected/5420.jpg", "inspected/5423.jpg", "inspected/5425.jpg", "inspected/5420.jpg",
        "inspected/5425.jpg", "inspected/5423.jpg", "inspected/5419.jpg"]*2
        imgallery = ImageGallery()   
        imgallery.populate2(pics, QSize(150,150))
        hlay.addWidget(imgallery,1,0,1,0) 
    
    def pb2(self):
        for i in reversed(range(hlay.count())): 
            hlay.itemAt(i).widget().setParent(None)
        
        pushButton_2.setStyleSheet("background-color : #84C1FB") 
        pushButton_3.setStyleSheet("background-color : light grey") 
        pushButton.setStyleSheet("background-color : light grey")
        pushButton.setFixedSize(100, 30)
        pushButton_2.setFixedSize(100, 30)
        pushButton_3.setFixedSize(100, 30)
        hlay.addWidget(pushButton,0,3)
        hlay.addWidget(pushButton_2,0,4)
        hlay.addWidget(pushButton_3,0,5)
        pics = ["inspected/1.jpg", "inspected/2.jpg","inspected/2.jpg","inspected/2.jpg","inspected/5.jpg","inspected/6.jpg"]*3
        imgallery = ImageGallery()   
        imgallery.populate3(pics, QSize(150,150))
        hlay.addWidget(imgallery,1,0,1,0)



class MainWindow(QtWidgets.QWidget):        
    def __init__(self, parent):   
        super(MainWindow, self).__init__(parent)
        layout = QtWidgets.QVBoxLayout(self)
        
        #set font size
        font = QtGui.QFont()
        font.setPointSize(9)
        
        
        # Initialize tabs
        tab_holder = QtWidgets.QTabWidget()   # Create tab holder
        tab_1 = GeneralWidget()           # Tab one        
        tab_2 = OptionsWidget()            # Tab two
        
        
        # Add tabs
        tab_holder.addTab(tab_1, "Analytics") 
        tab_holder.addTab(tab_2, "Image Gallery")  
        tab_holder.setFont(font)

        layout.addWidget(tab_holder)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())