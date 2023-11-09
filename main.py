import requests
from bs4 import BeautifulSoup
from math import *
import mysql.connector
import urllib.request
import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="hepsiemlak"
)
mycursor = mydb.cursor()
print("Hepsi Emlak Adresi:")
url = input()
print(url)
response = requests.get(url)
html_icerigi = response.content
soup = BeautifulSoup(html_icerigi,"html.parser")
baseurl="https://www.hepsiemlak.com"

firma=soup.find("span",{"class":"firm-name"})
firmaad=(firma.text).strip("\n").strip()
print(firmaad)

ilansayisicek=soup.find("div",{"class":"listing-title"})
isayi=(ilansayisicek.text).strip("\n").strip()
liste=isayi.split()
ilansayisi=int(liste[-3])
print(ilansayisi)
pc = ilansayisi / 36
i = 0
for ipc in range(1,ceil(pc+1)):
    if ipc > 0:
        page = "?page="+str(ipc)

        purl=url+page
        response = requests.get(purl)
        html_icerigi = response.content
        soup1 = BeautifulSoup(html_icerigi, "html.parser")
        for ilan in soup1.find_all("a", {"class": "card-link-clicker"}):
            i = i + 1
            print(i)
            href=ilan.get('href')
            bhref=baseurl+href
            print(bhref)
            response = requests.get(bhref)
            html_detay = response.content
            soup2 = BeautifulSoup(html_detay, "html.parser")
            baslik=soup2.find("h1", {"class": "fontRB"})
            ibaslik=(baslik.text).strip("\n").strip()
            print(ibaslik)
            fiyat=soup2.find("p", {"class": "fontRB fz24 price"})
            ifiyat=(fiyat.text).strip("\n").strip()
            print(ifiyat)
            detay=soup2.find("ul",{"class":"short-info-list"})
            for lis in detay.find_all("li"):
                li=(lis.text).strip("\n").strip().split()
                print(li)
            #
            #
            #
            #Detayların çekileceği yer.
            #
            #
            #


            sql = "INSERT INTO hepsiemlak (emlakisim,ilanad,ilanfiyat) VALUES (%s, %s, %s);"
            val = (firmaad, ibaslik, ifiyat)
            mycursor.execute(sql, val)
            mydb.commit()
            print(str(i) + ".Kayıt işlemi başarıyla gerçekleşti.")
            mycursor.execute("SELECT ilan_id FROM hepsiemlak ORDER BY ilan_id DESC")
            myresult = mycursor.fetchall()
            x = myresult[0][0]
            print("İlan id=" + str(x))
            if not os.path.exists("fotograflar/"+str(x)):
                os.makedirs("fotograflar/"+str(x))

            k = 0
            for resim in soup2.find_all("div", {"class": "swiper-slide"}):
                for image in resim.find_all("img"):
                    imglink=image['src']
                    k = k + 1
                    """
                    driver_path = "chromedriver.exe" #Klasör içinde bulunan dosyanın yolunu yazın...
                    browser = webdriver.Chrome(driver_path)

                    browser.get("https://www.watermarkremover.io/upload")
                    time.sleep(1)
                    urltik=browser.find_element_by_xpath('//*[@id="PasteURL__HomePage"]')
                    urltik.click()
                    urlgir=browser.find_element_by_xpath('//*[@id="modal-root"]/div[2]/div/div[1]/div[1]/input')
                    urlgir.send_keys(imglink)
                    subtik=browser.find_element_by_xpath('//*[@id="modal-root"]/div[2]/div/div[1]/div[1]/button')
                    subtik.click()
                    time.sleep(20)
                    indir=browser.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div/button')
                    indir.click()
                    

                    """
                    isim = str(x)+"_"+ str(k) + ".jpg"
                    yol="fotograflar/"+str(x)+"/"
                    print(yol)
                    urllib.request.urlretrieve(imglink,yol + isim)
                    print(str(k) + ".Fotoğraf eklendi.")
                
                    time.sleep(1)

                    sql = "INSERT INTO fotograf (ilan_id, foto_ad) VALUES (%s, %s)"
                    val = (x, isim)
                    mycursor.execute(sql, val)
                    mydb.commit()
