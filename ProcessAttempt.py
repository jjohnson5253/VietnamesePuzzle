#!/usr/bin/env python3

from multiprocessing import Process, Array, Value
import time


class P(Process):
	def __init__(self,firstNum,secondNum,perms):
		Process.__init__(self)
		self.firstNum = firstNum
		self.secondNum = secondNum
		self.perms = perms
		self.answers = Array('B',200)

	def run(self):
		i=0
		for num in range(self.firstNum,self.secondNum):
			strNum = str(num)
			checks = {}
			breakOut = False
			for digit in strNum:
				if(digit=='0'):
					breakOut = True
					break
				elif digit not in checks:
					checks[digit] = 1
				else:
					breakOut = True
					break
			if(breakOut == False):
				self.perms[i]=int(strNum)
				i=i+1;

"""
		for num in self.permutations:
			self.calculate(num)

		#print(self.permutations)


	def calculate(self,num):

		answer = int(num[0])+((13*int(num[1]))/int(num[2]))+int(num[3])+(12*int(num[4]))-int(num[5])-11+((int(num[6])*int(num[7]))/int(num[8])-10)

		if(answer==66):
			self.answers.append(answer)
"""

if __name__ == '__main__':

	permutations = Array('B',362880)

	p1 = P(123456789,123456800,permutations)
	p2 = P(123456789,123456800,permutations)
	#p3 = P(555555555,771604938)
	#p4 = P(771604938,987654322)

	p1.start()
	p2.start()
	#p3.start()
	#p4.start()

	p1.join()
	p2.join()

	print(permutations.raw)












