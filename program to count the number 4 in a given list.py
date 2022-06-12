from itertools import count


def myFunction(n):
    myList=[]
    for i in range(n):
        myList.append(int(input()))
    print(myList)
    count=0
    for i in range(n):
        if myList[i]==4:
            count=count+1
    return count
n=int(input("Enter Range of List : "))
print(myFunction(n))