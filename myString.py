a=input("Enter first string\n")
b=input("Enter second string\n")
print("1.Concatinate\n2.Length\n3.Uppercase\n4.Lowercase\n5.Swapcase\n6.Capitalize\n7.Slicing\n8.Range Slicing\n9.Reverse\n10.Iterarting\n")
while True:
    ch=int(input("Enter your choice\n"))
    if ch==1:
        print("Concatenation of two string is \n",a+b)
    elif ch==2:
        print("Lenth of first string is\n",len(a))
        print("Lenth of second string is\n",len(b))
    elif ch==3:
        print("Uppercase is\n",a.upper(),b.upper())
    elif ch==4:
        print("Lowercase is\n",a.lower(),b.lower())
    elif ch==5:
        print("Swapcase is\n",a.swapcase(),b.swapcase())
    elif ch==6:
        print("Capitalized strings is\n",a.capitalize(),b.capitalize())
    elif ch==7:
        n=int(input("Enter a number to slice\n"))
        print("Slicing with ",n,"is ",a[n],b[n])
    elif ch==8:
        n=int(input("Enter initial range to slice\n"))
        m=int(input("Enter final range to slice\n"))
        print("Slicing with ",n , m,"is ",a[n:m],b[n:m])
    elif ch==9:
        print("On Reversing\n",a[::-1],b[::-1])
    elif ch==10:
        print("Iterating through first string\n")
        for i in a:
            print(i)
        print("Iterating through second string\n")
        for j in b:
            print(j)
    else:
        print("Invalid choice\n")
            
        
        
           
