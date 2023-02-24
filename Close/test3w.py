import os
from googleapiclient.discovery import build
#from googleapiclient import discovery
from google.oauth2.service_account import Credentials
from googleapiclient.http import MediaFileUpload


class GoogleDriveService:
    def __init__(self, cred_path):
        self._SCOPES = ['https://www.googleapis.com/auth/drive']
        self._credentials = Credentials.from_service_account_file(cred_path, scopes=self._SCOPES)
        self._service = build('drive', 'v3', credentials=self._credentials)

    def get_service(self):
        return self._service


def upload_file(service, file_path, folder_id, file_name=None, mime_type=None):
    if not file_name:
        file_name = os.path.basename(file_path)
    if not mime_type:
        mime_type = 'application/octet-stream'
    file_metadata = {'name': file_name, 'parents': [folder_id]}
    media = MediaFileUpload(file_path, mimetype=mime_type)
    service.files().create(body=file_metadata, media_body=media, fields='id').execute()


if __name__ == "__main__":
    cred_path = os.path.join(os.path.dirname(__file__), 'credential.json')
    folder_id = '1iJszGHPp1NXtpjtJwDHaayRck418RmnK'
    service = GoogleDriveService(cred_path).get_service()
    file_path = '/Users/kajenthavaraj/Trojan Horse SaaS/01.jpg'
    file_name = os.path.basename(file_path)
    mime_type = 'image/png'
    upload_file(service, file_path, folder_id, file_name, mime_type)
