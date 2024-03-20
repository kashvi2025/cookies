
#attempt1
listt= [2,2,3,4,5,5]

def norepeats(listtt):
    for i in listtt:
        count=0
        for j in listt:
            if i==j and count>1:
                listtt.remove(i)
    return listtt
    
result= norepeats(listt)
print(result)
#this didn't work because 

listt= [2,2,3,4,5,5]
#attempt 2
def norepeats(listtt):
    listd=[]
    for i in listtt:
        count=0
        for j in listt:
            if i==j:
                count+=1
                if count==0:
                    listd.append(i)
    return listtt
result= norepeats(listt)
print(result)
# this didn't work because the if loop indentation was wrong and it was returning the wrong list

#attempt 3
def norepeats(listtt):
    listd=[]
    for i in listtt:
        count=0
        for j in listt:
            if i==j:
                count+=1
        if count==1:
            listd.append(i)
    return listd
#this was correct