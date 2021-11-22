from magic2 import *
ov1=Oper()
ov2=Oper()
ov1.get_elements()
ov2.get_elements()
print(ov1.alist)
print(ov2.alist)
while True:
    print("1 Operator Overload +\n2.Operator Overload -\n3.Operator Overload *\n4.Operator Overload //")
    ch=int(input("Enter your choice\n"))
    if ch==1:
        print("Operator Overload +\n")
        print(ov1+ov2)
    elif ch==2:
        print("Operator Overload -\n")
        print(ov1-ov2)
    elif ch==3:
        print("Operator Overload *\n")
        print(ov1*ov2)
    elif ch==4:
        print("Operator Overload //\n")
        print(ov1//ov2)
    else:
        print("Inavalid choice\n")
