class Person:
    def Hello(self,name=None,age=None): 
        self.name=name
        self.age=age
        if (name!=None and age!=None):
            print("Hello ",self.name,"your age is ",self.age)
        elif (name!=None and age==None):
            print("Name is",self.name)
        else:
            print("Helo")
p=Person()
p.Hello()
p.Hello("Teju",22)
p.Hello("Teju")
