def isleapyear(year):
    if(year%100 == 0):
        if(year%400 ==0):
            return 1
        else:
            return 0
    elif(year%4 ==0):
        return 1
    else:
        return 0


print isleapyear(1900)
print isleapyear(2004)
print isleapyear(2000)
print isleapyear(1800)

