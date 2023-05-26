def substract(a =8, b =6) :
    return a -b

n1 = substract() # take the default values
n2 = substract(10) # 10 will be passed to a
n3 = substract(16,22) # both these value will be assigned to a , b
n4 = substract(b=8,a=6) #values will be passed based on the arguments names not per the order - named arguments
print(n1,n2,n3,n4)

# arbitrary arguments - if we dont know the no of arguments then will use the same

def multiply (*numbers) :
    mul = 1
    for i in numbers :
        print("number is ", i)
        mul *= i
    return mul

mul1 = multiply(1,2)
mul2 = multiply(1,2,3,4)
mul3 = multiply()
print(mul1,mul2, mul3)