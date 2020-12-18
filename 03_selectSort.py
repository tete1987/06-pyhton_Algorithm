#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/12/18 10:07 
# @Author : TETE
# @File : 03_selectSort.py
# def select_sort_simple(li):
#     li_new = []
#     for i in range(len(li)):
#         min_val = min(li)
#         li_new.append(min_val)
#         li.remove(min_val)
#     return li_new
#
# li = [8,5,3,9,2,4]
# print(li)
# print(select_sort_simple(li))


def select_sort(li):
    for i in range(len(li)-1):    #i是第几趟
        min_loc = i
        for j in range(i+1,len(li)):
            if li[j]<li[min_loc]:
                min_loc =j
        li[i],li[min_loc] =li[min_loc],li[i]

li = [8,5,3,9,2,4]
print(li)
select_sort(li)
print(li)