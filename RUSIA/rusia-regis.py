import requests 
api = "http://45.77.98.246:57777/ecommerce/register"
body = 	{
	"username" : "seculab",
	"password" : "seculab", 
	"account" : "seculab" 
}

data = requests.post(api, json=body)
print (data.text)