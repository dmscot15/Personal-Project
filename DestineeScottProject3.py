#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 15:20:25 2018

@author: Desi
"""
import math

class similarity: 
    
    def __init__ (self, ratingP, ratingQ):
        self.ratings1 = ratingP
        self.ratings2 = ratingQ
        
    def minkowski(self, r):
        if (r <= 0):
            print ("r <= 0; returning -2 distance!")
            return -2
        
        distance = 0
        
        for item in (self.ratings1.keys() & self.ratings2.keys()):
            print('key', item, '; ratings1:', self.ratings1[item], '; ratings2 value:', self.ratings2[item])
            
            p = self.ratings1[item]
            q = self.ratings2[item]
            distance += pow(abs(p - q), r)
        
        return pow(distance, 1/r)
        
    def pearson(self): 
        
        sumpq = 0
        sump = 0
        sumq = 0
        sump2 = 0
        sumq2 = 0
    
        n = len(self.ratings1.keys() & self.ratings2.keys())
    
    # single for loop with items only rated by both users
        for item in (self.ratings1.keys() & self.ratings2.keys()):
            print('key', item, '; ratings1:', self.ratings1[item], ';ratings2 value:', self.ratings2[item])
        
       # computed sums
            p = self.ratings1[item]
            q = self.ratings2[item]
            sumpq += p * q
            sump += p
            sumq += q
            sump2 += pow(p, 2)
            sumq2 += pow(q, 2)
    
        if n == 0: 
            print ("0 key match; returning -2 correlation!")
            return -2
    # computationally efficient form of peason correlation
        
        dr = (math.sqrt(sump2 - pow(sump, 2) / n) * math.sqrt(sumq2 - pow(sumq, 2) / n)) 
        nr = (sumpq - (sump * sumq) / n)
        
        if dr == 0:
            return -2
        else: 
            return nr / dr
    
    
        
UserPRatings = {'Motorola':8, 'LG':5, 'Sony':1, 'Apple':1, 'Samsung':5, 'Nokia':7}
UserQRatings = {'Apple':7, 'Samsung':1, 'Nokia':4, 'LG':4, 'Sony':6, 'Blackberry':3}

users = similarity(UserPRatings, UserQRatings)
md = round(users.minkowski(1), 4)
print ("-"*33)
print ("Manhattan Distance =", md)
print ("-"*33)


md = round(users.minkowski(2), 4)
print ("-"*33)
print ("Euclidean Distance =", md)
print ("-"*33)

md = round(users.minkowski(3),4)
print ("-"*33)
print ("Minkowski Distance =", md)
print ("-"*33)

r = round(users.pearson(),4)
print ("-"*33)
print ('Pearson Correlation: ', r)
print ("-"*33)