class Oper():
    def __init__(self):
        self.alist=[]
    def getelements(self):
        n=int(input("Enter number of elements\n"))
        print("Enter elements\n")
        for i in range(0,n):
            self.alist.append(int(input()))
    def __add__(self,other):
        newlist=[]
        for i in range(0,len(self.alist)):
            newlist.append(self.alist[i]+other.alist[i])
        return newlist
    def __sub__(self,other):
        newlist=[]
        for i in range(0,len(self.alist)):
            newlist.append(self.alist[i]-other.alist[i])
        return newlist
    def __mul__(self,other):
        newlist=[]
        for i in range(0,len(self.alist)):
            newlist.append(self.alist[i]*other.alist[i])
        return newlist
    def __floordiv__(self,other):
        newlist=[]
        for i in range(0,len(self.alist)):
            newlist.append(self.alist[i]//other.alist[i])
        return newlist
    
