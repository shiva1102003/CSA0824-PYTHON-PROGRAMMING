print("enter marks for subjects")
maths=int(input("maths= "))
phy=int(input("phy= "))
chem=int(input("chem= "))
total=maths+phy+chem
average=total/3
print(f"average is {average}")
percentage=average*100
if percentage>=90:
    print("A grade")
elif percentage>=80:
    print("B grade")
elif percentage>=70:
    print("C grade")
elif percentage>=60:
    print("D grade")
elif percentage>=50:
    print("E grade")
else:
    print("F grade")
