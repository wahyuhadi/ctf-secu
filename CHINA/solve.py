import requests
import json
from time import sleep
urla = 'http://45.77.98.246:57777/binding/loginbot/'
bit = 'https://bittrex.com/api/v1.1/public/getmarketsummary?market=usdt-btc'
headers = {'Content-Type': 'application/json'}
url = requests.get(bit)
#sleep(30)
dump = json.loads(url.text)
key = (dump['result'][0]['Last'])
tes = {"password" : key }
print (tes)
resp = requests.post(urla, json=tes)
print (resp.text)
