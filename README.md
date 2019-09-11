# inf226
## Assignment 1

### 0x01
```C
#include <assert.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc , char **argv){

char buffer[32];
int32_t check = 0xdeadbeef ;

printf("Try to get past me!\n");
fflush(stdout);

assert(fgets(buffer, 1024, stdin)!= NULL);

if(check == 0xc0cac01a){
  printf("Congratulations, you win!\n");
  fflush(stdout);
  system("cat flag.txt");
}
else {
  printf("You lose! Bye.\n");
}

return 0 ;
}
```
#### Description of the vulnerability

C language has some functions in it's libraries that can produce several buffer overflow vulnerabilities. In this case we have a buffer of 32 bytes and a 8 bytes variable. The problem resides when the program calls to fgets function with first argument the 32 bytes buffer but the second argument indicates that the buffer at the first argument has 1024 bytes of lenght and because of this I can make the buffer overflow attack overwriting the value of the variable which name is check.

#### Python script using pwntools

Here is the exploit used to get the flag with comments about why I chose the offset, then I create the cyclic and then I add the value that I want to overwrite the var check in little endian and send it to the server. I will receive the data in out_1.txt that is upload linked below as well.

[Exploit with pwntools](https://github.com/jhaos/inf226/blob/master/pwn/entregar/pwn1.py)

[Flag received from the server](https://github.com/jhaos/inf226/blob/master/pwn/entregar/out_1.txt)

### 0x02

```C
#include <assert.h>
#include <stdio.h>
#include <stdlib.h>

void do_system(){
  system("cat flag.txt");
}

int main(int argc , char **argv){

char buffer[32];

printf("Try to get past me!\n");
fflush(stdout);

assert(fgets(buffer, 1024, stdin)!= NULL);

return 0 ;
}
```

#### Description of the vulnerability

C language has some functions in it's libraries that can produce several buffer overflow vulnerabilities. In this case I have a buffer of 32 bytes. The problem resides when the program calls to fgets function with first argument the 32 bytes buffer but the second argument indicates that the buffer at the first argument has 1024 bytes of lenght and because of this I can make the buffer overflow attack. I can see that the function that calls to system is not called in the main function so the job will be overwrite the RIP to call system function.

#### Python script using pwntools

Here is the exploit used to get the flag. After send a cyclic pattern I saw that the RSP has the substring 'kaaa' at the beginning and with the funcion of pwntools cyclic_find I can know the offset and I can send the correct lenght of pattern and after I will add the address of the do_system() function to overwrite RIP and finally send to the server the payload. I will receive the data in out_2.txt that is upload linked below as well.

[Exploit with pwntools](https://github.com/jhaos/inf226/blob/master/pwn/entregar/pwn2_script.py)

[Flag received from the server](https://github.com/jhaos/inf226/blob/master/pwn/entregar/out_2.txt)

### 0x03

```Python
from flask import Flask, json, render_template, request, redirect, url_for
import mysql.connector
import os
import socket

flag = <SNIPPED>
app = Flask(__name__)
def opendb():
  config = <SNIPPED>
  
  connection = mysql.connector.connect(**config)
  cursor = connection.cursor()
  
  return (connection, cursor)
  
def closedb(connection, cursor):
  cursor.close()
  connection.close()
 
@app.route("/")
def main():
  return redirect(url_for('showSignIn'))
  
@app.route('/showSignIn')
def showSignIn():
  return render_template('signin.html')

@app.route('signIn', methods=['POST'])
def signIn():
  _name = request.form.get('inputName')
  _password = request.form.get('inputPassword')
  
  if not _name or not _password:
    error = {'message':'<span>Some fields are missing</span>'}
    return json.dumps(error)

  if _name and _password:
    (connection, cursor) = opendb()
  
    req = "SELECT * FROM tlb_user WHERE login='{}' AND password='{}'"
    cursor.execute(req.format(_name, _password))
  
    data = [(login, password) for (login, password) in cursor]
    closedb(connection , cursor) 

    if len(data) != 0 and data[0][0] == ’admin’:
      return json.dumps({’gg’:’GG! Flag: {}!’.format(flag)})
    else:
      error = {’error’:’No user found with these credentials.’}
      return json.dumps(error)

if __name__ == "__main__":
  app.run(host = ’0.0.0.0’, port =8001)

```

#### Description of the vulnerability

In the code above I can  see the sql query can check that it could exist a vulnerability because if I try to post the name and the password using unpaired quotes it responses to the log console that is not the response that it supposed to be so I can suspect that I could do sqli. Addicionally using OWASP-ZAP confirm it so I can try to make an sql attack.

#### Description of the script
I will use requests library to make the request in the webpage using admin as a keyword because it is a common word to the user administrator and I'll send the request adding a quote and '#' at the end which makes that the request will ignore the rest of the query thats why don't need a real password, also I can use a 1 OR True request for example "1' or 1=1 #" and I will get the access.

[Exploit with python and request library](https://github.com/jhaos/inf226/tree/master/sqli/sqli_1.py)

[Flag received from the server](https://github.com/jhaos/inf226/blob/master/sqli/out_1.txt)
