import requests
url="https://www.btcturk.com/api/ticker"
cikti=  requests.get(url,verify=False).json()[0]['last']
if int(cikti)<40000:
    print "Fyat dustu"
    payload={"api_key":"4642e3","api_secret":"4HxSMkDdy2HnHak1","to":"905379126183","from":"ABY Bilgi Islem","text":"fiyatlar dustu be"}
    url="https://rest.nexmo.com/sms/json"
    requests.post(url=url,data=payload,verify=False)

