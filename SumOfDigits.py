n=int(input("Enter a number"))
d=0
while n!=0 :
   d= d + int(n%10)
   n= int(n/10)
print("Sum of digits is",d) 
