print("1.add")
print("2.subtract")
a=input("Enter your choice:")
n1=int(input("Enter number 1:"))
n2=int(input("Enter number 2:"))
if (a=="1"):
    s=n1+n2
    print("Result after adding =",s)
else:
    m=n1-n2
    print("Result after subtracting =",m)
