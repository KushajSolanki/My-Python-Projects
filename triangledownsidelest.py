r=int(input("Enter number of rows:"))

for i in range(r,0,-1):
    for j in range(0,i):
        print("*",end=" ")
    print()

n=1
for i in range(r,0,-1):
    for j in range(0,i):
        print(n, end=" ")
    n+=1
    print()


n=1
for i in range(r,0,-1):
    for j in range(0,i):
        print(j+1,end=" ")
    print()

for i in range(r, 0, -1):
    n = i
    for j in range(0, i):
         print(n, end=" ")
         n-=1
    print()
