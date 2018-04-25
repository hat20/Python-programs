print("Prints the largest of three numbers")
a = int(input("Enter 1st number "))
b = int(input("Enter 2nd number "))
c = int(input("Enter 3rd number "))
if a>b:
  if a>c:
     print("The largest no. is",a)
if b>a:
  if b>c:
     print("The largest no. is",b)
if c>a:
  if c>b:
     print("The largest no. is",c)