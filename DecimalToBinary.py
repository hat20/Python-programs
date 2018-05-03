n = int(input("Enter a Decimal No."))
a=[]
i=0
while n!=0:
   d = [int(n%2)]
   n=int(n/10)
   a = a+d
print("Its Binary equivalent",a)
