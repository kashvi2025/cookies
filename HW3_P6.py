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

test_list_1 = [1, 2, 3, 4, 5]
result=maxwhileloop(test_list_1)
print(result)
#result=5

resultt=minwhileloop(test_list_1)
print(resultt)
#result=1

resulttt=maxforloop(test_list_1)
print(resulttt)
#result = 5

resultttt=minforloop(test_list_1)
print(resultttt)
#result=1