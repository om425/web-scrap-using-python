import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as ps

name=[]
price=[]
description=[]


url="https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&p%5B%5D=facets.brand%255B%255D%3DRealme&otracker=nmenu_sub_Electronics_0_Realme"
 
r = requests.get(url)


soup = BeautifulSoup(r.text, 'lxml')

s = soup.find('div',class_="_1YokD2 _3Mn1Gg")

name_1=s.find_all('div',class_="_4rR01T")


for p in name_1:
    name1=p.text
    name.append(name1)
    



price_1=s.find_all('div',class_="_30jeq3 _1_WHN1")


for n in price_1:
    price1=n.text
    price.append(price1)
    



des_1=s.find_all('ul',class_="_1xgFaf")


for d in des_1:
    des1=d.text
    description.append(des1)




data=pd.DataFrame({"Product Name":name,"Description":description,"Price":price})
print(data)





