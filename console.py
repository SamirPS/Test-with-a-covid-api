import requests

Country=input("Give a country name ")

r=requests.get("https://corona.lmao.ninja/v2/countries?yesterday=false&sort=")
ville=[i["country"] for i in r.json()]
while Country not in ville:
    print("Here the Country you need to choose : ",ville)
    Country=input("Give a country name ")

for i in r.json():
    if i["country"]==Country:
        print('Here the number of case in'+str(i["country"])+str(i["cases"])+" case "+str(i["deaths"])+"death et "+str(i["recovered"])+"recovered")
        print("Today we have :"+str(i["todayCases"])+" case "+str(i["todayDeaths"])+" deaths et "+str(i["todayRecovered"])+" recovered  ")
        break
        

