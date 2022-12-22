r = int(input("Enter number of rows: "))
for i in range(0,r):
    for j in range(0,i+1):
        print("*", end=" ")
    print()

for i in range(0,r):
    for j in range(0,i+1):
        print(j+1,end =" ")
    print()

m=1
for i in range(0,r):
    for j in range(0,i+1):
        print(m, end=" ")
        m+=1
    print()

for i in range(0,r):
    x=i+1
    for j in range(0,i+1):
        print(x, end=" ")
        x-=1
    print()


for i in range(0,r):
    for j in range(0,i+1):
        print(i+1,end=" ")
    print()

ascii = 65
for i in range(0,r):
    for j in range(0,i+1):
        a=chr(ascii)
        print(a,end=" ")
        ascii+=1
    print()