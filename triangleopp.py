r=int(input("Enter number of rows :"))
for i in range(0,r):
    num=1
    for j in range(r,0,-1):
        if j>i+1:
            print(" ",end="")
        else:
            print(num,end="")
            num+=1
    print()

num=1
for i in range(0,r):
    for j in range(r,0,-1):
        if j>i+1:
            print(" ",end="")
        else:
            print(num,end="")
            num+=1
    print()

ascii = 65
for i in range(0,r):
    for j in range(r,0,-1):
        if j>i+1:
            print(" ",end="")
        else:
            a=chr(ascii)
            print(a,end="")
    ascii+=1
    print()