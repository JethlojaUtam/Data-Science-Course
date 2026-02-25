#print the sum of odd number
s=0
n=int(input("Enter the no.:"))
for i in range(1,n+1):
    if i%2!=0:
        print(i,end=" ")
        s+=i
print("\nSum of odd no.:",s)

#print the sum of even number
s=0
n=int(input("Enter the no.:"))
for i in range(1,n+1):
    if i%2==0:
        print(i,end=" ")
        s+=i
print("\nSum of even no.:",s)

#print the sum of number
s=0
n=int(input("Enter the no.:"))
for i in range(1,n+1):
    print(i,end=" ")
    s+=i
print("\nSum of no.:",s)