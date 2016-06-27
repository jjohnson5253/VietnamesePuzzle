#!/usr/bin/env python3

#Jake Johnson Summer 2016

#This program uses a built-in python method to find all permutations for digits 1-9
#and a brute force method to find all the answers to the vietnamese equation

import itertools
import time

#calculate time to run
start = time.time()

#permutations = list(itertools.permutations(['1','2','3','4','5','6','7','8','9']))
permutations = list(itertools.permutations([1,2,3,4,5,6,7,8,9]))

#Function to calculate answers
def calculate(num):

	answer = int(num[0])+((13*int(num[1]))/int(num[2]))+int(num[3])+(12*int(num[4]))-int(num[5])-11+((int(num[6])*int(num[7]))/int(num[8])-10)
	
	if(answer==66):
		answers.append(num)

#Create list for answers and plug all permutations into calculate function
#to find the answers
answers=[]
for num in permutations:
	calculate(num)

#write answers to files
a = open('answers.txt','w')
p = open('permutations.txt','w')
for num in permutations:
	p.write(str(num) + "\n")
for ans in answers:
	a.write(str(ans) + "\n")

#calculate time to run
print(time.time()-start)


