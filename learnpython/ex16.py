def Add(a, b):
    print("Addition of %d + %d " % (a, b))
    return a + b


def SUB(a, b):
    print("division of %d - %d " % (a, b))
    return a - b


def MUL(a, b):
    print("Multiplication of %d * %d" % (a, b))
    return a * b


def DIV(a, b):
    print("Divition of %d / %d " % (a, b))
    return a / b


age = Add(30, 5)
height = SUB(190, 6)
weight = MUL(10, 7)
iq = DIV(100, 2 )

print("YOUR AGE IS %d \n And Your height is %d /n As Well as your weight is %d /n so finally your iq is %d "
      % (age, height,weight,iq))


print("Lets play new puzzle :")



what =Add(age, SUB(height, MUL(weight, DIV(iq, 2))))

print("That's Becomes :", what, ", What YOU have got in your Hand? ")