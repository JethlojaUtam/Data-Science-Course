a=20
b=30

if a is b:
    print("Answer is same")
else:
    print("Answer is not same")

if id(a) == id(b):
    print("Id is same")
else:
    print("id is not same")

b=20

if a is b:
    print("Answer is same")
else:
    print("Answer is not same")

if a is not b:
    print("Answer is same")
else:
    print("Answer is not same")