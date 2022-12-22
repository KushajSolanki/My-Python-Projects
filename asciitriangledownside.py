r=int(input("Enter number of rows:"))

ascii=65
for i in range(r,0,-1):
    for j in range(0,i):
        a = chr(ascii)
        print(a,end=" ")
        ascii+=1
    print()

ascii = 65
for i in range(r,0,-1):
    for j in range(0,i):
        a = chr(ascii)
        print(a,end=" ")
    ascii+=1
    print()


for i in range(r,0,-1):
    ascii = 65
    for j in range(0,i):
        a = chr(ascii)
        print(a,end=" ")
        ascii+=1
    print()


for i in range(r,0,-1):
    ascii = 65+i-1
    for j in range(0,i):
        a = chr(ascii)
        print(a,end=" ")
        ascii-=1
    print()
