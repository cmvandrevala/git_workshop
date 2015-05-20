# -*- coding: utf-8 -*-
"""
Created on Fri Oct 31 18:49:21 2014

@author: cdhagmann
"""

'''
Problem 1

If we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3, 5, 6 and 9. The sum of these multiples is 23. If we do it for numbers
under 1000 the sum is 233168. Write a program than compute the sum of the 
numbers under n.
'''
def Problem1(n, multiples=(3,5)):
    nums = []
    for i in xrange(n):
        flag = False
        for m in multiples:
            if i % m == 0:
                flag = True
                break                    
        if flag:
            nums.append( i )
    return sum(nums)

            
'''
Problem 2

By considering the terms in the Fibonacci sequence whose values do not exceed 
n, find the sum of the even-valued terms.
'''
def Problem2(n, fib=[0,1]):
    if n < fib[-1]:
        return sum(f for f in fib if f < n and f % 2 == 0)
    else:
        while n > fib[-1]:
            fib.append( fib[-1] + fib[-2] )
            
        return Problem2(n)


'''        
Problem 3

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17. 
Find the sum of all the primes below two million.
'''
def Problem3(n, primes=[2, 3]):
    if n < primes[-1]:
        return sum(p for p in primes if p < n)
    else:
        for i in xrange(primes[-1] + 1, n):
            flag = True
            P = (p for p in primes if p <= i / 2.)
            for p in P:
                if i % p == 0:
                    flag = False
                    break
            if flag:
                primes.append( i )            
        
        return sum(p for p in primes if p < n)