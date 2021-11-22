l1=[]
l2=[]
n=int(input("Enter number of elements for first tupple\n"))
print("Enter element\n")
for i in range(0,n):
    ele=input()
    l1.append(ele)
t1=tuple(l1)
m=int(input("Enter number of elements for second tupple\n"))
print("Enter element\n")
for i in range(0,m):
    val=input()
    l2.append(val)
t2=tuple(l2)
print(t1)
print(t2)
print("1.Create a tupple\n2.Length\n3.Repititiion\n4.Slicing\n5.Range slicing\n6.Maximum\n7.Minimum\n8.Iterate\n9.Concat\n10.Delete\n11.Find particular value\n")
while True:
    ch=int(input("Enter Choice\n"))
    if ch==1:
        t3=()
        print("Created a tuple\n")
    elif ch==2:
        print("Length of t1 and t2 is \n",len(t1),len(t2))
    elif ch==3:
        n=int(input("Enter number of repititions\n"))
        print("Tuple t1 becomes\n",t1*n)
        print("Tuple t2 becomes\n",t2*n)
    elif ch==4:
        n=int(input("Enter number for slicing\n"))
        print("Tuple t1 becomes\n",t1[n])
        print("Tuple t2 becomes\n",t2[n])
    elif ch==5:
        n=int(input("Enter initial range\n"))
        m=int(input("Enter final range\n"))
        print("Tuple t1 becomes\n",t1[n:m])
        print("Tuple t2 becomes\n",t2[n:m])
    elif ch==6:
        print("Maximum values are\n",max(t1),max(t2))
    elif ch==7:
        print("Minimum values are\n",min(t1),min(t2))
    elif ch==8:
        print("Iteration through t1\n")
        for i in t1:
            print(i)
        print("Iteration through t2\n")
        for i in t2:
            print(i)
    elif ch==9:
        print("Concetinating t1 and t2\n",t1+t2)
    elif ch==10:
        del(t3)
        print("t3 is deleted\n")
    elif ch==11:
        c=input("Enter value to be searched\n")
        if c in t1:
            print(c,"is in t1")
        elif c in t2:
            print(c,"is in t2")
        else:
            print(c,"is not present")
    else:
        print("Invalid choice\n")
            
        
        
        
        
        
        

    
    
