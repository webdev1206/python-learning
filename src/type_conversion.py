n,f,s = 4,2.1,'S'

print(n+f, type(n+f)) # implicit type conversion - float

# print(n+s) -- TypeError: unsupported operand type(s) for +: 'int' and 'str' - cant convert int to string in implicit type conversion

# print(s+n) -- TypeError: can only concatenate str (not "int") to str

print(n*f, type(n*f))

print(n-f, type(n-f))

print(n / f, type(n/f))

# print(s/n) -- TypeError: unsupported operand type(s) for /: 'str' and 'int'

s1 = '2'

# print(n+s1) - TypeError: unsupported operand type(s) for +: 'int' and 'str'

s1 = int(s1)

print(s1,type(s1))

print(n+s1)

# Explicit type conversion - type casting

# s = int(s) -- ValueError: invalid literal for int() with base 10: 'S'

print(int(f))

s2 = '33'
print(float(s2))
print(float(n))

print(str(n), type(str(n)))
print(str(f), type(str(f)))