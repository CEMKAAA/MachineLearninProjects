import os
import shutil
import datetime
import schedule
import time

source_dir = "C:/Users/Cem/Pictures/Screenshots"
destination_dir = "C:/Users/Cem/Pictures/Backups"

def copy_folder_to_directory(source, dest):
    today = datetime.date.today()
    dest_dir = os.path.join(dest, str(today))
    
    try:
        shutil.copytree(source, dest_dir)
        print(f"folder copied to destination dir: {dest_dir}")
    except FileExistsError as e:
        print(f"folder already exist in the {dest}")
        
schedule.every().day.at("17:18").do(lambda: copy_folder_to_directory(source_dir, destination_dir))
        
while True:
    schedule.run_pending()
    time.sleep(60)