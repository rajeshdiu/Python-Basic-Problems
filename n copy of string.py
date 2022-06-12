from unittest import result


def myFunction(str,n):
    result=""
    for i in range(n):
        result+=str+" "
    return result

string=input("Enter new string: ")
n=int(input("How many Copy? "))
print(myFunction(string,n))