import ffmpeg
import subprocess
from pynput.keyboard import Key, Controller
import time
import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials

######link to google sheet######
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)
sheet1 = client.open("Trojan Horse Automation")
sheet2 = sheet1.worksheet("Edit")

ads_status_col = sheet2.col_values(6)

video_title = sheet2.col_values(1)

def running_ads_edit(brand_name):
    os.chdir(r"C:\Users\kajen\OneDrive\Desktop\Trojan_Horse_Marketing\Video_Editing_Automation")

    #take audio from pre recorded video and overlay with screen record
    subprocess.run('cmd /c "ffmpeg -i in_%s.mp4 -i TH_RunningAdsv3.mp4 -c copy -map 0:0 -map 1:1 -shortest merge.mp4"'%(brand_name))

    #overlay both videos
    subprocess.run('cmd /c "ffmpeg -i   merge.mp4 -vf   "movie=TH_RunningAdsv3.mp4, scale=350: -1 [inner]; [in][inner] overlay =10: main_h-(overlay_h + 10) [out]" %s.mp4"'%(brand_name))

    print(brand_name)

    os.remove("merge.mp4")
    os.remove('in_%s.mp4'%(brand_name))
    os.chdir(r"C:\Users\kajen\OneDrive\Desktop\Trojan_Horse_Marketing")

def not_running_ads_edit(brand_name):
    os.chdir(r"C:\Users\kajen\OneDrive\Desktop\Trojan_Horse_Marketing\Video_Editing_Automation")

    #take audio from pre recorded video and overlay with screen record
    subprocess.run('cmd /c "ffmpeg -i in_%s.mp4 -i TH_notrunningadsv2.mp4 -c copy -map 0:0 -map 1:1 -shortest merge.mp4"'%(brand_name))

    #overlay both videos
    subprocess.run('cmd /c "ffmpeg -i   merge.mp4 -vf   "movie=TH_notrunningadsv2.mp4, scale=350: -1 [inner]; [in][inner] overlay =10: main_h-(overlay_h + 10) [out]" %s.mp4"'%(brand_name))

    print(brand_name)

    os.remove("merge.mp4")
    os.remove("in_%s.mp4"%(brand_name))
    os.chdir(r"C:\Users\kajen\OneDrive\Desktop\Trojan_Horse_Marketing")

i = 1
while i < len(video_title):
    #get ads status from google sheet
    ads_status = ads_status_col[i]

    if ads_status == "yes" or ads_status == "Yes":
        running_ads_edit(video_title[i])

    elif ads_status == "no" or ads_status == "No":
        not_running_ads_edit(video_title[i])

    #sheet2.update_cell(i+1, 8, "MADE")
    i+=1

# i = 0
# while i < len(brand):
#     #get ads status from google sheet
#     ads_status = ads_status_col[i + 1]

#     if ads_status == "yes" or ads_status == "Yes":
#         running_ads_edit(brand[i])

#     elif ads_status == "no" or ads_status == "No":
#         not_running_ads_edit(brand[i])

#     sheet2.update_cell(i+2, 8, "MADE")
#     i+=1

print("Program Completed Successfully")