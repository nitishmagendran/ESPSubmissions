import urequests as requests
import ujson as json
#from parse import urlencode

city = input("Please enter the City name: ")
appid = "dcjz05qXKgB4QFxWNXT61GCdF8GQ7O4H"

urlcity = "http://dataservice.accuweather.com/locations/v1/cities/search?"+"apikey="+appid+"&q="+city
#url = urlcity+ urlencode(params=parameters,doseq = True)
print(urlcity)
lockeyresp = requests.get(urlcity)
rawdat = lockeyresp.json()
locationkey = rawdat[0]['Key']


url1 = "http://dataservice.accuweather.com/currentconditions/v1/"+locationkey+"?apikey=dcjz05qXKgB4QFxWNXT61GCdF8GQ7O4H"
response = requests.get(url1)
strin = response.json()
for par in strin:
    
    json_data = json.dumps(par)
    data = json.loads(json_data)
#print(data["LocalObservationDateTime"])
#print(data['WeatherText'])
#print(str(data['Temperature']['Metric']['Value'])+" Degree Celsius. ")
#print(data['PrecipitationType'])

toprint = str(data["LocalObservationDateTime"]) +"\n"+str(data['WeatherText'])+"\n"+str(data['Temperature']['Metric']['Value'])+" Degree Celsius. "+str(data['PrecipitationType'])
print(toprint)
import urequests as requests 
import ujson as json

url = "https://discord.com/api/webhooks/890522840821006366/Ol38KeLTe2aXel4y2ECnDLuiDdilNYiEjrhMYHTKp8FsGyVPn6CFHD5HwM-7nCR8ww0B"
headers = {
  'Content-Type': 'application/json'
}

while True:
    payload = json.dumps({
      "content": toprint
    })

    response = requests.post(url, headers=headers, data=payload)

    print(response.json)