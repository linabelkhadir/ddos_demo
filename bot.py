import os
import time
import requests

URL = os.getenv("TARGET_URL")

while True:
    try:
        requests.get(URL, timeout=2)
    except:
        pass
    time.sleep(0.5)