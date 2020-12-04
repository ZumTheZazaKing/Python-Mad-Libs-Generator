#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 16:33:53 2020

@author: muhammadzahidi
"""
import time

print('-'*70)
print('                           Mad Libs Generator')

def main():
    
    print('-'*70)
    
    time.sleep(2)
    
    userName = str(input('Enter a name:'))
    
    print('-'*70)
    
    userAdverb = str(input('Enter an adverb:'))
    
    print('-'*70)
    
    userVerbing = str(input('Enter a verb that ends with -ing:'))
    
    print('-'*70)
    
    userPlace = str(input('Enter a place:'))
    
    print('-'*70)
    
    userItem = str(input('Enter an item of small size:'))
    
    print('-'*70)
    
    print('Processing story...')
    
    print('-'*70)
    
    time.sleep(5)
    
    print(userName + ' was ' + userAdverb + ' ' + userVerbing + ' around the ' +
          userPlace + ' and ' + userName + ' found a ' + userItem + 
          ' on the ground.')
    
    print('-'*70)
    
    time.sleep(3)
    
    
while True:
    
    main()
    
    time.sleep(3)
    
    if str(input("Would you like to tell another story?(Y/N)")).strip().upper() != "Y":
        
        print('\nGoodbye!\n')
        
        time.sleep(1)
        
        break