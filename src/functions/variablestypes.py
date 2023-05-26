m = 10 # here m is global variable
def sum (n) :
    m = 1 # here m is local variable to the fucntion
    return m + n

s = sum(3)
print(s)
#print(m) # NameError: name 'm' is not defined - so m is local variable to the function sum

# outside function 
def outer():
    message = 'local'

    # nested function  
    def inner():

        # declare nonlocal variable
        nonlocal message # so it changes the outer fun message as well - if we comment this message variable has it own local scope to outer and inner it wont change the outer func message

        message = 'nonlocal' 
        print("inner:", message)

    inner()
    print("outer:", message)

outer()
