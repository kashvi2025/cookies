def minforloop(list):
#second attempt at min with for loop
    min= list[0]
    for num in list:
        if num<min:
            min=num
    return min
test_list_1 = [1, 2, 3, 4, 5]
result= min(test_list_1)
print(result)
