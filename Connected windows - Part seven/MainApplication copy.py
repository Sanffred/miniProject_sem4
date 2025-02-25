import logging
logging.basicConfig(level=logging.DEBUG, filename='app.log', filemode='w',
                    format='%(name)s - %(levelname)s - %(message)s')

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog, QMainWindow
from Page1_ui import Page1_ui_MainWindow
from Page2_ui1 import Page2_ui_MainWindow
from Page3_ui import Page3_ui_MainWindow
from Page4_ui import Page4_ui_MainWindow
from Page3_5_ui import Page3_5_ui_MainWindow
import time
from datetime import datetime
import json
import os
import sys
from googleapiclient.http import MediaFileUpload
from googleapiclient.errors import HttpError
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import dropbox
from dropbox.exceptions import ApiError
import logging
class MainWindowController:
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)   
        self.mainWindow = QtWidgets.QMainWindow()
        self.mainWindow.resize(900, 600)  
        self.stack = QtWidgets.QStackedWidget()
        self.mainWindow.setCentralWidget(self.stack)       
        self.firstPageWindow = self.createPage(Page1_ui_MainWindow)
        self.secondPageWindow = self.createPage(Page2_ui_MainWindow)  
        self.thirdPageWindow = self.createPage(Page3_ui_MainWindow)
        self.third_5PageWindow = self.createPage(Page3_5_ui_MainWindow)
        self.fourthPageWindow = self.createPage(Page4_ui_MainWindow)
        self.states = {
            "Google Drive": False,
            "Dropbox": False,
            "Local Directory": False
        }
        self.droppBox_uploaded_files = []
        self.droppBox_uploaded_folders = []
        self.stack.addWidget(self.firstPageWindow)
        self.stack.addWidget(self.secondPageWindow)
        self.stack.addWidget(self.thirdPageWindow)
        self.stack.addWidget(self.third_5PageWindow)
        self.stack.addWidget(self.fourthPageWindow)
        with open("TOKEN.txt" , "r") as f:
            self.access_token = f.read()
    def createPage(self, ui_class):
        page = QtWidgets.QMainWindow()
        ui = ui_class()
        ui.setupUi(page)
        page.ui = ui
        return page
    def startFirstPage(self):
        self.firstPageWindow.ui.backup_btn.clicked.connect(self.startSecondPage)  
        self.stack.setCurrentWidget(self.firstPageWindow)
    def startSecondPage(self):
        self.stack.setCurrentWidget(self.secondPageWindow)
        self.secondPageWindow.ui.cancel_btn.clicked.connect(self.goBackToFirstPage)
        self.secondPageWindow.ui.next_btn.clicked.connect(self.goToThirdPage)
        self.secondPageWindow.ui.select_files.clicked.connect(self.selectFiles)
        self.secondPageWindow.ui.select_folders.clicked.connect(self.selectFolders)
        self.secondPageWindow.ui.display_selected_files_listWidget.itemClicked.connect(self.confirmRemoveSelectedItem)
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
        self.stack.setCurrentWidget(self.firstPageWindow) 
    def goToThirdPage(self):
        self.startThirdPage()
    def goToThird_5Page(self):
        self.startThird_5Page()
    def goToSecondPage(self):
        self.startSecondPage()
    def goToFourthPage(self):
        self.startFourthPage()
    def selectFiles(self):
        files, _ = QFileDialog.getOpenFileNames(self.secondPageWindow, "Select Files")
        self.secondPageWindow.ui.selectedFiles.extend(files)
        self.updateSelectedPathsList()
        self.printCurrentSelection()
    def selectFolders(self):
        folder = QFileDialog.getExistingDirectory(self.secondPageWindow, "Select Folder")
        if folder:
            self.secondPageWindow.ui.selectedFolders.append(folder)
            self.updateSelectedPathsList()
            self.printCurrentSelection()
    def updateSelectedPathsList(self):
        self.secondPageWindow.ui.display_selected_files_listWidget.clear()
        for file in self.secondPageWindow.ui.selectedFiles:
            self.secondPageWindow.ui.display_selected_files_listWidget.addItem(file)
        for folder in self.secondPageWindow.ui.selectedFolders:
            self.secondPageWindow.ui.display_selected_files_listWidget.addItem(folder)
    def confirmRemoveSelectedItem(self, item):
        response = QMessageBox.question(self.secondPageWindow, "Remove Item", "Are you sure you want to remove this item?")
        if response == QMessageBox.Yes:
            self.removeSelectedItem(item.text())
    def removeSelectedItem(self, text):
        if text in self.secondPageWindow.ui.selectedFiles:
            self.secondPageWindow.ui.selectedFiles.remove(text)
        elif text in self.secondPageWindow.ui.selectedFolders:  
            self.secondPageWindow.ui.selectedFolders.remove(text)
        self.updateSelectedPathsList()
        self.printCurrentSelection()
    def printCurrentSelection(self):
        print("Current Files:")
        for file in self.secondPageWindow.ui.selectedFiles:
            print(file)
        print("Current Folders:")
        for folder in self.secondPageWindow.ui.selectedFolders:
            print(folder)
    def checkboxChanged(self):
        self.states = {
            "Google Drive": self.thirdPageWindow.ui.gdrive_toggle.isChecked(),
            "Dropbox": self.thirdPageWindow.ui.dropbox_toggle.isChecked(),
            "Local Directory": self.thirdPageWindow.ui.localdir_toggle.isChecked()
        }      
        print("Current Selection:")
        for storage, checked in self.states.items():
            print(f"{storage}: {'Checked' if checked else 'Unchecked'}")
    def display_backup_datetime(self):
        task_datetime = self.third_5PageWindow.ui.whentobackup.dateTime().toPyDateTime()  
        formatted_datetime = task_datetime.strftime("%Y-%m-%d %H:%M")
        print(f"Backup scheduled for: {formatted_datetime}")
        MainWindowController.write_schedule_to_file('upload_schedule.json', task_datetime)  
        logging.info("Path to upload_schedule.json: " + os.path.abspath("upload_schedule.json"))
        logging.info("Current working directory: " + os.getcwd())
    def display_keep_date(self):
        task_datetime = self.third_5PageWindow.ui.keepBackups.dateTime().toPyDateTime()  
        formatted_datetime2 = task_datetime.strftime("%Y-%m-%d %H:%M")
        print(f"Keep backups until: {formatted_datetime2}")
        MainWindowController.write_schedule_to_file('delete_schedule.json', task_datetime)  
        logging.info("Path to delete_schedule.json: " + os.path.abspath("delete_schedule.json"))
        logging.info("Current working directory: " + os.getcwd())
    @staticmethod
    def read_schedule_from_file(file_path):
        if not os.path.exists(file_path):
            return None
        with open(file_path, 'r') as file:
            logging.info("reading the schedule: ")
            schedule_info = json.load(file)
            return datetime.strptime(schedule_info['datetime'], "%Y-%m-%d %H:%M")
    @staticmethod
    def write_schedule_to_file(file_path, task_datetime):
        with open(file_path, 'w') as file:
            logging.info("writing the schedule: " + os.getcwd())
            schedule_info = {'datetime': task_datetime.strftime("%Y-%m-%d %H:%M")}
            json.dump(schedule_info, file)  
    def upload_files(self):
        print("Uploading files to the chosen cloud storage based on states...")
        if self.states["Google Drive"]:
            print("Google Drive: Upload process starts...")
            logging.info("entered the upload_files() function: ")
            self.initiate_gdrive_upload()
        if self.states["Dropbox"]:
            print("Dropbox: Upload process starts...")
            self.initiate_dropbox_upload()
        if self.states["Local Directory"]:
            print("Local Directory: Upload process starts...")  
    def delete_files(self):
        print("deleting files from the chosen cloud storage based on states...")
        if self.states["Google Drive"]:
            print("Google Drive: deleting process starts...")
            self.initiate_gdrive_deletion()
        if self.states["Dropbox"]:
            print("Dropbox: deleting process starts...")
            self.initiate_dropbox_delete()
        if self.states["Local Directory"]:
            print("Local Directory: deleting process starts...")
    def initiate_dropbox_upload(self):
        """Initialize the Dropbox upload process."""
        print("Initiating Dropbox upload...")
        self.authenticate_dropbox()
        try:
            logging.info("Starting Dropbox upload...")
            if hasattr(self.secondPageWindow.ui, 'selectedFiles'):
                for file_path in self.secondPageWindow.ui.selectedFiles:
                    self.upload_file_toDropbox(file_path)
            else:
                print("No files selected for upload.")
            if hasattr(self.secondPageWindow.ui, 'selectedFolders'):
                for folder_path in self.secondPageWindow.ui.selectedFolders:
                    self.upload_folder_toDropbox(folder_path)
            else:
                print("No folders selected for upload.")
            logging.info("Upload completed successfully.")
        except Exception as e:
            logging.error(f"Error during Dropbox upload: {e}")   
    def authenticate_dropbox(self):
        """Authenticate with the Dropbox API using the provided access token."""
        try:
            self.dbx = dropbox.Dropbox(self.access_token)
            # Check that the access token is valid
            self.dbx.users_get_current_account()
            print("Successfully authenticated with Dropbox.")
        except (dropbox.exceptions.AuthError, dropbox.exceptions.ApiError) as e:
            logging.error("Failed to authenticate with Dropbox: {}".format(e))
            raise Exception("Authentication failed")
    def upload_folder_toDropbox(self, folder_path):       
        folder_name = os.path.basename(folder_path)
        logging.info(f"Starting upload for folder: {folder_name}")
        dropbox_folder_path = f"/{folder_name}"
        self.droppBox_uploaded_folders.append(dropbox_folder_path)  
        print(f"Added to uploaded_folders: {dropbox_folder_path}")
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file.lower() == 'desktop.ini':
                    print(f"Skipping system file: {file}")
                    continue
                local_path = os.path.join(root, file)
                relative_path = os.path.relpath(local_path, folder_path)
                dropbox_path = f"/{folder_name}/{relative_path}"
                try:
                    self.upload_file_toDropbox(local_path, dropbox_path)
                except Exception as e:
                    logging.error(f"Failed to upload file {local_path}: {e}")
                    print(f"Error uploading {local_path}: {e}")
    def upload_file_toDropbox(self, file_path, destination_path=None):
        """Upload a single file to Dropbox. If no destination_path is provided, upload to root."""
        if destination_path is None:
            filename = os.path.basename(file_path)
            destination_path = f"/{filename}"
        logging.info(f"Preparing to upload file: {file_path} to {destination_path}")
        with open(file_path, 'rb') as file:
            try:
                self.dbx.files_upload(file.read(), destination_path, mode=dropbox.files.WriteMode('overwrite'))
                print(f"Uploaded file to {destination_path}")
                logging.info(f"Uploaded file to {destination_path}")
                self.droppBox_uploaded_files.append(destination_path)  
                print(f"Added to uploaded_files: {destination_path}")
            except dropbox.exceptions.ApiError as e:
                logging.error(f"Failed to upload file {file_path}: {e}")
                print(f"Error uploading {file_path}: {e}")
    def initiate_dropbox_delete(self):
        """Initialize the Dropbox deletion process."""
        print("Initiating Dropbox delete...")
        self.authenticate_dropbox()
        try:
            logging.info("Starting Dropbox deletion...")
            if hasattr(self, 'droppBox_uploaded_files'):
                for destination_path in self.droppBox_uploaded_files:
                    if destination_path.startswith("/"):  
                        self.delete_file_from_dropbox(destination_path)
                    else:
                        print(f"Invalid Dropbox path: {destination_path}")
            else:
                print("No files selected for deletion.")
            if hasattr(self, 'droppBox_uploaded_folders'):
                for folder_path in self.droppBox_uploaded_folders:
                    if folder_path.startswith("/"):  
                        self.delete_folder_from_dropbox(folder_path)
                    else:
                        print(f"Invalid Dropbox path: {folder_path}")
            else:
                print("No folders selected for deletion.")
            logging.info("Deletion completed successfully.")
        except Exception as e:
            logging.error(f"Error during Dropbox deletion: {e}")
    def delete_file_from_dropbox(self, destination_path):
        """Delete a specific file from Dropbox based on its Dropbox path."""
        try:
            self.dbx.files_delete_v2(destination_path)
            print(f"Deleted file at {destination_path}")
            logging.info(f"Deleted file at {destination_path}")
        except dropbox.exceptions.ApiError as e:
            logging.error(f"Failed to delete file {destination_path}: {e}")
            print(f"Error deleting {destination_path}: {e}")
    def delete_folder_from_dropbox(self, folder_name):
        """Delete a folder and all its contents from Dropbox, based on the folder name."""
        logging.info(f"Starting deletion for folder: {folder_name}")
        folder_path = f"/{folder_name}"
        try:
            entries = self.dbx.files_list_folder(folder_path, recursive=True).entries
            for entry in reversed(entries):  # Reverse to delete files before folders
                if isinstance(entry, dropbox.files.FileMetadata):
                    self.delete_file_from_dropbox(entry.path_lower)
                elif isinstance(entry, dropbox.files.FolderMetadata):
                    self.delete_file_from_dropbox(entry.path_lower)
            self.dbx.files_delete_v2(folder_path)
            print(f"Deleted folder {folder_path}")
            logging.info(f"Deleted folder {folder_path}")
        except dropbox.exceptions.ApiError as e:
            logging.error(f"Failed to delete folder {folder_path}: {e}")
            print(f"Error deleting {folder_path}: {e}")
    def initiate_gdrive_upload(self):
        print("Initiating Google Drive upload...")
        service = self.authenticate_google_drive()
        try:
            logging.info("Starting Google Drive upload...")
            if hasattr(self.secondPageWindow.ui, 'selectedFiles'):
                for file_path in self.secondPageWindow.ui.selectedFiles:
                    self.upload_file_toGoogle(service, file_path)
            else:
                print('some file/folder error')
            if hasattr(self.secondPageWindow.ui, 'selectedFolders'):
                for folder_path in self.secondPageWindow.ui.selectedFolders:
                    self.upload_folder_toGoogle(service, folder_path)
            else:
                print('some file/folder error')

            logging.info("Upload completed successfully.")
        except Exception as e:
            logging.error("Error during Google Drive upload: {}".format(e))
    @staticmethod
    def authenticate_google_drive():
        if getattr(sys, 'frozen', False):
            datadir = sys._MEIPASS
        else:
            datadir = os.path.dirname(os.path.abspath(__file__))
        SCOPES = ['https://www.googleapis.com/auth/drive']
        creds = None
        token_paths = os.path.join(datadir, 'token.json') 
        if os.path.exists(token_paths):
            creds = Credentials.from_authorized_user_file(token_paths, SCOPES)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                print("Current Working Directory to check the path of credientals.jsons path :", os.getcwd())
                credentials_path = os.path.join(datadir, 'credentials.json')
                flow = InstalledAppFlow.from_client_secrets_file(credentials_path, SCOPES)
                creds = flow.run_local_server(port=0)
            with open("token.json", "w") as token:
                token.write(creds.to_json())
        return build('drive', 'v3', credentials=creds)
    @staticmethod
    def upload_file_toGoogle(service, file_path, parent_id=None):
        """Upload a file to Google Drive."""
        file_name = os.path.basename(file_path)
        file_metadata = {'name': file_name}
        if parent_id:
            file_metadata['parents'] = [parent_id]
        media = MediaFileUpload(file_path, resumable=True)
        try:
            file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
            print(f"Uploaded file {file_name} with ID: {file['id']}")
            return file['id']
        except HttpError as error:
            print(f"An error occurred: {error}")
            print(error.resp.status, error.content) 
        except Exception as e:
            print(f"An unexpected error occurred: {e}") 
    @staticmethod
    def upload_folder_toGoogle(service, folder_path, parent_id=None):
        """Create a folder in Google Drive and upload its contents."""
        folder_name = os.path.basename(folder_path)
        folder_metadata = {
            'name': folder_name,
            'mimeType': 'application/vnd.google-apps.folder'
        }
        if parent_id:
            folder_metadata['parents'] = [parent_id]
        try:
            folder = service.files().create(body=folder_metadata, fields='id').execute()
            folder_id = folder.get('id')
            print(f"Created folder {folder_name} with ID: {folder_id}")

            for item in os.listdir(folder_path):
                item_path = os.path.join(folder_path, item)
                if os.path.isfile(item_path):
                    MainWindowController.upload_file(service, item_path, folder_id)
                elif os.path.isdir(item_path):
                    MainWindowController.upload_folder(service, item_path, folder_id)
        except HttpError as error:
            print(f"An error occurred: {error}")
            print(error.resp.status, error.content) 
        except Exception as e:
            print(f"An unexpected error occurred: {e}")  
    def initiate_gdrive_deletion(self):
        print("Initiating Google Drive deletion...")
        service = self.authenticate_google_drive()
        try:
            logging.info("Starting Google Drive deletion...")
            # Deleting selected files
            if hasattr(self.secondPageWindow.ui, 'selectedFiles'):
                for file_path in self.secondPageWindow.ui.selectedFiles:
                    self.delete_file_fromGoogle(service, file_path)
            else:
                print('some file/folder error')
            if hasattr(self.secondPageWindow.ui, 'selectedFolders'):
                for folder_path in self.secondPageWindow.ui.selectedFolders:
                    self.delete_folder_fromGoogle(service, folder_path)
            else:
                print('some file/folder error')
            logging.info("Deletion completed successfully.")
        except Exception as e:
            logging.error("Error during Google Drive deletion: {}".format(e))
    @staticmethod
    def delete_file_fromGoogle(service, file_path):
        """Delete a file from Google Drive given the file ID."""
        file_name = os.path.basename(file_path)
        try:
            search_result = service.files().list(q=f"name = '{file_name}'",
                                                spaces='drive',
                                                fields='files(id)').execute()
            file_id = search_result.get('files', [])[0].get('id')
            service.files().delete(fileId=file_id).execute()
            print(f"Deleted file: {file_path}")
        except HttpError as error:
            print(f"An error occurred: {error}")
        except IndexError:
            print(f"No file found with name {file_name}")
    @staticmethod
    def delete_folder_fromGoogle(service, folder_path):
        """Delete a folder from Google Drive given the folder ID."""
        folder_name = os.path.basename(folder_path)
        try:
            search_result = service.files().list(q=f"mimeType = 'application/vnd.google-apps.folder' and name = '{folder_name}'",
                                                spaces='drive',
                                                fields='files(id)').execute()
            folder_id = search_result.get('files', [])[0].get('id')
            service.files().delete(fileId=folder_id).execute()
            print(f"Deleted folder: {folder_path}")
        except HttpError as error:
            print(f"An error occurred: {error}")
        except IndexError:
            print(f"No folder found with name {folder_name}")
    @staticmethod
    def check_and_execute(task_file, action):
        scheduled_time = MainWindowController.read_schedule_from_file(task_file)
        logging.info("Entered the check_and_execute() function .......... ")
        if scheduled_time and datetime.now() >= scheduled_time:
            action()
            os.remove(task_file)
    def run_scheduler(self, upload_file_path, delete_file_path):
        import threading
        logging.info("scheduler functions has been called  ")
        def scheduler_loop():
            logging.info("entered the scheduler loop function   ")
            while True:
                logging.info("entered the scheduler loop   ")
                if os.path.exists(upload_file_path):
                    self.check_and_execute(upload_file_path, self.upload_files)
                if os.path.exists(delete_file_path):
                    self.check_and_execute(delete_file_path, self.delete_files)
                time.sleep(30)  
        threading.Thread(target=scheduler_loop, daemon=True).start()
    def execute(self):
        self.mainWindow.show()
        self.startFirstPage()
        sys.exit(self.app.exec_())
if __name__ == "__main__":
    controller = MainWindowController()
    controller.execute()
