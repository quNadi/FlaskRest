import requests

location="http://127.0.0.1:5000/"

data=[{"name": "szoff","content":23344444444444444444},
      {"name": "loft","content":444},
      {"name": "porfff","content":999999444444}]

for i in range(len(data)):
    response=requests.put(location+"api/"+str(i),data[i])


