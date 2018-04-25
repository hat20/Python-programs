s = str(input("enter a string"))
s_len = len(s)
rev = ''
while s_len != -1:
    s_len = s_len - 1
    rev = rev + s[s_len]
print(rev)


