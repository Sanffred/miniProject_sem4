from PyQt5 import QtWidgets
from Page1_ui import Page1_ui_MainWindow
from Page2_ui1 import Page2_ui_MainWindow, MainWindow as Page2_MainWindow
from Page3_ui import Page3_ui_MainWindow
from Page4_ui import Page4_ui_MainWindow
from Page3_5_ui import Page3_5_ui_MainWindow

import time
from datetime import datetime
import json
import os
import sys


class MainWindowController:
    def __init__(self):
        
        self.app = QtWidgets.QApplication(sys.argv)
        
        self.mainWindow = QtWidgets.QMainWindow()
        self.mainWindow.resize(900, 600)  # Set this to the desired dimensions
        self.stack = QtWidgets.QStackedWidget()
        self.mainWindow.setCentralWidget(self.stack)
        
        self.firstPageWindow = self.createPage(Page1_ui_MainWindow)
        self.secondPageFilesAndFolders = Page1_ui_MainWindow
        self.secondPageWindow = Page2_MainWindow()  # Assuming this is correctly instantiated
        self.thirdPageWindow = self.createPage(Page3_ui_MainWindow)
        self.third_5PageWindow = self.createPage(Page3_5_ui_MainWindow)
        self.fourthPageWindow = self.createPage(Page4_ui_MainWindow)

        self.states = {
            "Google Drive": False,
            "Dropbox": False,
            "Local Directory": False
        }
        
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

        self.thirdPageWindow.ui.gdrive_toggle.stateChanged.connect(self.checkboxChanged)
        self.thirdPageWindow.ui.dropbox_toggle.stateChanged.connect(self.checkboxChanged)
        self.thirdPageWindow.ui.localdir_toggle.stateChanged.connect(self.checkboxChanged)

    def startFourthPage(self):
        self.stack.setCurrentWidget(self.fourthPageWindow)
        self.fourthPageWindow.ui.backup_btn.clicked.connect(self.startSecondPage)

    def startThird_5Page(self):
        self.stack.setCurrentWidget(self.third_5PageWindow)
        self.third_5PageWindow.ui.back_btn.clicked.connect(self.goToThirdPage)
        self.third_5PageWindow.ui.cancel_btn.clicked.connect(self.goBackToFirstPage)

        self.third_5PageWindow.ui.backup_btn.clicked.connect(self.initiateBackupProcess)

        self.third_5PageWindow.ui.When_select_btn.clicked.connect(self.display_backup_datetime)
        self.third_5PageWindow.ui.keep_select_btn.clicked.connect(self.display_keep_date)

    def initiateBackupProcess(self):
        self.goToFourthPage()
        self.run_scheduler('upload_schedule.json', 'delete_schedule.json')


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

    #Page 3 checkbox funtions starts here
    def checkboxChanged(self):
        self.states = {
            "Google Drive": self.thirdPageWindow.ui.gdrive_toggle.isChecked(),
            "Dropbox": self.thirdPageWindow.ui.dropbox_toggle.isChecked(),
            "Local Directory": self.thirdPageWindow.ui.localdir_toggle.isChecked()
        }
        
        print("Current Selection:")
        for storage, checked in self.states.items():
            print(f"{storage}: {'Checked' if checked else 'Unchecked'}")
        
        # Here you can call other functions based on these states
    #     if self.states["Google Drive"]:
    #         self.initiate_gdrive_upload()
    #     if self.states["Dropbox"]:
    #         self.initiate_dropbox_upload()
    #     if self.states["Local Directory"]:
    #         self.initiate_local_upload()

    # def initiate_gdrive_upload(self):
    #     print("Initiating Google Drive upload...")
    #     # Insert code to handle Google Drive uploads here

    # def initiate_dropbox_upload(self):
    #     print("Initiating Dropbox upload...")
    #     # Insert code to handle Dropbox uploads here

    # def initiate_local_upload(self):
    #     print("Initiating Local Directory upload...")
    #     # Insert code to handle Local Directory uploads here

    # page 3 customeCheckBox funtions end here 

    # Page3-5 date time functions start here 

    def display_backup_datetime(self):
        # Get the date and time from the QDateTimeEdit widget
        task_datetime = self.third_5PageWindow.ui.whentobackup.dateTime().toPyDateTime()  # Convert to Python datetime
        formatted_datetime = task_datetime.strftime("%Y-%m-%d %H:%M")
        print(f"Backup scheduled for: {formatted_datetime}")

        MainWindowController.write_schedule_to_file('upload_schedule.json', task_datetime)  # Pass datetime object

    def display_keep_date(self):
        # Get the date from the QDateTimeEdit widget
        task_datetime = self.third_5PageWindow.ui.keepBackups.dateTime().toPyDateTime()  # Convert to Python datetime
        formatted_datetime2 = task_datetime.strftime("%Y-%m-%d %H:%M")
        print(f"Keep backups until: {formatted_datetime2}")

        MainWindowController.write_schedule_to_file('delete_schedule.json', task_datetime)  # Pass datetime object

        
    # Page3-5 date time functions end here 

    
    # scheduling programms and functions 

    @staticmethod
    def read_schedule_from_file(file_path):
        if not os.path.exists(file_path):
            return None
        with open(file_path, 'r') as file:
            schedule_info = json.load(file)
            return datetime.strptime(schedule_info['datetime'], "%Y-%m-%d %H:%M")

    @staticmethod
    def write_schedule_to_file(file_path, task_datetime):
        with open(file_path, 'w') as file:
            schedule_info = {'datetime': task_datetime.strftime("%Y-%m-%d %H:%M")}
            json.dump(schedule_info, file)

    
    def upload_files(self):
        print("Uploading files to the chosen cloud storage based on states...")
        if self.states["Google Drive"]:
            print("Google Drive: Upload process starts...")
            self.initiate_gdrive_upload()
        if self.states["Dropbox"]:
            print("Dropbox: Upload process starts...")
        if self.states["Local Directory"]:
            print("Local Directory: Upload process starts...")

    
    def delete_files(self):
        print("deleting files from the chosen cloud storage based on states...")
        if self.states["Google Drive"]:
            print("Google Drive: deleting process starts...")
        if self.states["Dropbox"]:
            print("Dropbox: deleting process starts...")
        if self.states["Local Directory"]:
            print("Local Directory: deleting process starts...")

    # gdrive upload and deltion functions 

    def initiate_gdrive_upload(self):
        print("Initiating Google Drive upload...")
        # Call authentication and upload methods here
        MainWindowController.authenticate_google_drive()

        service = self.authenticate_google_drive()
        # Assuming self.secondPageWindow stores selected files and folders
        for file_path in self.secondPageFilesAndFolders.ui.selectedFiles:
            self.upload_file(service, file_path)
        for folder_path in self.secondPageFilesAndFolders.ui.selectedFolders:
            self.upload_folder(service, folder_path)


    @staticmethod
    def authenticate_google_drive():
        # Your authentication function with minor modification for inline imports
        import os
        from google.auth.transport.requests import Request
        from google.oauth2.credentials import Credentials
        from google_auth_oauthlib.flow import InstalledAppFlow
        from googleapiclient.discovery import build

        SCOPES = ['https://www.googleapis.com/auth/drive']
        creds = None
        if os.path.exists("token.json"):
            creds = Credentials.from_authorized_user_file("token.json", SCOPES)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
                creds = flow.run_local_server(port=0)
            with open("token.json", "w") as token:
                token.write(creds.to_json())
        return build('drive', 'v3', credentials=creds)
    
    @staticmethod
    def upload_file(service, file_path, parent_id=None):
        # Your file upload function with minor modification for inline imports
        from googleapiclient.http import MediaFileUpload
        from googleapiclient.errors import HttpError
        import os

        file_metadata = {'name': os.path.basename(file_path)}
        if parent_id:
            file_metadata['parents'] = [parent_id]
        media = MediaFileUpload(file_path, resumable=True)
        try:
            file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
            print(f"Uploaded file {file_path} with ID: {file['id']}")
            return file['id']
        except HttpError as error:
            print(f"An error occurred: {error}")
            return None

    @staticmethod
    def upload_folder(service, folder_path, parent_id=None):
        # Your folder upload function with minor modification for inline imports
        import os
        folder_name = os.path.basename(folder_path)
        folder_metadata = {
            'name': folder_name,
            'mimeType': 'application/vnd.google-apps.folder'
        }
        if parent_id:
            folder_metadata['parents'] = [parent_id]
        folder = service.files().create(body=folder_metadata, fields='id').execute()
        folder_id = folder.get('id')
        print(f"Created folder {folder_name} with ID: {folder_id}")

        for item in os.listdir(folder_path):
            item_path = os.path.join(folder_path, item)
            if os.path.isfile(item_path):
                MainWindowController.upload_file(service, item_path, folder_id)
            elif os.path.isdir(item_path):
                MainWindowController.upload_folder(service, item_path, folder_id)
    

    # gdrive uplaod and deltion functions end 
        
    

    @staticmethod
    def check_and_execute(task_file, action):
        scheduled_time = MainWindowController.read_schedule_from_file(task_file)
        if scheduled_time and datetime.now() >= scheduled_time:
            action()
            os.remove(task_file)  # Remove the file after executing to prevent re-execution

    def run_scheduler(self, upload_file_path, delete_file_path):
        import threading
        def scheduler_loop():
            while True:
                if os.path.exists(upload_file_path):
                    self.check_and_execute(upload_file_path, self.upload_files)
                if os.path.exists(delete_file_path):
                    self.check_and_execute(delete_file_path, self.delete_files)
                time.sleep(60)  # Check every minute

        threading.Thread(target=scheduler_loop, daemon=True).start()


        #Daemon Thread: I’ve set the thread as a daemon. Daemon threads are threads that run in the background and do not prevent the program from exiting. This is important because if your main application quits, you probably want these background tasks to stop as well.

    # End of the scheduling programms and functions 

    def execute(self):
        self.mainWindow.show()
        self.startFirstPage()
        sys.exit(self.app.exec_())

if __name__ == "__main__":

    controller = MainWindowController()
    controller.execute()
