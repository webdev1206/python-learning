tuple=('a',1)
print(tuple[1])
tuple1 = 1,2,'3'
print(type(tuple1))
tuple2 = 'name',
print(type(tuple2))
s='name'
print(type(s))
print(tuple2)
print(tuple1[2])
print(type(tuple1[2]))
#print(tuple1[4])

print(tuple1[-2]) # from last item is negative indexing

tuple4 = ('a',1,'b',2,'c',3,'d',4,'e',5)
#slice
print(tuple4[2:6])
print(tuple4[:])
print(tuple4[:-6])
print(tuple4[6:])

#methods
print(tuple4.count(2))
print(tuple4.index(3))

#iterating

for i in tuple4:
    print(i)

#checking the values existed in tuple or not
print(2 in tuple4)
print('x' in tuple4)


