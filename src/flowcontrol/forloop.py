frts = ["mango","banana","orange"]
for frt in frts :
    print(frt)

str = "PySpark"
for s in str:
    print(s)

vals = range(6)
for v in vals :
    print(v)

# we can use _ for mot metioning any element in for loop iteration
for _ in vals :
    print("its for loop")

for v in vals:
    print(v)
else :
    print("no vals left")
sum = 0
for v in vals :
    sum += v
print(sum)