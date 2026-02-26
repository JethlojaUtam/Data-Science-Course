a=int(input("Enter the value A:"))
b=int(input("Enter the value B:"))
c=int(input("Enter the value C:"))

if a>b:
    if a>c:
        print("A is greatest")
    else:
        print("C is greatest")
else:
    if b>c:
        print("B is greatest")
    else:
        print("C is greatest")