s = str(input("Enter a string"))
s = s + ' '
d = ''
a = ''
i = 0
while s[i] != ' ':
    a = s[i]
    if a=='a' or a=='e'or a=='i' or a=='o' or a=='u' or a=='A' or a=='E'or a=='I' or a=='O' or a=='U':
       d = d + a
    else:
       d = d + a +'o'+ a
    i = i+1   
print(d)
