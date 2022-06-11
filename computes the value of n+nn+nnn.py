def myFunction(n):

    n1 = int( "%s" % n )
    n2 = int( "%s%s" % (n,n))
    n3 = int( "%s%s%s" % (n,n,n))
    return (n1+n2+n3)

n=int(input("Enter Number: "))
print(myFunction(n))