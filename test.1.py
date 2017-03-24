#!/usr/bin/python
# -*- coding: utf-8 -*-
# de a a ab
num=10
max=len(range(ord('A'),ord('Z')))+1
init=ord('A')
maxChar=625
Elements=[]
if num>maxChar:
    print ("error {0} exceeds {1}").format(num, maxChar)
    exit(0)
if num/max > 0:
    for i in range (1, int(num/max)*max+1):
        if i/max == 0 or i == max:
            value=chr(i-1+init)
        else:
            if i==max*(i/max):
                value = chr(((i-1) / max) - 1 + init) + chr(max - 1 + init)
            else:
                value=chr((i/max)-1+init)+chr(i-(max*(i/max))-1+init)

        #print ("{0:3} {1:3}").format(str(i),value)
        Elements.append(value)
    for i in range (num-(num % max)+1, num+1 ):
        value = chr((i / max) - 1 + init) + chr(i - (max * (i / max)) - 1 + init)
        #print ("{0:3} {1:3}").format(str(i), value)
        Elements.append(value)
else:
    for i in range(1,num):
        value = value=chr(i-1+init)
        #print ("{0:3} {1:3}").format(str(i),value)
        Elements.append(value)
print Elements