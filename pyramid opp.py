r = int(input("Enter number of rows:"))
for i in range(r,0,-1):
    for j in range(0,r-i):
        print(end=" ")
    for k in range(0,i):
        print("*",end=" ")
    print()