
def power_of_a_number(x,y):
    result=1
    for i in range (y):
        result *= x  
    return result

def min(list):
#1st attempt at min with for loop
    list = []
    for i in range (len(list)-1):
        min = i
        if list[i]<list[i+1] :
            j=i+1
            min = i
        elif list[i]> list[i+1]:
            j=i+1
            min = j
    return min

def check_leap_year(x):
    if x % 4 == 0 and x%100 != 0:
        return "this is a leap year"
    else:
        return "this is not a leap year"
    
def BMI(weight, height):
    BMI= weight/ (height*height)
    return BMI

def rotating_digits(n):
    end= n%10
    remaining= n//10
    rotated= end*((10**len(str(n)))+ remaining)
    return rotated

def minforloop(list):
#second attempt at min with for loop
    min= list[0]
    for num in list:
        if num<min:
            min=num
    return min
def maxforloop(list):
    max=list[0]
    for num in list:
        if num>max:
            max=num
    return max
def minwhileloop(list):
    i=1
    min= list[0]
    while i<len(list):
        if min>list[i]:
            min=list[i]
        i+=1
    return min   
def maxwhileloop(list):
    i=1
    max= list[0]
    while i<len(list):
        if max<list[i]:
            max=list[i]
        i+=1
    return max 
def vowels(string):
    j=0
    vowels="aeiouAEIOU"
    for char in string:
        if char in vowels:
            j+=1
    return j

def digital_root(number):
    digital_root=0
    while number>0:
        digital_root+= number%10
        number//=10
    return digital_root