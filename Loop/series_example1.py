a=int(input("Enter the number:"))
for i in range(1,a+1):
    if i%2==0:
        print((-i)*i,end=" ")
    else:
        print(i*i,end=" ")
print("")