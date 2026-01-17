from werkzeug.middleware.proxy_fix import ProxyFix
from flask import Flask, request
from flask_limiter import Limiter
import time

print("SERVER STARTING")

def get_client_ip():
    # Trust the fake IP injected by the gateway
    return request.headers.get("X-Forwarded-For", request.remote_addr)

app = Flask(__name__)

app.wsgi_app = ProxyFix(
    app.wsgi_app,
    x_for=1
)

limiter = Limiter(
    get_client_ip,
    app=app,
    default_limits=["5 per second"]
)

@app.route("/")
def home():
    fake_ip = request.headers.get("X-Forwarded-For")
    real_ip = request.remote_addr
    print("FAKE IP:", fake_ip, "| REAL IP:", real_ip)
    time.sleep(0.05)
    return "Server alive"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
