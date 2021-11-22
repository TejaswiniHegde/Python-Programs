print("1.Uppercase\n2.Lower Case\n3. Length\n4.Maximum\n5.Minimum\n6.Slicing\n7.Reverse\n8.Cocetination\n9 Comparision\n11Sort\n12Strip\n")
while True:
    ch=int(input("Enter your choice\n"))
    if ch==1:
        n1=input("Enter a string\n")
        if not(n1):
            print("Empty")
        elif n1.isalnum():
            print(n1.upper())
        else:
            print("not possible")
    elif ch==2:
        n1=input("Enter a string\n")
        if not(n1):
            print("Empty")
        else:
            print(n1.lower())
    elif ch==3:
        n1=input("Enter a string\n")
        if not(n1):
            print("Empty")
        else:
            print(len(n1))
    elif ch==4:
        n1=input("Enter a string\n")
        if not(n1):
            print("Empty")
        else:
            print(max(n1))
    elif ch==5:
        n1=input("Enter a string\n")
        if not(n1):
            print("Empty")
        else:
            print(min(n1))
    elif ch==6:
        n1=input("Enter a string\n")
        if not(n1):
            print("Empty")
        else:
            print(n1[2:4])
    elif ch==7:
        n1=input("Enter a string\n")
        if not(n1):
            print("Empty")
        else:
            print(n1[::-1])
    elif ch==8:
        n1=input("Enter a string\n")
        if not(n1):
            print("Empty")
        else:
            n2=input("Enter a string\n")
            print(n1*n2)
    elif ch==9:
        n1=input("Enter a string\n")
        if not(n1):
            print("Empty")
        else:
            n2=input("Enter a string\n")
            print(n1==n2)
    elif ch==10:
        n1=input("Enter a string\n")
        n2=input("Enter a string\n")
        print(n2 in n1)
    elif ch==12:
        n1=input("Enter a string\n")
        if not(n1):
            print("Empty")
        else:
            print(n1.strip())     
    else:
        break
            
