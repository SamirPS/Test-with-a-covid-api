import requests

Country=input("Give a country name ")

r=requests.get("https://corona.lmao.ninja/v2/countries?yesterday=false&sort=")

while Country not in [i["country"] for i in r.json()]:
    print("Here the Country you need to choose : ",ville)
    Country=input("Give a country name ")

for i in r.json():
    if i["country"]==Country:
        print(f'Here the number of case in  {i["country"]} : {i["cases"]} case  {i["deaths"]} death et  {i["recovered"]} recovered  ')
        print(f'Today we have : {i["todayCases"]} case  {i["todayDeaths"]} deaths et  {i["todayRecovered"]} recovered  ')
        break
        

