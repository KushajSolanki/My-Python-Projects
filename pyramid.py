r = int(input("Enter number of rows:"))
for i in range(0,r):
    for j in range(0,r-i):
        print(end=" ")
    for k in range(0,i+1):
        print("*",end=" ")
    print()

n=1
for i in range(0,r):
    for j in range(0,r-i):
        print(end=" ")
    for k in range(0,i+1):
        print(n,end=" ")
        n+=1
    print()

ascii=65
for i in range(0,r):
    for j in range(0,r-i):
        print(end=" ")
    for k in range(0,i+1):
        a=chr(ascii)
        print(a,end=" ")
        ascii+=1
    print()

