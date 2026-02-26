n1=int(input("Enter the first number:"))
n2=int(input("Enter the second number:"))

print("1. Addition\n2. Substraction\n3. Multiplication\n4. Division")

choice=int(input("Enter the choice number:"))

if choice==1:
    ans=n1+n2
    print("Addition is:",ans)

elif choice==2:
    ans=n1-n2
    print("Substraction is:",ans)

elif choice==3:
    ans=n1*n2
    print("Multiplication is:",ans)

elif choice==4:
    if n2!=0:
        print("Division is:",ans)
    else:
        print("Error: Division by zero not allowed")

else:
    print("Invalid choice!!")