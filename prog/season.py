Enterdate = input("Enter Date DD-MM-YYYY : ")
Edate = Enterdate.split("-")

spliDD = int(Edate[0])
spliMM = int(Edate[1])
spliYY = int(Edate[2])
print(spliDD, spliMM, spliYY)

if spliMM == 4 or spliMM == 5:
    print("its spring")
elif spliMM == 7 or spliMM == 8:
    print("its summer")
elif spliMM == 10 or spliMM == 11:
    print("its fall")
elif spliMM == 1 or spliMM == 2:
    print("its winter")

if spliMM == 3:
    if spliDD >= 20:
        print("its spring")
    else:
        print("its winter")

if spliMM == 6:
    if spliDD >= 20:
        print("its summer")
    else:
        print("its fall")

if spliMM == 9:
    if spliDD >= 20:
        print("its fall")
    else:
        print("its winter")

if spliMM == 12:
    if spliDD >= 20:
        print("its winter")
    else:
        print("its spring")