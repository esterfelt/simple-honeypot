from flask import request
from datetime import datetime

def log(username, password):
    SUSPICIOUS = ["'", '"', '--', ';', '<', '>', 'script']
    danger = any(s in username + password for s in SUSPICIOUS)

    with open('logs.txt', 'a') as file:
        # Logs will contain date, ip address and danger mark
        file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {request.remote_addr} - {danger} - {username} - {password} \n")