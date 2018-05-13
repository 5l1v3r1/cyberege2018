import requests
dosya=open("linkler.txt","r")
icerik=dosya.read()
dosya.close()
dosya=open("cyberstruggle","r")
icerik2=dosya.read()
dosya.close()
csListe=[]
for i in icerik2.split("\n"):
    csListe.append(str(i))
for i in icerik.split("\n"):
    sonuc=requests.get(i,verify=False)
    for j in csListe:
        if not  str(j) in sonuc.content:
            print "Sitede degisim var"
        else:
            print "Site ayni"
        print "=================="