from magicPractice import *
ov1=Oper()
ov2=Oper()
ov1.getelements()
ov2.getelements()
print(ov1.alist)
print(ov2.alist)
while True:
    print("1.Add\n2.Sub\n3.Mul\n4.Floor Div\n")
    if (len(ov1.alist)==len(ov2.alist)):
        ch=int(input("Enter choice\n"))
        if ch==1:
            print("Addition is\n")
            print(ov1+ov2)
        elif ch==2:
            print("Subtraction is\n")
            print(ov1-ov2)
        elif ch==3:
            print("Multiplication is\n")
            print(ov1*ov2)
        elif ch==4:
            print("Division is\n")
            print(ov1//ov2)
        else:
            print("Invalid choice\n")
            break
    else:
        print("Cannot perform overloading")
        exit()
