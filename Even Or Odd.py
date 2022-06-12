def myFunction(n):
    if n%2==0:
        r="Even"
    else:
        r="Odd"
    return r

n=int(input("Input Enter Number :"))
print(myFunction(n))