from PyQt5 import QtWidgets
from Page1_ui import Page1_ui_MainWindow
from Page2_ui1 import Page2_ui_MainWindow, MainWindow as Page2_MainWindow
from Page3_ui import Page3_ui_MainWindow
from Page4_ui import Page4_ui_MainWindow
from Page3_5_ui import Page3_5_ui_MainWindow


class MainWindowController:
    def __init__(self):
        import sys
        self.app = QtWidgets.QApplication(sys.argv)
        
        self.mainWindow = QtWidgets.QMainWindow()
        self.mainWindow.resize(900, 600)  # Set this to the desired dimensions
        self.stack = QtWidgets.QStackedWidget()
        self.mainWindow.setCentralWidget(self.stack)
        
        self.firstPageWindow = self.createPage(Page1_ui_MainWindow)
        self.secondPageWindow = Page2_MainWindow()  # Assuming this is correctly instantiated
        self.thirdPageWindow = self.createPage(Page3_ui_MainWindow)
        self.third_5PageWindow = self.createPage(Page3_5_ui_MainWindow)
        self.fourthPageWindow = self.createPage(Page4_ui_MainWindow)
        
        self.stack.addWidget(self.firstPageWindow)
        self.stack.addWidget(self.secondPageWindow)
        self.stack.addWidget(self.thirdPageWindow)
        self.stack.addWidget(self.third_5PageWindow)
        self.stack.addWidget(self.fourthPageWindow)

        # Ensure signals are connected to existing methods
        self.secondPageWindow.goBackSignal.connect(self.goBackToFirstPage)
        self.secondPageWindow.goToNextPageSignal.connect(self.goToThirdPage)

    def createPage(self, ui_class):
        page = QtWidgets.QMainWindow()
        ui = ui_class()
        ui.setupUi(page)
        page.ui = ui  # Store the ui object as an attribute of the page
        return page

    def startFirstPage(self):
        self.firstPageWindow.ui.backup_btn.clicked.connect(self.startSecondPage)  # Ensure `ui` is accessible
        self.stack.setCurrentWidget(self.firstPageWindow)

    def startSecondPage(self):
        self.stack.setCurrentWidget(self.secondPageWindow)

    def startThirdPage(self):
        self.stack.setCurrentWidget(self.thirdPageWindow)
        self.thirdPageWindow.ui.back_btn.clicked.connect(self.goToSecondPage)
        self.thirdPageWindow.ui.cancel_btn.clicked.connect(self.goBackToFirstPage)
        self.thirdPageWindow.ui.next_btn.clicked.connect(self.goToThird_5Page)

    def startFourthPage(self):
        self.stack.setCurrentWidget(self.fourthPageWindow)

    def startThird_5Page(self):
        self.stack.setCurrentWidget(self.third_5PageWindow)
        self.third_5PageWindow.ui.back_btn.clicked.connect(self.goToThirdPage)
        self.third_5PageWindow.ui.cancel_btn.clicked.connect(self.goBackToFirstPage)
        self.third_5PageWindow.ui.backup_btn.clicked.connect(self.goToFourthPage)

    def goBackToFirstPage(self):
        self.stack.setCurrentWidget(self.firstPageWindow)  # Correctly defining the missing method

    def goToThirdPage(self):
        self.startThirdPage()

    def goToThird_5Page(self):
        self.startThird_5Page()

    def goToSecondPage(self):
        self.startSecondPage()

    def goToFourthPage(self):
        self.startFourthPage()

    def execute(self):
        self.mainWindow.show()
        self.startFirstPage()
        sys.exit(self.app.exec_())

if __name__ == "__main__":
    import sys
    controller = MainWindowController()
    controller.execute()
