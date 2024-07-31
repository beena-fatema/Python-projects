import os
import shutil
import datetime
import schedule
import time
source_dir="C:/Users/Dell/Desktop/General"
destination_dir="C:/Users/Dell/Desktop/General"
def copy_folder(source,dest):
    today=datetime.date.today()
    dest_dir=os.path.join(dest,str(today))
    try:
        shutil.copytree(source,dest_dir)
        print(f"folder copied to:{dest_dir}")
    except FileExistsError:
        print(f"folder already exist in the {dest}")
schedule.every().day.at("17:55").do(lambda:copy_folder(source_dir,destination_dir))
while True:
    schedule.run_pending()
    time.sleep(60)