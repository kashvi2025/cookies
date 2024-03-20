list_1to50 = [num for num in range (51)]
print(list_1to50)

#attempt1 at 2.2
def square(list):
    for i in (list):
        listt=i**2
    return listt

result= square(list_1to50)
print(result)
# this is incorrect because it just returns the square of the last number in the list

#attempt2 at 2.2
def square(list):
    listt=[]
    for i in (list):
        listt.append(i**2)
    return listt

result= square(list_1to50)
print(result)
#I needed to add .append so that the elements would be added to the new list

#attempt 1 at 2.3
listA= [num for num in range(1,11,1)]
listB= [num for num in range(10,21,1)]

def oddlist(list1,list2):
    oddlist=[]
    for i in (list1):
        if i%2 != 0:
            oddlist.append(i)
            
    for i in (list2):
        if i%2 != 0:
            oddlist.append(i)
    return oddlist
    
result= oddlist(listA,listB)
print(result)
# i didn't mess up in this one i just made a syntax error that vscode caught

