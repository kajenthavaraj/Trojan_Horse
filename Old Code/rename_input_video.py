import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials


######link to google sheet######
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)
sheet1 = client.open("Trojan Horse Automation")
sheet2 = sheet1.worksheet("Edit")

######Get info from google sheet######
video_title = sheet2.col_values(1)

os.chdir(r'C:\Users\kajen\OneDrive\Desktop\Trojan_Horse_Marketing\Rename_Videos')

existing_files = os.listdir()

i = 1
for f in existing_files:
    file_name, file_ext = os.path.splitext(f)
    print(file_name)

    new_name = "in_" + video_title[i] + ".mp4"

    os.rename(f, new_name)
    i = i+1











# import pathlib

# def rename_videos():
#     path = pathlib.Path('.') / "photos"
#     for folder in path.iterdir():
#         if folder.is_dir():
#             counter = 1
#             for file in folder.iterdir():
#                 if file.is_file():
#                     new_file = "from automation sheet"
#                     print(folder.name)
#                     file.rename(path / folder.name / new_file)
#                     #file.rename(path / folder.name / new_file)
#                     counter +=1

# if __name__ == "__main__":
#     rename_videos()