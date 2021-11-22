num=int(input("Enter a value\n"))
for i in range(1,num+1):
    for j in range(1,i+1):
        print(j,end=" ")
    for k in range(num+1-i,0,-1):
        print(k,end=" ")
    print()
