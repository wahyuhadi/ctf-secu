import requests 
api = "http://45.77.98.246:57777/ecommerce/login"
body = 	{
	"username" : "seculab",
	"password" : "seculab", 
}

data = requests.post(api, json=body)
print (data.text)