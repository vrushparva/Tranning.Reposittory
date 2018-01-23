# fibonacci in while loop
n= int(input("Enter Positive Number :"))
a = 1
b = 0
counter = 1
while counter <= n:
    counter += 1

    print(a, end=" ")
    a = a+b
    b = a-b
print(end="\n")
print(counter)

