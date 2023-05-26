
#language("java") ---- NameError: name 'language' is not defined
def language (name) :
    print("language name is --- " + name)

language("java")
language("js")
language("go")
language("python")

def sum(n1, n2) :
    print("sum is ", n1 + n2)
    return n1 + n2

sum(2,3)

sum(n1 =6,n2=8)
#sum(num1=4, num2 =6) --- TypeError: sum() got an unexpected keyword argument 'num1'

sum1 = sum(1,2)
print("sum1 is ---", sum1)