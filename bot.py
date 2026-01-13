import requests
import time
import os

URL = os.getenv("TARGET_URL", "http://host.docker.internal:5001")
PROFILE = os.getenv("PROFILE", "vm")

PROFILES = {
    "vm": {
        "sleep": 0.5,
        "timeout": 2,
        "headers": {"User-Agent": "Simulated-VM"}
    },
    "cloud": {
        "sleep": 0.1,
        "timeout": 1,
        "headers": {"User-Agent": "Simulated-Cloud"}
    }
}

profile = PROFILES[PROFILE]

print(f"[BOT] profile={PROFILE}")

while True:
    try:
        requests.get(
            URL,
            headers=profile["headers"],
            timeout=profile["timeout"]
        )
    except:
        pass
    time.sleep(profile["sleep"])