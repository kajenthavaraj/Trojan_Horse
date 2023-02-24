from selenium import webdriver
import io
import os

from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
from google_auth_oauthlib.flow import Flow, InstalledAppFlow
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload
from google.auth.transport.requests import Request


class GoogleDriveService:
    def __init__(self):
        self._SCOPES=['https://www.googleapis.com/auth/drive']

        _base_path = os.path.dirname(__file__)
        _credential_path=os.path.join(_base_path, 'credential.json')
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = _credential_path

    def build(self):
        creds = ServiceAccountCredentials.from_json_keyfile_name(os.getenv("GOOGLE_APPLICATION_CREDENTIALS"), self._SCOPES)
        service = build('drive', 'v3', credentials=creds)

        return service

def file_upload(service, file_path, mime_type):
    #for file_name, mime_type in zip(file_names, mime_types):
    folder_id = '1iJszGHPp1NXtpjtJwDHaayRck418RmnK'
    file_metadata = {
        'name': file_name,
        'parents': [folder_id]
    }

    media = MediaFileUpload(file_path, mimetype = mime_type)

    service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id'
    ).execute()


# Create a webdriver object
driver = webdriver.Chrome()

# Navigate to a web page
driver.get('http://www.ionic-x.com')

i=1
screenshot_name = 'screenshot_{0}.png'.format(i)

#####VM_PATH = '/Users/kajenthavaraj/Trojan Horse SaaS'

#VM_PATH = input("What is the VM Path: ")
#VM_PATH = "kajenthavaraj@{0}".format(VM_NAME)  - VM_NAME = instance-1

VM_PATH = 'kajenthavaraj@instance-1'

mime_type = 'image/png'

file_path = '{0}/{1}'.format(VM_PATH, screenshot_name)


#Get service
service = GoogleDriveService().build()


#Upload PNG to google folder - https://drive.google.com/drive/folders/1iJszGHPp1NXtpjtJwDHaayRck418RmnK
file_upload(service, file_path, mime_type)


# Take a screenshot
driver.save_screenshot(screenshot_name)


#Upload an image to google drive to look at later (testing)

# Close the web browser
driver.quit()







# 1.) Get all the tabs
# 2.) Go to tab 1 (wait 5 seconds)
# 3.) Start recording
# 4.) Exectute tab switches and scrolling
# 5.) Stop recording & save to computer
# 6.) Create webpage
# 7.) Upload video to webpage
