import requests
dosya=open("kritikVeri.txt","r")
kritikVeri=dosya.read()
dosya.close()
for i in kritikVeri.split(" "):
    url="http://192.168.43.161/ABY_"+str(i)
    requests.get(url)