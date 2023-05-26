vals = range(10)
for v in vals :
    print(v)
    if(v // 2 == 2) :
        print(v)
        break

n = 10
while (n > 0) :
    n -= 1
    if(n % 2 == 0) :
        continue

    print("odd number is",n)