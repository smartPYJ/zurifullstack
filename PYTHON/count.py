#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 18 13:39:47 2022

@author: smart
"""

#prompt user to give a word 
given_word = input("enter a word")

#remove wihite spaces from front and back 
clean_word = given_word.strip()

#count given word 
count = len (clean_word)

print ('the length of your inputed word is' , count)