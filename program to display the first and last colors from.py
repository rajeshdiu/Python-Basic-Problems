def myFunction(n):
    myList=[]
    for i in range(n):
        myList.append(input())
    print("First and Last Item is : ",myList[0],myList[-1])

n=int(input("Enter Range : "))
print(myFunction(n))