
n=9
num = 0
for i in range(n):
    for j in range(i,n-1):
        print("",end=" ")
    for s in range(i):
        print(num, end=" ")
        num += 1
    print(" ")


