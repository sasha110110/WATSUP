from flask import Flask
import json
from flask import request
import requests

instance_id="instance48357"
token="c5mz6bh47ltnl6ka"
url = "https://api.ultramsg.com/instance48357/messages/chat"

app = Flask(__name__)

@app.route('/', methods=['POST'])
def home():
    res=""
    if request.method == 'POST':
        msg=request.get_json(force=True)
        if msg["data"] is not None:
            
            res+=str(msg['data'])

            payload = f"token={token}&to=%2B79500310422&body=res"
            payload = payload.encode('utf8').decode('iso-8859-1')
            headers = {'content-type': 'application/x-www-form-urlencoded'}
            response = requests.request("POST", url, data=payload, headers=headers)
            print(response)
            return "ok"

