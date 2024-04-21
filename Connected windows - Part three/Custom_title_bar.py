from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget


#Global value for window status 
WINDOW_SIZE = 0;
# THIS WILL HELP US DETERMINE IF TEH WINDOW IS MINIMIZED OR MAXIMIZED


class CustomMainWindow(QMainWindow):
    def __init__(self, ui_class):
        super().__init__()
        self.setWindowTitle("Custom Title Bar")  # Set window title
        self.resize(400, 200)  # Set initial size
        self.setWindowFlags(Qt.FramelessWindowHint)  # Make window frameless
        
        self.ui = ui_class()
        self.ui.setupUi(self)

        # Correctly connect the close button's clicked signal to the close method of the window
        self.ui.close_btn.clicked.connect(self.close)

        self.ui.minimize_btn.clicked.connect(self.showMinimized)

        # self.ui.maximize_btn.clicked.connect(self.restore_or_maximize_window)
        # above code is to make the window maximized or restore option ...its def is below ....but in our project we are not implementung teh maximize option 
             

             
    def buttonClicked(buttonName):
        print(f"{buttonName} has been clicked.")


    # Restore or maximize your window 
    def restore_or_maximize_window(self):

        # Global windows state 
        global WINDOW_SIZE  # THE DEDAULT VALUE IS ZERO TO SHOW THAT THE SIZE IS NOT MAXIMIZED
        win_status = WINDOW_SIZE

        if win_status == 0:   
            # if window is not maximized 
            WINDOW_SIZE = 1   # UPDATE VALUE TO SHOW THAT THE WINDOW HAS BEEN MAXIMIZED 
            self.showMaximized()

        else:
            # if the window is on its default size 
            WINDOW_SIZE = 0   # UPDATE VALUE TO SHOW THAT THE WINDOW HAS BEEN MINIMIZED 
            self.showNormal()



        # Initialize the old position
        self._old_pos = None


         # Connect mouse events to the title bar or another element meant to be draggable
        self.ui.header.mousePressEvent = self.mousePressEvent
        self.ui.header.mouseMoveEvent = self.mouseMoveEvent
        self.ui.header.mouseReleaseEvent = self.mouseReleaseEvent



    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._old_pos = event.globalPos()

    def mouseMoveEvent(self, event):
        if not self._old_pos:
            return
        delta = event.globalPos() - self._old_pos
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self._old_pos = event.globalPos()

    def mouseReleaseEvent(self, event):
        self._old_pos = None
    
