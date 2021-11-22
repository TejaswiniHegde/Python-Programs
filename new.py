class Person:
	def Hello(self,name=None,age=None):
		self.name=name
		self.age=age
		#self.name=input("Enter name\n")
		#self.age=int(input("Enter age\n"))
		if self.name!=None and self.age!=None:
			print("Hello %s your age is %s"%(self.name,self.age))
		elif self.name!=None and self.age==None:
			print("Hello",self.name)
		else:
			print("Hello")
p1=Person()
p1.Hello()
p1.Hello(input(Enter Name))
p1.Hello(int(input("Enter age)))
