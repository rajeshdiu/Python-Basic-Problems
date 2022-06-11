def myFunction(n):
    myList=[]
    for i in range(n):
        myList.append(input())
    myList2=[]
    myList2.append(myList[0])
    myList2.append(myList[-1])

    return myList2

n=int(input("Enter Range : "))
print("First and Last Item is :",myFunction(n))