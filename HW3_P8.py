def digital_root(number):
    digital_root=0
    while number>0:
        digital_root+= number%10
        number//=10
    return digital_root
    
result=digital_root(5837)
print(result)
#result=23