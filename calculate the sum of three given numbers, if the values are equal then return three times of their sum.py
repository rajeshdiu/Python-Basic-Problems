def myFunction(n1,n2,n3):
    sum=0
    if n1==n2==n3:
        sum=n1+n2+n3
        print("Summation is = ",sum)
        return sum
    else:
        return sum

num1=int(input("Enter Number1="))
num2=int(input("Enter Number1="))
num3=int(input("Enter Number1="))

print(myFunction(num1,num2,num3))