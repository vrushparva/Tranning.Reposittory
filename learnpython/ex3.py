name = 'Vrushparva  Vaishnav '
age = 29
height = 180 #cm
weight = 74 #kg
eyes = 'Black'
teeth = 'White'
hair = 'Black ' #90%

print("Let's talk about %s." % name)
print("He's %r inches tall." % height)
print("He's %r pounds heavy." % weight)
print("Actually that's not too heavy.")
print("He's got %r eyes and %r hair." % (eyes, hair))
print("His teeth are usually %s depending on the coffee." % teeth)
# this line is tricky, try to get it exactly right
print ("If I add %r, %r, and %r I get %r." % ( age, height, weight, age + height + weight))
