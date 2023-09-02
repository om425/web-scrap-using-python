import requests

API_KEY= 'icGekmVUdwr6WDMAw7YRVRdJbAq7ZPPdRl8waFpn'



def NasaNews(Date):
    Url="https://api.nasa.gov/planetary/apod?api_key=icGekmVUdwr6WDMAw7YRVRdJbAq7ZPPdRl8waFpn"


    Params={'date':str(Date)}
    r=requests.get(Url,params=Params)
    Data=r.json()
    
    Info=Data['explanation']
    print(Info)

    Image_Url= Data['url']
    print(Image_Url)
   
   
   
   
    img_data = requests.get(Image_Url).content
    with open( str(Date)+'.jpg', 'wb') as handler:
     handler.write(img_data)
  
NasaNews('2023-05-07')    