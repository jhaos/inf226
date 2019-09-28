# Inf226

## Assignment 2
Code analysis with sonarqube and zap over the proyect Yacy .

### Description of the software analysed.

YaCy is a free search engine that anyone can use to build a search portal for their intranet or to help search the public internet. When contributing to the world-wide peer network, the scale of YaCy is limited only by the number of users in the world and can index billions of web pages. It is fully decentralized, all users of the search engine network are equal, the network does not store user search requests and it is not possible for anyone to censor the content of the shared index. We want to achieve freedom of information through a free, distributed web search which is powered by the world's users. 

For more information [yacy website](https://yacy.net/en)

### Analysis of the security design of the software – including a threat model describing the assumed threats against the software.


### Details of how the project was analysed.

On first place to analise the proyect we have made a static analisys using the well known tool sonarqube. With this tool we can analise a lot of aspects of the code.

#### Issues
Here we can see the pieces of code that does't pass the rules clasified in types and severity of the issues.

##### Type

###### Bugs 
Represents something wrong in the code that if it is not broken it will and need to be fixed.

###### Vulnerability
A security-related issue which represents a backdoor for attackers.

###### Code Smell
This means that the maintainability of the some parts of the code is compromised. This means that the coders which want to change some in the code it will be harder than it's supposed or even can add erros with those changes.

###### Security Hotspot
A piece of code that uses a security-sensitive API like weak algorithms or database connections. It  must be manually reviewed to determine if the APIs are being used in ways that introduce Vulnerabilities.

##### Severity

Blocker, critical, major, minor, info
