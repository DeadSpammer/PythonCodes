import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime

class CheckWrite :
    def __init__(self):
        now = datetime.now()
        altindosya = open("Altin.txt","w", encoding="utf8")
        Link = "https://www.mynet.com/"
        Site = requests.get(Link)
        İçerik = BeautifulSoup(Site.content, "html.parser")
        Fiyat = str(İçerik.select("body > div.my-wrap > div.container.fluid-container > div:nth-child(8) > div.col.col-3-2.item > div.finance-bar.finance-bar-1.card.m-t-20 > section > article.liveData.liveDataGold > a > div.liveDataAbsorber > p.liveName.dynamic-price-GAUTRY"))
        altindosya.seek(0)
        altindosya.write(Fiyat)
        altindosya.close
        altindosya = open("Altin.txt","r+", encoding="utf8")
        
        altindosya.seek(42)
        af = altindosya.read(8)
        print("Altinin Güncel Fiyati : ",af, "YTL")
        altindosya.close



        Kayit = open("AltinKayit.txt","a",encoding="utf8")

        Kayit_Yazisi = ("Tarih :  " + str(now) + "       Altinin Değeri : " + str(af) + "\n")
        #Kayit_Yazisi = f"Tarih : {now}       Altinin Değeri : {af}\n"
        Kayit.write(Kayit_Yazisi)
        Kayit.close()


        time.sleep(1000)
        CheckWrite()
        
CheckWrite()


#https://steamcommunity.com/profiles/76561198998485310/games/?tab=all
##game_394360 > div.gameListRowItem > div.gameListRowItemTop > div.gameListRowItemTopPrimary > h5


#https://www.mynet.com/
#body > div.my-wrap > div.container.fluid-container > div:nth-child(4) > div.col.col-3-2.item > div.finance-bar.finance-bar-1.card.m-t-20 > section > article.liveData.liveDataGold > a > div.liveDataAbsorber > p.liveName.dynamic-price-GAUTRY")
