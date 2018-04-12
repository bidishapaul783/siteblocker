import time
from datetime import datetime as dt
hosts_temp="hosts"
hosts_path="C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
website_block=["www.facebook.com","facebook.com","www.youtube.com","youtube.com","www.squarespace.com","squarespace.com"]
while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,10):
        print ("workinh hrs...")
        with open(hosts_path,'r+') as file:
            content=file.read();
            for web in website_block:
                if web in content:
                    pass
                else:
                    file.write(redirect+" "+web+'\n')
    else:
        with open(hosts_path,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_block):
                    file.write(line)
            file.truncate()
        print("fun time...")
    time.sleep(5)
