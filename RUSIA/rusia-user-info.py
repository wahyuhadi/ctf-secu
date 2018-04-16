import requests 
api = "http://45.77.98.246:57777/ecommerce/action/getuserinfo"

headers = {
    "usertoken" : "eyJpZCI6MzQsInVzZXJuYW1lIjoic2VjdWxhYiIsInBhc3N3b3JkIjoic2VjdWxhYiJ9"
}
data = requests.get(api, headers=headers)
print (data.text)