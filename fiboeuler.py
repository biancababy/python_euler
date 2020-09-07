
#sum of  the even fibonacci series

total = 0
x,y = 0,1
fib = []
while y < 4000000:
    x, y = y, x + y
    fib.append(y)
    if y % 2:
        continue
    total += y

print(fib)
print(total)


