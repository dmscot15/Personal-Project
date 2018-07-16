#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 11:22:53 2018

@author: Desi
"""
import math

def pearsonD (user1ratings, user2ratings):
    """This function returns the Pearson Correlation of user1ratings and user2ratings""" 
    
    sumpq = 0
    sump = 0
    sumq = 0
    sump2 = 0
    sumq2 = 0
    
    for item in (user1ratings.keys() & user2ratings.keys()):
       print('key', item, '; user1ratings:', user1ratings[item], ';user2ratings value:', user2ratings[item])
       
       p = user1ratings[item]
       q = user2ratings[item]
       sumpq += p * q
       sump += p
       sumq += q
       sump2 += pow(p, 2)
       sumq2 += pow(q, 2)
    
    n = len(user1ratings.keys() & user2ratings.keys())
    print ('n is: ', n)

    nr = (sumpq - (sump * sumq) / n)
    dr = (math.sqrt(sump2 - pow(sump, 2) / n) * math.sqrt(sumq2 - pow(sumq, 2) / n))    
    r = nr / dr
    return r

UserPRatings = {'Apple':1, 'Samsung':5, 'Nokia':7, 'Motorola':8, 'LG':5, 'Sony':1, 'Blackberry':7}
UserQRatings = {'Apple':7, 'Samsung':1, 'Nokia':4,'LG':4, 'Sony':6, 'Blackberry':3}


r = round(pearsonD(UserPRatings, UserQRatings),4)
print ('Pearson Correlation: ', r)


