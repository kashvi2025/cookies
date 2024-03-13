def rotating_digits(n):
    end= n%10
    remaining= n//10
    rotated= end*((10**len(str(remaining))))+(remaining)
    return rotated

result = rotating_digits(54321)
print (result)
#result = 15432