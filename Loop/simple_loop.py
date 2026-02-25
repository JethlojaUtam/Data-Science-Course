# 1 to 10
for i in range(1,11):
    print(i,end=" ")
print("\n")

# 10 to 1
for i in range(10,0,-1):
    print(i,end=" ")
print("\n")

# 1 to n
n=int(input("Enter the No.:"))
for i in range(1,n+1):
    print(i,end=" ")
print("\n")

# n to 1
n=int(input("Enter the No.:"))
for i in range(n,0,-1):
    print(i,end=" ")
print("\n")

# n to m
n=int(input("Enter the starting No.:"))
m=int(input("Enter the ending No.:"))
for i in range(n,m+1):
    print(i,end=" ")