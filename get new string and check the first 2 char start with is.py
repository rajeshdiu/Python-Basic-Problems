def myFunction(str):
    if len(str)>2 and str[:2]=="is":
        return True
    else:
        return False

string=input("Enter new string: ")
print(myFunction(string))