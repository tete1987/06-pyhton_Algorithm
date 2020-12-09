#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/12/9 10:10 
# @Author : TETE
# @File : 01_hanoi.py
def hanoi(n,a,b,c):
    if n>0:
        hanoi(n-1,a,c,b)
        print(f"moving from %s to %s"%(a,c))
        hanoi(n-1,b,a,c)

hanoi(3,'A','B','C')