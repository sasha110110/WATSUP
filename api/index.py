from flask import Flask
import json
from flask import request
import requests

instance_id="instance48357"
token="c5mz6bh47ltnl6ka"
url = "https://api.ultramsg.com/instance48357/messages/chat"

app = Flask(__name__)

@app.route('/', methods=['POST', "GET"])
def home():
    res=""
    if request.method == 'POST':
        result=json['data']
        res+=str(resuult)
        

        payload = f"token={token}&to=%2B79500310422&body=result"
        payload = payload.encode('utf8').decode('utf8')#('iso-8859-1')
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = requests.request("POST", url, data=payload, headers=headers)
        return ""
    return res
