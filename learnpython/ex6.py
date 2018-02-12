formatter = "%r %r %r %r"

print(formatter % (1, 2, 3, 4))
print(formatter % ("One", "Two", "Three", "Four"))
print(formatter % (True, False, True, False,))
print( formatter % ("I had this thing.",
                    "That you could type up right."
                    ,"But i didn't sing.",
                    "So i said goodnight."))