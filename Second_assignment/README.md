# Mandatory Assignment 2: YaCy

#### Julio Jose Reyes Hurtado

#### Pedro Domínguez López


## 1.YaCy description

YaCy (​ **Y** ​et ​ **a** ​nother ​ **Cy** ​berspace) is a peer to peer search engine, written in Java, which is

limited by the number of users. This mean that every user is important and it is fully

decentralized.

### Components

YacY is formed by:

```
● Crawler: browses the WWW for web indexing
● Indexer: creates a reverse word index, RWI, that made possible to search by text and
found the website
● Database: stores the RWI in a NoSQL database
● Search Interface: web interface provided by a local HTTP servlet
```
Others components:

```
● Parser: a variety of external parser libraries allows you to read and process doc, xls,
ppt, rtf, rss, html, xml, vcf, zip, gzip, tar, 7z, csv, torrent, odt, pdf, ps, swf and other
formats.
● Multi-Protocol Harvesting Clients: YaCy reads documents using the following
protocols: http, https, ftp, smb and from the file system of the local host.
```

### Network

The connection in YaCy works by connecting to a network of people also running YaCy. To

be able to perform a search using the YaCy network, every user has to set up their own

node. Each peer crosses the internet, analyzes and indexes the results, and saves indexed

results into a common database called “index”, which is shared with other YaCy-peers using

P2P network principles.

To store the search index, a special data structure is used. This data structure is optimized

for fast index delete and index merge to support the DHT functionality. The database also

stores all other work data like document metadata and the document cache. No other SQL

database is used.

## 2.Analysis of the security design of the software –

## including a threat model describing the assumed

## threats against the software. How it could be

## attacked.

We are in front of a P2P web application. Having this clues it’s possible to guess the types of

vulnerabilities based on the technologies than has been used. We will start with possible

vulnerabilities in P2P:


```
❖ Distributed Denial-of-Service: Taking profit of the nature of P2P networks sending a
high quantity of request to peers and the broadcast storm will make parts of the
network won’t work. Also is possible to use the entire P2P network to attack targets
such as web sites.
❖ Privacy and Identity: P2P networks also have problems with privacy and identity. For
example Skype uses P2P networks and though the data stream is encrypted, a peer
which carries the stream now has direct access to the data packets, which would not
be the case in traditional routing. Also the P2P philosophy is to share private files
which could make several ways to attack like remote file injection or introducing
works in those share files.
❖ Man in the Middle Attack: It happens when a attacker are between two nodes and all
communications between those nodes act passively when he is just sniffing the data
or actively if he wants to, for example, insert fake messages.
❖ Worms: A worm is a self replicate program like a virus. The vulnerability comes from
the software so in a P2P network they are sharing the same software with the same
vulnerability so is really easy to spread through the network.
```
On the other hand as a web application can also have it issues:

```
● Cross-Site-Scripting(XSS): One of the most common attacks on websites. This attack
consists of injecting malicious code into benign web pages. The attacker injects code
from the client side, so that due to bad configuration of the website, this code is
shown to other users. These types of attacks usually occur when the browser uses a
user input field to generate an output field without previously validating it. Possible
consequences of this kind attack is cookie stealing, force to download a file or
redirect an user.
● When a part of a website or application allows a user to input information we can
directly into a SQL query, this makes the website vulnerable to SQL injection. SQL
injection is when malicious code is inserted as SQL query and it begins to execute
the malicious code. Usually the purpose of this code is to access data to steal it or
delete it. If an attacker manages to access data and impersonate a database
administrator, they can then access the entire system using those copied credentials.
● XML External Entity(XXE): An XML external entity attack happens when an input
XML contains a reference an external entity by a weakly configured XML parser.​ ​This
attack can give raise to compromise confidential data or denial of service.
```

## 3.details of how the project was analysed. Using

## screenshots.

### ZAP

The first to do is start running YaCy and ZAP in your local machine, YaCy is running in

localhost:8090. In our case we have done a Manual Explore so this is how to start analyzing

YaCy. After that a Internet window appear and you can control ZAP with a HUD.

First thing to do when the window is loaded is to put YaCy index in the scope, this is

because the HUD will only allow you to use tools on sites that are in scope. After that we can

use the Spider.

ZAP has two spiders to explore web sites. The normal spider crawls all of the web pages

and follows all of the links that it can find. It is fast but it will not be able to follow links

defined using JavaScript. The ajax spider It is much slower than the 'traditional' spider but it

will be able to handle sites that make heavy use of JavaScript much more effectively.


The spider explore is done in order to make an active scan. This tool find vulnerabilities in

the URLs that ZAP knows about for the site, this is the spider scan.

In the image above we can see that the Spider have found 122039 URLs and we can see

the ones in the passive scanning queue too. This is a lot of time consuming. We have kept

this scanning for hours and think for nothing because we thought this can be scanning all the

network.

The next part is scanning for vulnerabilities.


In this picture you can see the progress for each vulnerability.

When the process is done you can see all the alerts ordered in low, medium and high

priority, and informational alerts, being the high priority alerts the riskiest and the ones with

vulnerabilities that could compromise the integrity of the system.

Finally we can save the results in a HTML report that looks like this:


### Sonarqube

Sonarqube is a static code analyzer which can find bugs and code smells. It can give us

important information about possibles vector of attacks.

To make the analysis we’ve used a docker with a demo of the software to analyze in

localhost. After run the sonarqube docker we have the application in localhost:9000/about.


We can login into the platform using the user and password provide by sonarqube team. We

have to add a new project and give it a name. Also we need to put a token to identify the

project and choose the programming language, in this case the application is write in Java

using maven.

We will use the command provide to make the scan and then we will have the static analysis

of the program. To do this we have to be in the folder of the project.


Once the process is finished we have the report.

We can see the bugs and vulnerabilities and code smells and it’s classified in block, critical,

major, minor and info levels, also it provide us some information about the nature of the

problem and some tips to know how to solve them.


## 4.results of the analysis

### With SonarQube

In this section we are going to see the security failures in the static analysis. Here are

reflected the most critical aspects divided into bugs, vulnerabilities and code smell.

#### BUGS

Bugs represents something wrong in the code that if it is not broken it will and need to be

fixed. That’s why we have locate and fix the errors.

Sonarqube reports to us that the code is using a lot of closeables objects and the coders

didn’t manage well how to close them allowing to have a risk if an exception cause that the

code won’t be executed the object won’t be closed which could put extra cost over the

application. In the next image the types of errors in several uses of functions:


Also we can find another possible bug which could cause loss of functionality like a loop

without a ending condition.

In the following critical bug they made a classic programming error that is possible to divide

by zero.

#### Vulnerability

In this section we are going to see the possible attack vectors that the code of this

application can present. As we can see in the following image we can see that there are

several similar faults in different points of the code.

An entity is a storage unit of some type. A XML external entity (XXE) vulnerability consists of

an injection that takes advantage of the bad configuration of the XML interpreter that

includes external entities, this attack is carried out against an application that interprets XML

language in its parameters. An attacker could be able to:

```
● Distributed Denial of service (DDoS).
● Access to local and remote files and services.
```

Another issue that sonarqube shows us is the insertion of credentials like users or

passwords and those hard-coded strings are easy to extract once the application is compiled

those can end up in the hands of the attackers.

The previous vulnerabilities are the higher on the sonarqube scanner but the next one are

almost as critical as the previous.

This cookie attribute makes possible to prevent client-side scripts from reading cookies with

the attribute, and its use can go a long way to defending against Cross-Site Scripting(XSS)

attacks. Said that this attribute must be set by default in all cookies in the server-side.

#### Code Smells

This is the name when the code is written without following the standards of the coding. It’s

is not a bug of programming but it represents deficiencies in the code design, the scalability

could be affected and improve the possibilities to cause errors in the future. One of the most

repeated code smells in the application is:

This function creates a new instance of the class of current object and initializes all its fields

with exactly the contents of the corresponding fields of this object but it doesn’t call to the

constructor then it doesn’t preserve the invariants established by the constructor.

Also they used similar names in several functions which could provoke misunderstanding

each other:


It could be a problem a new programmer make a mistake using one function or another, so

this errors should be fixed.

### With ZAP

#### High alerts

##### XSS

```
URL http://localhost:8090/Autocrawl_p.html
```
```
Method POST
```
```
Parameter autocrawlQuery
```
```
Attack "><script>alert(1);</script>
```
```
Evidence "><script>alert(1);</script>
```
```
URL http://localhost:8090/ConfigHTCache_p.html
```
```
Method POST
```
```
Parameter HTCachePath
```
```
Attack "><script>alert(1);</script>
```
```
Evidence "><script>alert(1);</script>
```
```
URL http://localhost:8090/CrawlCheck_p.html
```

```
Method POST
```
```
Parameter crawlingURLs
```
```
Attack <img src=x onerror=alert(1);>
```
```
Evidence <img src=x onerror=alert(1);>
```
and more

Cross-site Scripting (XSS) is an attack technique that involves echoing attacker-supplied

code into a user's browser instance. The code will run within the security context (or zone) of

the hosting web site. With this level of privilege, the code has the ability to read, modify and

transmit any sensitive data accessible by the browser. Applications utilizing browser object

instances which load content from the file system may execute code under the local machine

zone allowing for system compromise.

##### Directory Traversal

```
URL http://localhost:8090/Blacklist_p.html
```
```
Method POST
```
```
Parameter selectedListName
```
```
Attack ../../../../../../../../../../../../../../../../etc/passwd
```
```
Evidence root:x:0:
```
Directory traversal or Path Traversal is an HTTP attack which allows attackers to access

restricted directories and execute commands outside of the web server’s root directory. With

a system vulnerable to directory traversal, an attacker can make use of this vulnerability to

step out of the root directory and access other parts of the file system. This might give the

attacker the ability to view restricted files, which could provide the attacker with more

information required to further compromise the system.

##### Remote File Injection (RFI)

```
URL http://localhost:8090/api/getpageinfo_p.xml?actions=title%2Crobots&url=http
%3A%2F%2Fwww.google.com%2F
```
```
Method GET
```
```
Parameter url
```
```
Attack http://www.google.com/
```

```
Evidence <title>Google</title>
```
RFI is used to exploit dynamic file include mechanisms in web application. The web take

user input and pass them into file include commands.

An attacker can use RFI for:

* Running malicious code on the server: any code in the included malicious files will be run

by the server. If the file include is not executed using some wrapper, code in include files is

executed in the context of the server user. This could lead to a complete system

compromise.

* Running malicious code on clients: the attacker's malicious code can manipulate the

content of the response sent to the client. The attacker can embed malicious code in the

response that will be run by the client (for example, Javascript to steal the client session

cookies).

##### SQL Injection

```
URL http://localhost:8090/PerformanceGraph.png?nomem=+AND+1%3D1+--+&ti
me=
```
```
Method GET
```
```
Parameter nomem
```
```
Attack AND 1=1 --
```
```
URL http://localhost:8090/ConfigPortal.html
```
```
Method POST
```
```
Parameter search.verify.delete
```
```
Attack true' AND '1'='1' --
```
there is a lot of results on ConfigPortal.html but it doesn’t seem to work

#### Medium alerts

##### Buffer overflow

```
URL http://localhost:8090/Banner.png?textcolor=000000&bgcolor=e7effc&borderc
olor=5090d
```

```
Method GET
```
```
Parameter bgcolor
```
```
Attack GET
http://localhost:8090/Banner.png?textcolor=000000&bgcolor=ldaFpUUqvnxy
HhhcQCilYcFkHaijBqnedaqfVNYYSKUGtsOAmsHrFndQTADHJHtNcrVZlRG
nAbClZVDslGdEFpvyvLuYCLSRbQpDUAWRreqVaexFmXrlmOmQbTJMeB
wJSALGZwHaGAFjUGhRexOuhEcZkiiccixeYNQLsbYcPWKVwBFZREbcoq
RLKAFfmgNLmYYjZCwblUjAkqKBIAgvekvdFyGTOVpYtXCfwEOTAYcmdHB
EAImtsobDQYLYxBImYeAXrYllhtgPjRwFCOSssOVdijXOFhgqhWMVJkKAB
kOjSWuBfnHGpWsFBIuuyABhjqNApMRIBcAPoxyUqXhaBkcxEvgQwcqxYIN
hocIYuHuycDaolcGTsfmymOnTTRlSwipuhcJFKLfrhSPrndUHPeneeWIpRm
mghAHsixtMIPWwdwAdZiGFRNsRtXocjWJWWMHLqyQfpVjktkmUhKDrKQ
DrQpaYtbVkDBwXduCfnhhSFEShHwfWIvCgBbqSkRaeOwJWpkufSlnlwAec
HWCKImDkFJjTyHorjfegWckeQnTnautXekfikiNXkpNdOubKgNrHjKFfWDgid
pHEabwMjFqCvnciONduynNoEJgknaloAmglIAfbGsEUbrEIJReryjUVMJkhaP
jjsJrbtoSKsiafSiuqepJFLjXEUHyqaXafkrHmavyNdtphVaJEHQSacCfqowHgd
qbMLsaRpKncmglDuxUTnIeNfiCrpDYNHmAOXTFalIZDvOnKXIeHpbjbpgLk
WdffXYATcwUJjSccvLtnbxiBYNfijufDUuUQdlrprvJBXpRgpKhxHvSWwjndqE
SAvwqnhZnHbgwkiwApsHeAxoatwOQafUMFgGRjcoWwFsTgDmCsllefVHlL
DbLsojXvAYWEPQBYSegkQOMiflJlfxqadKSUBZoQwyxJJrjyniMLAioKMwq
WkfCsvoUWWQWxRxdAXesOXwtDFetjYDDfmRtjBmSHiGvQfuoGnZcdAAO
ZxWKwbdXFlWEBQgCdIawTPHVMsFdvipxLDkxRolHdXUmRJaTVwnKSPx
nHPLWLrfdPYfhPBJFwgjNGoAtgwrCyLVXWtDuNawfKYpNDBqHeFYQHEiQ
wLBQbAWSLrPKNMfSdLZgSkTMMoXAjZTNDYhvHryuEjHQvEIcpUdjPgvvf
MhSRvWWvoghWSYgGbIjqtkqrMxoXboktnVtiCvlKSVQRcUmEwyPGVitKok
RAVihmbUjgFqpDJrYOBuuiSFkohLhHnTdCIDLwCAFEYbboUHOrixLEKqPc
EiguLFfPPeCYbCuehpwmSDaKfvQLkqhdwowgZdHeNhVZNxpgMlhfoNALTv
rFkcmtLKrKveTehySgvXUhmgcgKxlbNXuLVFJiDBmesSxESlNgyDEepTmjw
SfeHZLnsieeZcxnMEraWcxdWqdPFEkNENaZtZnejDISbwfuSrehXnlIjEAoAj
PpPQegqnOFReMVfeqXgOxnvjmildIjyYyelrTUKsoGSoxZOWZjZNfEwQoBB
YIQdNQkCIbYiNQfivGJZxjdBuureQWkFGsxtvCZqNWfNPrOjwmZlPOISxxvlv
BQWHGcdexcFsOHtpsoMXMaDTFSWfNcwLZSoDSOXFZNNqntARrSSBVv
orHyQCOrWSLwYmIswykRvpsHsFHBqOdlEnQPkWeuyyukBIZDIGtFCJvXm
PcAeDmFNxeElSTwwnBJYJQXoPguJjbSAATwLyByGvYJFrYURwjYwvykaN
OutygkOftmpNJddWNALcqfUvfWIBZQaBNoLBElpuevJCAAgPeIqoxdfFvqD
XssuLHrTClnqRLUGOJxqfuqEFutvbpRjYqDkDVjAFhjahILhhRSLQVHTPpVF
cgPwlwVmMjlGLHTbywbTTfrgReXalRcjLIXTjdUCfsDVFosvVgnYfFIkGaMbS
aGhOWWXyJChoJGVoNsqUikEcKQVHRlracLWZkeTeuovupQhOmgbcwXrF
JuPbMKbCnGUcTNpbRpyFJblFPEtcWauyDOSvZLkKcussjFUtjPlNnjxLbvDx
YidEWwogwLYvbAhJiJOKFRWWQTQqrfqffCsFbMtXGBGPdR&bordercolor=
5090d0 HTTP/1.1 User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64;
rv:69.0) Gecko/20100101 Firefox/69.0 Accept: image/webp,*/*
Accept-Language: en-US,en;q=0.5 Connection: keep-alive Referer:
https://localhost:8090/Status.html Content-Length: 0 Host: localhost:
```
Buffer overflow errors are characterized by the overwriting of memory spaces of the

background web process, which should have never been modified intentionally or

unintentionally. Overwriting values of the IP (Instruction Pointer), BP (Base Pointer) and


other registers causes exceptions, segmentation faults, and other process errors to occur.

Usually these errors end execution of the application in an unexpected way

##### Directory Browsing

```
URL http://localhost:8090/js/​ , ​http://localhost:8090/env/​ ,
http://localhost:8090/proxymsg/​ , ​http://localhost:8090/processing/​ ,
http://localhost:8090/jquery/
```
```
Method GET
```
```
Attack Parent Directory
```
It is possible to view the directory listing. Directory listing may reveal hidden scripts, include

files , backup source files etc which can be accessed to read sensitive information.

## 5. Discussion of the significance of the findings

At this point we are going to explain deeper the dangerous vulnerabilities found in the code

using both static and dynamic analysis.

#### XSS

The vulnerabilities found can be used to compromise the integrity of the system. With a XSS

vulnerability an attacker could inject JavaScript which could be passed among the peers and

infect all the p2p network with malicious content.

#### Directory traversal

With the Directory traversal vulnerability, an attacker could access to private data like

passwords of the peers. This can be combined with the XSS attack. Someone can inject

JavaScript in the peers that can access to the data via Directory traversal and then be

returned or displayed in the network.

#### RFI and SQL Injection

The RFI is similar to XSS. An attacker could inject code on the server or on the client,

stealing the data using Directory Traversal or even with SQL Injection (ZAP have detected

SQL Injection but we think that in this software it can’t be done, probably is an error).


#### XML external entity (XXE)

XML external entity (XXE) is one of the most critical vulnerabilities nowadays. As we said

before It is an attack against an application that interprets XML entries. The attack is

possible when the way of interpreting the XML allows to include external entities due to its

bad configuration. It can lead to reading of local files, discovery and mapping of internal

network, denials of service, etc.

As we mentioned before this vulnerability could drive to Distributed Denial of service (DDoS)

and the attacker also could have access to local and remote files and services. In recent

months there have been reports to Yahoo, eBay or Google.

It’s common find this vulnerability in Content-Types: text/xml, application/xml although it can

be found in Word docs joined and compressed, lastly JSON parsed as XML. It is about

malformating requests with XML so that we add functionalities to the XML interpreter such

as reading a local file and sending its content to an external server.

#### Hardcoding credentials

Have hard-coded credentials could the cause of amount of holes that allows to attackers

bypass the authentication. This kind of vulnerability may be hard to the system administrator

to detect or fix which could force to turn down the entire system. We can distinguish two

different types:

```
● Inbound: the software has an authentication mechanism that verify input credentials
with hard-coded credentials. This means that the software has stored the password
inside the code which cannot be changed by the administrator without modifying the
code or with a patch. If this credentials is discovered then it can be used in all the
products.
● Outbound: the software has to connect to another system which contains the
hard-coded credentials to connect with this that system. This happens when a
front-end communicate with a back-end service. The programmer could hard-code
those back-end credentials into front-end software and any user could discover it and
extract the password. Client side with hard-coded passwords are a real threat also
because extract it from binaries could be very simple.
```
#### HttpOnly cookies attribute

A cookie is a file created by a website that contains small amounts of data and is sent

between a sender and a receiver. In the case of the Internet, the sender will be the server

where the web page is hosted and the receiver is the browser used to visit any web page.

Its main purpose is to identify the user by storing their activity history on a specific website

the cookie will be sent along with your requests to the web application, so that the web

application knows you're logged in. If someone steal that cookie, they could add the cookie

to their own browser and steal the identity.


“If the HttpOnly flag (optional) is included in the HTTP response header, the cookie cannot

be accessed through client side script (again if the browser supports this flag). As a result,

even if a cross-site scripting ​ **(XSS)** ​ flaw exists, and a user accidentally accesses a link that

exploits this flaw, the browser (primarily Internet Explorer) will not reveal the cookie to a third

party. ” ​OWASP​.

So the server could help to mitigate XSS and this issue by setting the HttpOnly flag on the

cookie it creates to indicate that the cookie musn’t be in the client side.

## 6. Suggestions for possible improvements to the

## security of the application

All of this vulnerabilities can be solved with some work.

### XSS solution

#### Filtering input

This can be applied for any vulnerability, is essential to filter all the input from the user.

Validating input is the process of ensuring an application is rendering the correct data and

preventing malicious data from doing harm to the site, database, and users. But trying to

prevent malicious input is difficult because:

- Blacklisting is bad security practice.
- The disallowed characters (say, &, <, >, " , ' and /) are quite common.
- Client side checking is easy to circumvent.

#### Escaping

Escaping data means taking the data an application has received and ensuring it’s secure

before rendering it for the end user. By escaping user input, key characters in the data

received by a web page will be prevented from being interpreted in any malicious way. That

will disallow the characters – especially < and > characters – from being rendered.

#### Encoding

For every web page that is generated, it should be used and specified a character encoding

such as ISO-8859-1 or UTF-8. When an encoding is not specified, the web browser may

choose a different encoding by guessing which encoding is actually being used by the web

page. This can cause the web browser to treat certain sequences as special, opening up the

client to subtle XSS attacks.


#### Security checks

For any security checks that are performed on the client side, is important to ensure that

these checks are duplicated on the server side, in order to avoid CWE-602. Attackers can

bypass the client-side checks by modifying values after the checks have been performed, or

by changing the client to remove the client-side checks entirely. Then, these modified values

would be submitted to the server.

### RFI solution

#### Disable remote inclusion feature

Is important to have the RFI feature disable especially if it is not necessary. It is done by

default in PHP

#### Filter and sanitize variables and inputs

Like XSS is important to assume all inputs and GET variables are malicious. A good strategy

is to use a whitelist of acceptable inputs for example, that strictly conform to specifications.

Reject any input that does not strictly conform to specifications, or transform it into

something that does.

### Directory Traversal solution

#### Filter and sanitize variables and inputs

As before

#### Low privileges

Run server processes with only the permissions that they require to function. This can help

limit the impact of vulnerabilities as a second line of defense.

#### Use Indirection

Each time a file is uploaded it should be labelled using indirection. It can have a family name

for the site but when the file is accessed, perform a lookup in the data-store to discover the

actual file path.

### SQL Injection solution

Like before the client side input have to be assumed like malicious. So is important to check

all data on the server side. For that reason is important to not concatenate strings from the

direct input without filtering and sanitizing them first.


### XML external entity (XXE)

To prevent this kind of vulnerability begins at development level. A good knowledge of XML

can provide a good configuration which will mitigate a lot of threats with XEE. OWASP

recommend use easier formats to manage the data like JSON which uses a lighter and

newer syntax and tends to be less exploitable than xml. Also is recommended that for huge

applications that manual code review is the best choice to find and fix XXE vulnerabilities but

it’s also recommend the use of automatized applications.

### Hard-coding credentials

A first approach could be to encrypt the credentials that hard code but this can bring the

problem that if the attacker finds the form of encryption it could take out the password with a

dictionary attack. Another better way is to use an strongly encrypted file where you can store

the password, also you can apply strong one-way hashes to the credentials and store the

hashes in a configuration file.

### HttpOnly

A server will send the cookie to the browsers in the client side and if this attribute is not set it

could make that an attacker the possibility of use XSS attacks or make a cookie theft. To

avoid that the first step is to set the flag to the cookie created in the server and then it cannot

be accessible to the client.

If the browser detects a cookie with the flag activated and someone attempts to read the

cookie the browser will return an empty string.
