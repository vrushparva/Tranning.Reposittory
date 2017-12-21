min = float(input("Enter usage call minutes of whole month :"))
txt = float(input("Enter usage text message  of whole month :"))

basecharge = int(15)
callcharge = 0.44

if min <= 50  or  txt <= 50:
    if min > 50  or txt > 50:
        base_cal1 = (min - 50) * 0.25
        base_txt = (txt -50) * 0.15
        extracharge = (base_cal1 + base_txt)
        callcharge = 0.44
        salastax = (basecharge + callcharge + extracharge) * 0.05
        grandtotall = basecharge + extracharge + callcharge + salastax
    else:
        base_cal1 = 0
        base_txt = 0
        extracharge = 0
        salastax = (basecharge + callcharge) * 0.05
        grandtotall = basecharge + extracharge + callcharge + salastax

elif min > 50 and txt > 50 :
    base_cal1 = (min - 50)*0.25
    base_txt=  (txt - 50)*.15
    basecharge = 15
    extracharge = (base_cal1 + base_txt)
    callcharge = 0.44
    salastax = (basecharge + callcharge + extracharge)*0.05
    grandtotall = basecharge + extracharge +  callcharge + salastax

print ("your base charge is         :%d" % basecharge)
print ("your extra call charges is  :%0.2f" % base_cal1)
print ("your extra txt charges is   :%0.2f" % base_txt)
print ("your callcharges is         :%0.2f" % callcharge)
print ("your salestax is            :%0.2f" % salastax)
print ("your grand totall  is       :%0.2f" % grandtotall)