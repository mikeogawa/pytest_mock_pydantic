import requests
import json

def send_info(url,x):
    res = format_info(x)
    requests.post(url,data=res)

def format_info(x):
    return json.dumps(x)
