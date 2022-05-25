# importing modules
import json
import time
from plyer import notification

data = open('tasks.json') # reading task.json file which stores data
tasks = json.load(data) # packing tasks in a python dict

if __name__ == "__main__":
    while True:
        for task in tasks:
            notification.notify(title="Task Remainder", message=task['task'], timeout=8, app_icon="img/app-icon.ico") # notifies task
            time.sleep(60) # Takes break of 60 secs
