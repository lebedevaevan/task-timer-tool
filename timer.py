import time
import json
from datetime import datetime

with open("config/settings.json") as f:
    settings = json.load(f)

task = input("Task name: ")
start = time.time()
input("Press ENTER to stop the timer...")
end = time.time()

duration = end - start
formatted = time.strftime(settings["time_format"], time.gmtime(duration))

with open(settings["log_file"], "a") as log:
    log.write(f"{datetime.now()} | {task} | {formatted}\n")

print(f"Task '{task}' took {formatted}")
