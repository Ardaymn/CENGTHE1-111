number=input()
numberone=number[0]
numbertwo=number[1]
numberthree=number[2]
numberfour=number[3]
numberfive=number[5]
if numberfive=="X" or numberfive=="x":
    numberfive="10"
if "?" not in number or number[5]=="?":
    givennumber=(2*int(numberone))+(3*int(numbertwo))+(5*int(numberthree))+(7*int(numberfour))
    checkdigit=(givennumber%11)

if "?" in number:
    loc=number.find("?")
    if loc==5:
        if checkdigit==10:
            print(number[:4]+"-"+"X")
        else:
            print(number[:4]+"-"+str(checkdigit))
    elif loc!=5:
        if "?"==numberone:
            givennumber=int((3*int(numbertwo))+(5*int(numberthree))+(7*int(numberfour)))
            y=int(givennumber-int(numberfive))
            if y%11==0:
                print(str(0)+number[1:])
            z=1
            garip=11*(y//11+z)-y
            garipa=garip/2
            if str(garipa)[-1]!="0" and y%11!=0:
                z=2
                garip=11*(y//11+z)-y
                garipa=garip/2
            songivennumber=givennumber+garip
            checkdigit=(songivennumber%11)
            if checkdigit==int(numberfive) and y%11!=0:
                print(str(int(garipa))+number[1:])

        elif "?"==numbertwo:
            givennumber=int((2*int(numberone))+(5*int(numberthree))+(7*int(numberfour)))
            y=int(givennumber-int(numberfive))
            if y%11==0:
                print(number[0]+str(0)+number[2:])
            z=1
            garip=11*(y//11+z)-y
            garipa=garip/3
            if str(garipa)[-1]!="0" and y%11!=0:
                z=2
                garip=11*(y//11+z)-y
                garipa=garip/3
            if str(garipa)[-1]!="0" and y%11!=0:
                z=3
                garip=11*(y//11+z)-y
                garipa=garip/3
            songivennumber=givennumber+garip
            checkdigit=(songivennumber%11)
            if checkdigit==int(numberfive) and y%11!=0:
                print(number[0]+str(int(garipa))+number[2:])

        elif "?"==numberthree:
            givennumber=int((2*int(numberone))+(3*int(numbertwo))+(7*int(numberfour)))
            y=int(givennumber-int(numberfive))
            if y%11==0:
                print(number[:2]+str(0)+number[3:])
            z=1
            garip=11*(y//11+z)-y
            garipa=garip/5
            if str(garipa)[-1]!="0" and y%11!=0:
                z=2
                garip=11*(y//11+z)-y
                garipa=garip/5
            if str(garipa)[-1]!="0" and y%11!=0:
                z=3
                garip=11*(y//11+z)-y
                garipa=garip/5
            if str(garipa)[-1]!="0" and y%11!=0:
                z=4
                garip=11*(y//11+z)-y
                garipa=garip/5
            if str(garipa)[-1]!="0" and y%11!=0:
                z=5
                garip=11*(y//11+z)-y
                garipa=garip/5
            songivennumber=givennumber+garip
            checkdigit=(songivennumber%11)
            if checkdigit==int(numberfive) and y%11!=0:
                print(number[:2]+str(int(garipa))+number[3:])

        elif "?"==numberfour:
            givennumber=int((2*int(numberone))+(3*int(numbertwo))+(5*int(numberthree)))
            y=int(givennumber-int(numberfive))
            if y%11==0:
                print(number[:3]+str(0)+number[4:])
            z=1
            garip=11*(y//11+z)-y
            garipa=garip/7
            if str(garipa)[-1]!="0" and y%11!=0:
                z=2
                garip=11*(y//11+z)-y
                garipa=garip/7
            if str(garipa)[-1]!="0" and y%11!=0:
                z=3
                garip=11*(y//11+z)-y
                garipa=garip/7
            if str(garipa)[-1]!="0" and y%11!=0:
                z=4
                garip=11*(y//11+z)-y
                garipa=garip/7
            if str(garipa)[-1]!="0" and y%11!=0:
                z=5
                garip=11*(y//11+z)-y
                garipa=garip/7
            if str(garipa)[-1]!="0" and y%11!=0:
                z=6
                garip=11*(y//11+z)-y
                garipa=garip/7
            songivennumber=givennumber+garip
            checkdigit=(songivennumber%11)
            if checkdigit==int(numberfive) and y%11!=0:
                print(number[:3]+str(int(garipa))+number[4:])


elif checkdigit==int(numberfive):
    print("VALID")
elif checkdigit!=int(numberfive):
    print("INVALID")


