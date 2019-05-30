# -*- coding: utf-8 -*-
"""
Created on Sat May  25 12:59:24 2019

@author: Abhinits2046
"""

things = "tree,box,chair,lamp,\n" \
         "desk,cat,dog,grass,\n" \
         "pig,box,lamp,shelf"
print(things)
print()

old_item = input("old item:")
new_item = input("new item:")
len_old_item = len(old_item)

i = things.find(old_item)
while i >= 0:
    before = things[:i]
    after = things[i + len_old_item:]
    things = before + new_item + after
    i = things.find(old_item)

print()
print(things)

##############  HINT
# old item:tree
# new item:rrr
#
# rrr,box,chair,lamp,
# desk,cat,dog,grass,
# pig,box,lamp,shelf
