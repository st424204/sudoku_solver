import numpy as np
import os

class Solver:
	def __init__(self):
		self.stack = []
		self.data = []
		self.position = [0,0]
	def show(self):
		os.system("cls")
		for a in self.data:
			for b in a:
				print(b,end=" ")
			print("\n")
			
	def legal(self,val):
		if val in self.data[self.position[0],:]:
			return False
		if val in self.data[:,self.position[1]]:
			return False
		x = self.position[0]-self.position[0]%3
		y = self.position[1]-self.position[1]%3
		if val in self.data[x:x+3:,y:y+3]:
			return False
		return True
		
	def move_next(self):
		self.position[1]+=1
		if self.position[1] == 9:
			self.position[0]+=1
			self.position[1]=0
		
	def get(self):
		self.__init__()
		ok = open("input.txt").readlines()
		for i in range(9):
			line = [ int(d) for d in ok[i].split("\n")[0].split()]
			self.data.append(line)
		self.data = np.array(self.data).astype(np.int8)
	def get_string(self,ok):
		self.__init__()
		ok = list(ok)
		for i in range(0,81,9):
			self.data.append([ d for d in ok[i:i+9]])
		self.data = np.array(self.data).astype(np.int8)
	def get_data(self,tmp):
		self.__init__()
		self.data = tmp.reshape([9,9]);
		self.data = np.array(self.data).astype(np.int8)
	def solve(self):
		try:
			while(1):
				if self.position[0] == 9:
					break
				if self.data[self.position[0],self.position[1]] <= 0:
					for i in range(1-self.data[self.position[0],self.position[1]],11):
						if i<=9 and self.legal(i):
							self.data[self.position[0],self.position[1]] = i
							self.stack.append([self.position[0],self.position[1]])
							self.move_next()
							break
						elif i >= 9:
							self.data[self.position[0],self.position[1]] = 0
							self.position = self.stack[-1]
							self.stack = self.stack[:-1]
							self.data[self.position[0],self.position[1]] = -self.data[self.position[0],self.position[1]]
							break
				else:
					self.move_next()
		except:
			self.get()

