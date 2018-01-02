hage =int(input("Enter human age :" ))

def calcu(base,divition,above24 ):
    dage = float(hage - divition) / above24
    dage = dage + base
    return dage

if hage <= 15:
      print ("Your dog age is %0.2f" % calcu(0,0,15))
if hage > 15 and hage <= 24:
      print("Your dog age is %0.2f" % calcu(1,15,9))
if hage > 24:
      print("Your dog age is %0.2f" % calcu(2,24,4))
