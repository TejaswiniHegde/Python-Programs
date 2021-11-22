print("1.Uppercase\n2.Lower Case\n3. Length\n4.Maximum\n5.Minimum\n6.Slicing\n7.Reverse\n8.Cocetination\n9 Comparision\n11Sort\n12Strip\n")
while True:
    print("Enter Your choice\n")
    ch=int(input("Enter your choice\n"))
    if ch==1:
        n1=input("Enter a string\n")
        if not(n1):
            print("Empty")
        elif n1.isalnum():
            print("n1.upper")
        else:
            print("not possible")
    elif ch==2:
        n1=input("Enter a string\n")
        if not(n1):
            print("Empty")
        else:
            print("n1.lowercase")
    else:
        break
            
