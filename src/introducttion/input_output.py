print('Hi',end = ' ') # if we dont specify the end then default value of end is \n
print('How are you?')

print('a','b','c', sep='-')

s ='zazu'
s1 = 'pandu'
print(s +' '+ s1) #strings can be concatenated using the + operator

print('The first name is {} and last name is {}'.format(s,s1)) #if we use the variable/loteral which hasnt been declared then will get error like this NameError: name 'x' is not defined



n = input('enter a number :')
print('you have entered ', n)
print('type of entered value is', type(n))

num = int(input('enter a number :')) # ValueError: invalid literal for int() with base 10: 'tn' - if we pass string
print('you have entered ', num)
print('type of entered value is', type(num))