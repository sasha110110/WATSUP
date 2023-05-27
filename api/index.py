from flask import Flask
import json
from flask import request
import requests

instance_id="instance48357"
token="c5mz6bh47ltnl6ka"
chatID="+79500310422"
url = f"https://api.ultramsg.com/instance48357/messages/chat/?token={token}"

app = Flask(__name__)

@app.route(f'/{token}', methods=['POST'])
def home():
    res=""
    if request.method == 'POST':
        msg=request.json
        #if msg["data"] != []:
            
        res=str(msg) #str(msg['data'])

        headers = {'content-type': 'application/json'}
        data = {"to" : chatID, "body" : res} 
        response = requests.request("POST", url, data=json.dumps(data), headers=headers)

        print(response.text)
        return "ok"

