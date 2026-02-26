rollno=int(input("Enter the rollno:"))
name=input("Enter the name:")
math=int(input("Enter the math mark:"))
python=int(input("Enter the python mark:"))
java=int(input("Enter the java mark:"))
ml=int(input("Enter the ml mark:"))
dotnet=int(input("Enter the dotnet mark:"))
total=(math+python+java+ml+dotnet)
percentage=float(total*100/500)

print("Roll No.:",rollno)
print("Name:",name)
print("Math Mark:",math)
print("Python Mark:",python)
print("Java Mark:",java)
print("ML Mark:",ml)
print("DotNET Mark:",dotnet)
print("Total Mark:",total)
print("Percentage:",percentage)

if percentage>=0 and percentage<40:
    print("Grade D")
elif percentage>=40 and percentage<55:
    print("Grade C")
elif percentage>=55 and percentage<70:
    print("Grade B")
elif percentage>=70 and percentage<85:
    print("Grade A")
elif percentage>=85 and percentage<=100:
    print("Grade A+")
else:
    print("Something went wrong")
