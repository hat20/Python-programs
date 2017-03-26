# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel). 
#

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    flag = 0
    months = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    no_of_days = months[month1] - day1
    month1 = month1 + 1
    curr_year = year1
    while True:
        no_of_days = no_of_days + months[month1]
        if(month2 == month1 and curr_year == year2):
            break
        elif(month1 == 12):
            month1  = 1
            curr_year = curr_year + 1
        month1 = month1 + 1
    no_of_days = no_of_days + day2

    if(day1 <= 28 and month1 <= 2):
        no_of_days = no_of_days + isleapyear(year1)
    year1 = year1 + 1
    if(month2 > 2):
        no_of_days = no_of_days + isleapyear(year2)
    year2 = year2 - 1

    while(year2 > year1):
        no_of_days = no_of_days + isleapyear(year1)
        year1 = year1 + 1



    

        
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

# Test routine

def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()
