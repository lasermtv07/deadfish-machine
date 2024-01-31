#!/bin/python3
import sys
a=sys.argv
a=a[1:]
source="".join(a)
print(source)
source+=" " #bruh
p=0
o="v2.0 raw\n"
#it aint pretty but it werks
ti=0
td=0
ts=0
to=0
while p<len(source):
    while source[p]=="i":
        ti+=1
        p+=1
    if ti>0:
        if ti>1:o+=f" {ti}*9"
        elif ti==1:o+=" 9"
        ti=0
    while source[p]=="d":
        td+=1
        p+=1
    if td>0:
        if td>1:o+=f" {td}*b"
        elif td==1:o+=" b"
        td=0
    while source[p]=="s":
        ts+=1
        p+=1
    if ts>0:
        if ts>1:o+=f" {ts}*c"
        elif ts==1:o+=" c"
        ts=0
    while source[p]=="o":
        to+=1
        p+=1
    if to>0:
        if to>1:o+=f" {to}*30"
        elif to==1:o+=" 30"
        to=0
    p+=1
print(o)
