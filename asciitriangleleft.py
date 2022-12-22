r = int(input("Enter number of rows:"))

ascii = 65
for i in range(0,r):
    for j in range(0,i+1):
        a=chr(ascii)
        print(a,end=" ")
        ascii+=1
    print()

for i in range(0,r):
    ascii=65
    for j in range(0,i+1):
        a=chr(ascii)
        print(a,end=" ")
        ascii+=1
    print()

for i in range(0,r):
    ascii = 65+i
    for j in range(0,i+1):
        a=chr(ascii)
        print(a, end=" ")
        ascii-=1
    print()

ascii=65
for i in range(0,r):
    for j in range(0,i+1):
        a=chr(ascii)
        print(a,end=" ")
    ascii+= 1
    print()
