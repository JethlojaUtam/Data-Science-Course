#break
n=int(input("Enter the number:"))
for i in range(1,n+1):
    if i==4:
        break
    else:
        print(i,end=" ")
print("")

for letter in "Python Programming":
    if letter=="o":
        break
    else:
        print(letter,end=" ")
print("")

#continue
n=int(input("Enter the number:"))
for i in range(1,n+1):
    if i%2==0:
        continue
    else:
        print(i,end=" ")
print("")

#continue
n=int(input("Enter the number:"))
for i in range(1,n+1):
    if i==5:
        continue
    else:
        print(i,end=" ")
print("")

for letter in "Python Programming":
    if letter=="o" or letter=="m":
        continue
    else:
        print(letter,end=" ")
print("")
