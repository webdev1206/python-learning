glo_var = 11

def outer_func():
    outer_var = 22
    #print(inner_var) #NameError: name 'inner_var' is not defined
    def inner_func():
        inner_var = 33
        print(inner_var)
        print(outer_var)
        print(glo_var)
    inner_func()
outer_func()