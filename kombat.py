import random
import time
def yazitura(karakter1,karakter2):
    orneklem = [random.randint(1, 2) for i in range(100)]
    yazi = orneklem.count(1)
    tura = orneklem.count(2)
    if yazi>tura:
        cikti1=karakter1+" önce başlar."
        print(cikti1)
        return cikti1
    if tura>yazi:
        cikti2=karakter2+" önce başlar."
        print(cikti2)
        return cikti2       
def cangosterbaslangic(sonuc):
    if(sonuc==karakter1+" önce başlar."):
        print(karakter1 +"\n"+f"HP:[{player1.can}]"+'|'*(player1.can//2))
        print(karakter2+ "\n"+f"HP:[{player2.can}]"+'|'*(player2.can//2))
    if(sonuc==karakter2+" önce başlar."):
        print(karakter2 +"\n"+f"HP:[{player2.can}]"+'|'*(player2.can//2))
        print(karakter1+ "\n"+f"HP:[{player1.can}]"+'|'*(player1.can//2))

class player1():
    def __init__(self,can):
        self.can = can
    def cangoster():
         print(karakter1 +"\n"+f"HP:[{player1.can}]"+'|'*(player1.can//2))
    def hasaralma1(m):
        alinanhasar1=[random.randint(1,2) for i in range (0,100-m)]
        vurdu = alinanhasar1.count(1)
        vurmadi = alinanhasar1.count(2)
        if vurdu>vurmadi:
            print(karakter2+f"{m} hasar verdi")
            player1.can-=m
            player1.cangoster()
            player2.cangoster()
        if vurmadi>vurdu:
            print("Saldırı Başarısız")
            player1.can=player1.can
            player1.cangoster()
            player2.cangoster()
class player2():
    def __init__(self,can):
        self.can = can
    def cangoster():
        print(karakter2 +"\n"+f"HP:[{player2.can}]"+'|'*(player2.can//2))
    
    def hasaralma2(m):
        alinanhasar2=[random.randint(1,2) for i in range (0,100-m)]
        vurdu = alinanhasar2.count(1)
        vurmadi = alinanhasar2.count(2)
        if vurdu>vurmadi:
            print(karakter1+f"{m} hasar verdi")
            player2.can-=m
            player1.cangoster()
            player2.cangoster()
        if vurmadi>vurdu:
            print("Saldırı başarısız.")
            player2.can=player2.can
            player1.cangoster()
            player2.cangoster()
def olumkontrol():
    if(player1.can==0 or player2.can==0):
        return True
def karakter1turu():
    m=int(input(karakter1+"Saldırı!!!\n Saldırı büyüklüğünüzü 1 ile 50 arasında seçin"))
    if(m>50):
        print("Saldırı büyüklüğü 1 ile 50 arasında olmalıdır")
        m=int(input(karakter1+"Saldırı!!!\n Saldırı büyüklüğünüzü 1 ile 50 arasında seçin"))
    player2.hasaralma2(m)
def karakter2turu():
    m=int(input(karakter2+" Saldırı!!!\n Saldırı büyüklüğünüzü 1 ile 50 arasında seçin"))
    if(m>50):
        print("Saldırı büyüklüğü 1 ile 50 arasında olmalıdır")
        m=int(input(karakter2+" Saldırı!!!\n Saldırı büyüklüğünüzü 1 ile 50 arasında seçin"))
    player1.hasaralma1(m)
def savas():
        while True:
            if(sonuc==karakter1+" önce başlar."):
                karakter1turu()
                if (olumkontrol()==True):
                    player1.cangoster()
                    player2.cangoster()
                    print("\n"+karakter2+"kazandı!")
                    break
                else:
                    karakter2turu()
            if(sonuc==karakter2+" önce başlar."):
                karakter2turu()

                if (olumkontrol()==True):
                    player1.cangoster()
                    player2.cangoster()
                    print("\n"+karakter2+"kazandı!")
                    break
                else:
                    karakter1turu()
player1.can=int(100)
player2.can=int(100)          
karakter1=input("----İlk Kahraman----\nLütfen kahramanınızın adını yazın")
karakter2=input("----İkinci Kahraman----\nLütfen kahramanınızın adını yazın")
if karakter1==karakter2:
    print(karakter2+"alındı,lütfen başka bir isim seçin")
    karakter2 = input("----İkinci Kahraman----\nLütfen kahramanınızın adını yazın")
sonuc=yazitura(karakter1,karakter2)
cangosterbaslangic(sonuc)
time.sleep(.5)
while True:
    savas()
    time.sleep(1)
    soru=input("Bir tur daha oynamak ister misiniz (Evet veya Hayır)? :")
    if soru=="Hayır":
        print("Oynadığınız için teşekkürler! Tekrar görüşürüz!")
        break
    elif soru=="Evet":
        sonuc=yazitura(karakter1,karakter2)
        cangosterbaslangic(sonuc)
        time.sleep(.5)
        savas()