# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Deja_Dup_ui_test.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import os


from PyQt5 import QtCore, QtGui, QtWidgets
from Custom_Widgets.QCustomCheckBox import QCustomCheckBox
import icons


from Custom_title_bar import *

# for reading the json file 
import json

# for animation value imported from json file not be a str and convert it into a value
from PyQt5.QtCore import QEasingCurve


# method for reading json file 
def loadJsonFile(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)


# method for converting the animation valur of json file into a value 
def getEasingCurve(curveStr):
    if curveStr == "Linear":
        return QEasingCurve.Linear
    # Add other cases for different easing curves as necessary
    # For example:
    # if curveStr == "InOutQuad":
    #     return QEasingCurve.InOutQuad

    if curveStr == "InOutCubic":
        return QEasingCurve.InOutCubic
    
    # Default case if not matched
    return QEasingCurve.Linear



class Page1_ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 600)
        MainWindow.setStyleSheet("*{\n"
"background-color:#E0E2E3\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.header = QtWidgets.QFrame(self.centralwidget)
        self.header.setMinimumSize(QtCore.QSize(0, 50))
        self.header.setMaximumSize(QtCore.QSize(16777215, 50))
        self.header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header.setObjectName("header")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.header)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame = QtWidgets.QFrame(self.header)
        self.frame.setMinimumSize(QtCore.QSize(311, 0))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.overview_frame = QtWidgets.QFrame(self.frame)
        self.overview_frame.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        self.overview_frame.setFont(font)
        self.overview_frame.setStyleSheet("")
        self.overview_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.overview_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.overview_frame.setObjectName("overview_frame")
        self.overview_btn = QtWidgets.QPushButton(self.overview_frame)
        self.overview_btn.setGeometry(QtCore.QRect(0, 8, 180, 35))
        self.overview_btn.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(13)
        font.setBold(True)
        self.overview_btn.setFont(font)
        self.overview_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.overview_btn.setStyleSheet("#overview_btn{\n"
"border : none;\n"
"border-radius : 5px;\n"
"padding : 5px 10px;\n"
"color:white;\n"
"background-color : #0c4140;\n"
"}\n"
"\n"
"#overview_btn:hover{\n"
"background-color : #105857;\n"
"\n"
"}\n"
"\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/safe-square-svgrepo-com (1).svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.overview_btn.setIcon(icon)
        self.overview_btn.setIconSize(QtCore.QSize(30, 30))
        self.overview_btn.setObjectName("overview_btn")
        self.horizontalLayout.addWidget(self.overview_frame, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.restore_frame = QtWidgets.QFrame(self.frame)
        self.restore_frame.setMinimumSize(QtCore.QSize(200, 50))
        self.restore_frame.setMaximumSize(QtCore.QSize(16777215, 50))
        self.restore_frame.setStyleSheet("\n"
"\n"
"")
        self.restore_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.restore_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.restore_frame.setObjectName("restore_frame")
        self.restore_btn = QtWidgets.QPushButton(self.restore_frame)
        self.restore_btn.setGeometry(QtCore.QRect(0, 8, 180, 35))
        self.restore_btn.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(13)
        font.setBold(True)
        self.restore_btn.setFont(font)
        self.restore_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.restore_btn.setStyleSheet("#restore_btn{\n"
"border : none;\n"
"border-radius : 5px;\n"
"padding : 5px 10px;\n"
"color:white;\n"
"background-color : #0c4140;\n"
"}\n"
"\n"
"#restore_btn:hover{\n"
"background-color : #105857;\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/settings-svgrepo-com (1).svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.restore_btn.setIcon(icon1)
        self.restore_btn.setIconSize(QtCore.QSize(28, 28))
        self.restore_btn.setObjectName("restore_btn")
        self.horizontalLayout.addWidget(self.restore_frame, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.horizontalLayout_2.addWidget(self.frame, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addWidget(self.header)
        self.image = QtWidgets.QFrame(self.centralwidget)
        self.image.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.image.setFrameShadow(QtWidgets.QFrame.Raised)
        self.image.setObjectName("image")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.image)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_4 = QtWidgets.QFrame(self.image)
        self.frame_4.setMinimumSize(QtCore.QSize(224, 235))
        self.frame_4.setMaximumSize(QtCore.QSize(205, 281))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label = QtWidgets.QLabel(self.frame_4)
        self.label.setGeometry(QtCore.QRect(0, 70, 204, 196))
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.frame_4, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addWidget(self.image)
        self.info_and_btn = QtWidgets.QFrame(self.centralwidget)
        self.info_and_btn.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.info_and_btn.setFrameShadow(QtWidgets.QFrame.Raised)
        self.info_and_btn.setObjectName("info_and_btn")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.info_and_btn)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.backup_automaticly = QtWidgets.QFrame(self.info_and_btn)
        self.backup_automaticly.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.backup_automaticly.setFrameShadow(QtWidgets.QFrame.Raised)
        self.backup_automaticly.setObjectName("backup_automaticly")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.backup_automaticly)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_5 = QtWidgets.QFrame(self.backup_automaticly)
        self.frame_5.setMinimumSize(QtCore.QSize(700, 100))
        self.frame_5.setMaximumSize(QtCore.QSize(700, 100))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.frame_5.setFont(font)
        self.frame_5.setStyleSheet("*{\n"
"background-color: #ffffff;\n"
"border-top-left-radius: 20px;\n"
"border-top-right-radius: 25px;\n"
"}")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_5.setLineWidth(1)
        self.frame_5.setMidLineWidth(0)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_3.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.frame_5)
        self.label_2.setMaximumSize(QtCore.QSize(400, 16777215))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2, 0, QtCore.Qt.AlignLeft)
        self.checkBox = QCustomCheckBox(self.frame_5)
        self.checkBox.setMinimumSize(QtCore.QSize(60, 40))
        self.checkBox.setMaximumSize(QtCore.QSize(90, 40))
        self.checkBox.setSizeIncrement(QtCore.QSize(0, 0))
        self.checkBox.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.checkBox.setFont(font)
        self.checkBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkBox.setStyleSheet("#checkBox{\n"
"padding : 5px 10px;\n"
"\n"
"\n"
"}")
        self.checkBox.setText("")
        self.checkBox.setIconSize(QtCore.QSize(15, 15))
        self.checkBox.setTristate(False)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_3.addWidget(self.checkBox)
        self.horizontalLayout_4.addWidget(self.frame_5, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.verticalLayout_3.addWidget(self.backup_automaticly)
        self.create_backup = QtWidgets.QFrame(self.info_and_btn)
        self.create_backup.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.create_backup.setFrameShadow(QtWidgets.QFrame.Raised)
        self.create_backup.setObjectName("create_backup")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.create_backup)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_6 = QtWidgets.QFrame(self.create_backup)
        self.frame_6.setMinimumSize(QtCore.QSize(700, 0))
        self.frame_6.setMaximumSize(QtCore.QSize(700, 16777215))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.backup_btn = QtWidgets.QPushButton(self.frame_6)
        self.backup_btn.setGeometry(QtCore.QRect(0, 0, 700, 60))
        self.backup_btn.setMinimumSize(QtCore.QSize(700, 60))
        self.backup_btn.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(14)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.backup_btn.setFont(font)
        self.backup_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.backup_btn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.backup_btn.setStyleSheet("#backup_btn{\n"
"border-bottom-left-radius: 20px;\n"
"border-bottom-right-radius: 20px;\n"
"background-color:#ffffff;\n"
"}\n"
"\n"
"#backup_btn:hover{\n"
"background-color:#9EB1B1;\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/right_arrow_key.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.backup_btn.setIcon(icon2)
        self.backup_btn.setIconSize(QtCore.QSize(30, 50))
        self.backup_btn.setCheckable(False)
        self.backup_btn.setObjectName("backup_btn")
        self.verticalLayout_4.addWidget(self.frame_6, 0, QtCore.Qt.AlignHCenter)
        self.frame_7 = QtWidgets.QFrame(self.create_backup)
        self.frame_7.setMinimumSize(QtCore.QSize(700, 0))
        self.frame_7.setMaximumSize(QtCore.QSize(700, 16777215))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_4.addWidget(self.frame_7, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_3.addWidget(self.create_backup)
        self.verticalLayout.addWidget(self.info_and_btn)
        MainWindow.setCentralWidget(self.centralwidget)


        
        # Load styles
        checkBoxStyles = loadJsonFile(r"Json Style\style.json")["QCustomCheckBox1"]
        checkBoxStyles["animationEasingCurve"] = getEasingCurve(checkBoxStyles["animationEasingCurve"])

        
        # Apply styles to each checkbox
        self.checkBox.customizeQCustomCheckBox(**checkBoxStyles)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)





        # Connect buttons to the click handler with a lambda to pass the button name
        self.backup_btn.clicked.connect(lambda: CustomMainWindow.buttonClicked("backup button "))
        # self.Restore_from_prev_btn.clicked.connect(lambda: CustomMainWindow.buttonClicked("Restore"))
        self.checkBox.clicked.connect(lambda: CustomMainWindow.buttonClicked("toggle"))
        # self.menu_btn.clicked.connect(lambda: CustomMainWindow.buttonClicked("menue btn"))
        # self.minimize_btn.clicked.connect(lambda: CustomMainWindow.buttonClicked("minimize btn"))
        # self.close_btn.clicked.connect(lambda: CustomMainWindow.buttonClicked("Close btn"))
        self.overview_btn.clicked.connect(lambda: CustomMainWindow.buttonClicked("overbiew btn"))
        self.restore_btn.clicked.connect(lambda: CustomMainWindow.buttonClicked("Restore btn"))


      

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.overview_btn.setText(_translate("MainWindow", " Overview"))
        self.restore_btn.setText(_translate("MainWindow", "Settings"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/icons/icons/backup_logo-removebg-preview (1).png\"/></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Back Up Automatically"))
        self.backup_btn.setText(_translate("MainWindow", "Create My First Backup"))





# To run code of this specific ui only 
# if __name__ == "__main__":
#     import sys
#     app = QApplication(sys.argv)
#     window = CustomMainWindow(Page1_ui_MainWindow)
#     window.show()
#     sys.exit(app.exec())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Page1_ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())