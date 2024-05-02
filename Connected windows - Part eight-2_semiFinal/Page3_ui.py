# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Page3_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.



from PyQt5 import QtCore, QtGui, QtWidgets
from Custom_Widgets.QCustomCheckBox import QCustomCheckBox
import icons


from Custom_title_bar import *

# for reading the json file 
import json

# for animation value imported from json file not be a str and convert it into a value
from PyQt5.QtCore import QEasingCurve


# # method for reading json file 
# def loadJsonFile(filepath):
#     with open(filepath, 'r') as file:
#         return json.load(file)


# # method for converting the animation valur of json file into a value 
# def getEasingCurve(curveStr):
#     if curveStr == "Linear":
#         return QEasingCurve.Linear
#     # Add other cases for different easing curves as necessary
#     # For example:
#     # if curveStr == "InOutQuad":
#     #     return QEasingCurve.InOutQuad

#     if curveStr == "InOutCubic":
#         return QEasingCurve.InOutCubic
    
#     # Default case if not matched
#     return QEasingCurve.Linear


class Page3_ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("/* Header 1 */\n"
"\n"
"\n"
"#headre_2{\n"
"background-color:#105857;\n"
"}\n"
"\n"
"#cancel_btn{\n"
"color:white;\n"
"border:none;\n"
"background-color:#0c4140;\n"
"border-radius:10px;;\n"
"}\n"
"\n"
"#cancel_btn:hover{\n"
"background-color:#25827c;\n"
"}\n"
"\n"
"#next_btn{\n"
"color:white;\n"
"border:none;\n"
"background-color:#0c4140;\n"
"border-radius:10px;;\n"
"}\n"
"\n"
"#next_btn:hover{\n"
"background-color:#25827c;\n"
"}\n"
"\n"
"#back_btn{\n"
"border:none;\n"
"background-color:#9eb1b1;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"#back_btn:hover{\n"
"background-color:#d1d2d2;\n"
"}\n"
"\n"
"#backup_label{\n"
"color:white;\n"
"padding-right:35px;\n"
"}\n"
"\n"
"/* Body */\n"
"#body{\n"
"background-color:#e0e2e3;\n"
"}\n"
"\n"
"#storage_label{\n"
"color:white;\n"
"background-color:#87ACA3;\n"
"border-radius:50px;\n"
"\n"
"/*border-top-right-radius: 50px;\n"
"border-bottom-right-radius: 30px;\n"
"border-top-left-radius: 15px;\n"
"border-bottom-left-radius: 5px*/\n"
"}\n"
"\n"
"\n"
"#gdrive_btn,#local_dir_btn,#dropbox_btn{\n"
"border:none;\n"
"}\n"
"\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 60))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.headre_2 = QtWidgets.QFrame(self.frame_2)
        self.headre_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.headre_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.headre_2.setObjectName("headre_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.headre_2)
        self.horizontalLayout_2.setContentsMargins(9, 5, 9, 9)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.cancel_btn = QtWidgets.QPushButton(self.headre_2)
        self.cancel_btn.setMinimumSize(QtCore.QSize(150, 45))
        self.cancel_btn.setMaximumSize(QtCore.QSize(200, 45))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(15)
        self.cancel_btn.setFont(font)
        self.cancel_btn.setObjectName("cancel_btn")
        self.horizontalLayout_2.addWidget(self.cancel_btn)
        self.backup_label = QtWidgets.QLabel(self.headre_2)
        self.backup_label.setMinimumSize(QtCore.QSize(0, 45))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.backup_label.setFont(font)
        self.backup_label.setAlignment(QtCore.Qt.AlignCenter)
        self.backup_label.setObjectName("backup_label")
        self.horizontalLayout_2.addWidget(self.backup_label)
        self.back_btn = QtWidgets.QPushButton(self.headre_2)
        self.back_btn.setMinimumSize(QtCore.QSize(100, 45))
        self.back_btn.setMaximumSize(QtCore.QSize(100, 45))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(15)
        self.back_btn.setFont(font)
        self.back_btn.setObjectName("back_btn")
        self.horizontalLayout_2.addWidget(self.back_btn)
        self.next_btn = QtWidgets.QPushButton(self.headre_2)
        self.next_btn.setMinimumSize(QtCore.QSize(150, 45))
        self.next_btn.setMaximumSize(QtCore.QSize(150, 45))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(15)
        self.next_btn.setFont(font)
        self.next_btn.setObjectName("next_btn")
        self.horizontalLayout_2.addWidget(self.next_btn)
        self.verticalLayout_5.addWidget(self.headre_2)
        self.verticalLayout.addWidget(self.frame_2)
        self.body = QtWidgets.QFrame(self.centralwidget)
        self.body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.body.setObjectName("body")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.body)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_8 = QtWidgets.QFrame(self.body)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_11 = QtWidgets.QFrame(self.frame_8)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_11)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.frame_11)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.storage_label = QtWidgets.QLabel(self.frame_4)
        self.storage_label.setGeometry(QtCore.QRect(20, 200, 400, 100))
        self.storage_label.setMinimumSize(QtCore.QSize(400, 100))
        self.storage_label.setMaximumSize(QtCore.QSize(400, 100))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(25)
        font.setBold(True)
        font.setItalic(False)
        self.storage_label.setFont(font)
        self.storage_label.setAlignment(QtCore.Qt.AlignCenter)
        self.storage_label.setObjectName("storage_label")
        self.verticalLayout_2.addWidget(self.frame_4)
        self.horizontalLayout.addWidget(self.frame)
        self.frame_3 = QtWidgets.QFrame(self.frame_11)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_6 = QtWidgets.QFrame(self.frame_3)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gdrive_toggle = QCustomCheckBox(self.frame_6)
        self.gdrive_toggle.setGeometry(QtCore.QRect(30, 160, 80, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.gdrive_toggle.setFont(font)
        self.gdrive_toggle.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.gdrive_toggle.setText("")
        self.gdrive_toggle.setIconSize(QtCore.QSize(25, 25))
        self.gdrive_toggle.setChecked(False)
        self.gdrive_toggle.setTristate(False)
        self.gdrive_toggle.setObjectName("gdrive_toggle")
        self.dropbox_toggle = QCustomCheckBox(self.frame_6)
        self.dropbox_toggle.setGeometry(QtCore.QRect(30, 310, 80, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.dropbox_toggle.setFont(font)
        self.dropbox_toggle.setText("")
        self.dropbox_toggle.setIconSize(QtCore.QSize(25, 25))
        self.dropbox_toggle.setObjectName("dropbox_toggle")
        self.gdrive_btn = QtWidgets.QPushButton(self.frame_6)
        self.gdrive_btn.setGeometry(QtCore.QRect(190, 150, 220, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.gdrive_btn.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/google-drive-svgrepo-com.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.gdrive_btn.setIcon(icon)
        self.gdrive_btn.setIconSize(QtCore.QSize(40, 40))
        self.gdrive_btn.setObjectName("gdrive_btn")
        self.dropbox_btn = QtWidgets.QPushButton(self.frame_6)
        self.dropbox_btn.setGeometry(QtCore.QRect(190, 300, 220, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.dropbox_btn.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/dropbox-color-svgrepo-com.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dropbox_btn.setIcon(icon1)
        self.dropbox_btn.setIconSize(QtCore.QSize(40, 40))
        self.dropbox_btn.setObjectName("dropbox_btn")
        self.verticalLayout_3.addWidget(self.frame_6)
        self.horizontalLayout.addWidget(self.frame_3)
        self.horizontalLayout_3.addWidget(self.frame_11)
        self.verticalLayout_6.addWidget(self.frame_8)
        self.verticalLayout.addWidget(self.body)
        MainWindow.setCentralWidget(self.centralwidget)



        #     # Load styles
        # checkBoxStyles = loadJsonFile(r"Json_Style\style.json")["QCustomCheckBox1"]
        # checkBoxStyles["animationEasingCurve"] = getEasingCurve(checkBoxStyles["animationEasingCurve"])

        
        # Apply styles to each checkbox
        self.gdrive_toggle.customizeQCustomCheckBox(
                bgColor = "#8A9EA0",
                circleColor = "#08313A",
                activeColor = "#517E64",
                animationEasingCurve = QEasingCurve.Linear,
                animationDuration = 500
        )
        self.dropbox_toggle.customizeQCustomCheckBox(
                bgColor = "#8A9EA0",
                circleColor = "#08313A",
                activeColor = "#517E64",
                animationEasingCurve = QEasingCurve.Linear,
                animationDuration = 500
        )

        self.gdrive_toggle.setFixedSize(200, 40)
        self.dropbox_toggle.setFixedSize(200, 40)




        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.cancel_btn.setText(_translate("MainWindow", "Cancel"))
        self.backup_label.setText(_translate("MainWindow", "                Back up"))
        self.back_btn.setText(_translate("MainWindow", "Back"))
        self.next_btn.setText(_translate("MainWindow", "Next"))
        self.storage_label.setText(_translate("MainWindow", "Storage Location "))
        self.gdrive_btn.setText(_translate("MainWindow", "Google Drive"))
        self.dropbox_btn.setText(_translate("MainWindow", "Dropbox"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Page3_ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
