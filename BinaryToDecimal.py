import math
n=int(input("Enter a binary number"))
d=0
p=0
while n!=0:
   dig= int(n%10)
   d = d + dig*(math.pow(2,p))
   n=n/10
   p= p + 1
print("Decimal equivalent is",d) 
