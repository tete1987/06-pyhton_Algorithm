#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/12/18 9:40 
# @Author : TETE
# @File : 02_bubbleSort.py
def bubble_sort(li):
    for i in range(len(li)-1):
        exchange = False
        for j in range(len(li)-i-1):
            if li[j]>li[j+1]:
                li[j],li[j+1]=li[j+1],li[j]
                exchange =True
        print(li)
        if not exchange:
            return

li = [1,2,4,7,8,9,3]
print(li)
bubble_sort(li)
print(li)