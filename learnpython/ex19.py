i = 0
numbers = []

while i < 6:
    print("The Top number is %d" % i)
    numbers.append(i)

    i += 1
    print("Now number is %r" % numbers)

    print("At the bottom i is %d " % i)


print("The Numbers :")
for num in numbers:
    print(num)