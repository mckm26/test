#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 20:16:02 2021

@author: mck_m
"""
dct = ({'X':'a','N':'b','Y':'c','A':'d','H':'e','P':'f','O':'g','G':'h',
        'Z':'i','Q':'j','W':'k','B':'l','T':'m','S':'n','F':'o','L':'p','R':'q',
        'C':'r','V':'s','M':'t','U':'u','E':'v','K':'w','J':'x','D':'y','I':'z'})

a = input('Input encrypted text: ')

emp_str=''
for letter in a:
    emp_str = emp_str + dct[letter]
    
print('plain text (w/o spaces): ' + emp_str)
    

