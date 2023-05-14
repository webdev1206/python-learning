global_var = 22

def func():
    global_var = 33
    print(global_var)
print(global_var)
func()
print(global_var)

def func1():
    global global_var
    global_var = 33
    print(global_var)
print(global_var)
func1()
print(global_var)