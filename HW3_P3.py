def check_leap_year(x):
    if x % 4 == 0 and x%100 != 0:
        return "this is a leap year"
    else:
        return "this is not a leap year"
    
result = check_leap_year(2400)
print(result)
#test case=2400
#ourput:"this is not a leap year"