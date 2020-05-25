#!/usr/bin/env python
# coding: utf-8

file=open("model.py","r")
list=file.readlines()
list
var1=list[19]
a=len(var1)
var1
var2=int(var1[2:a-1]) +1
var2
var1
list[19]=var1[0:2]+str(var2)+var1[a-1:]
list[19]
list
file2=open("/root/Desktop/py_files/model.py","w")
file2.writelines(list)
file.close()
file2.close()
