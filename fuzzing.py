import requests
dosya=open("fuzzingDosya.txt","r")
icerik=dosya.read()
dosya.close()
for i in icerik.split("\n"):
    url="http://192.168.43.161/"+str(i)
    sonuc=requests.get(url)
    if "200" in str(sonuc.status_code):
        print "[+]Dizin var:",str(i)
        print sonuc.content
    else:
        print "[+]Dizin yok:",str(i)
    print "======"