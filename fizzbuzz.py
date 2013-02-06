'''
Created on Feb 4, 2013
Code Golf challenge for the traditional fizzbuzz problem.
@author: anduril
'''
for x in range(1,101):print'Fizz'*(x%3==0)+'Buzz'*(x%5==0)or x
