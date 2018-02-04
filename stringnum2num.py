# 中科曙光面试题目20180128
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 17:36:20 2018

@author: samsung
"""
def zhengshuzhengfu(string):
    num=0
    if string[0]=='-':
        string1=string[1:]
        for i in range(len(string1)):
            num += int(string1[i])*(10**(len(string1)-1-i))
        num=(-1)*num
    else:
        for i in range(len(string)):
            num += int(string[i])*(10**(len(string)-1-i))
    return num
	
def xiaoshu(string):
    num=0.0
    for i in range(len(string)):
        num+=float(string[i])*(0.1**(1+i))
    return num
	
def shifoushixiaoshu(string):
    num=0        
    if '.' in string:
        i=string.index('.')        
        str1=string[:i]
        str2=string[i+1:]
        #print(str2)
        num1=zhengshuzhengfu(str1)
        if '-' in str1:
            num2=(-1)*xiaoshu(str2)
        else:
            num2=xiaoshu(str2)
        num=num1+num2
    else:
        num=zhengshuzhengfu(string)    
    return num

string=input("plesase input a number:")
#str1=string.split('')
string1=','.join(string)
string11=string1.split(',')
print(shifoushixiaoshu(string11))

