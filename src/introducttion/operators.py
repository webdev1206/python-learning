# arithmetic operators : + - * / % // **
x,y = 8, 5

print('sum :', x+y)

print('sub :', x-y)

print('mul :', x*y)

print('div :', x/y)

print('mod :', x%y)

print('floor div :', x//y)

print('power :', x**y)


# assignment operators : = += -= *= /= %= **= //=

n = 8

print(n)
n += 1
print('after addition assignment :', n)

n //= 5
print(n)

# comparision operators : == >= <= != > <

print(1 == '1')

print(1 == 1.0)


# logical operators: and or not
print ('logical operators')

print( 2 > 1 and 3 > 2)

print( 2 > 1 and 1 > 2)

print( 2 > 1 or 1 > 2)

print (not 2 > 1)

# bitwise operators: & | ^ << >> ~
print('bitwise operators:')
bx, by = 10, 4 # 0000 1010 , 0000 0100

print(bx & by)

print(bx | by)

print(~bx)

print(bx >> 1)

print(by << 1)


# special operators - identity operators - is is not
print('identity operators:')
fname,lname,shortname = 'zazu','k','zazu'
print(fname is lname)
print(fname is not lname)
print(fname is shortname)

# membership operators : in not in
print('membership operators:')

dict = {'fname':fname,'lname':lname,'shortname':shortname} #disctionary
str ='zazu is a good boy'
print('Z' in str)
print('z' in str)
print('good' in str)

print('fname' in dict)
print('fname' not in dict)




