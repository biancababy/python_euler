

def sum_square(n):
       return ((n*(n+1)*((2*n)+1))/6)


def square_sum(n):
    sum = 0
    for i in range(n+1):
        sum =sum+i
    return pow(sum, 2)

z = int(input(" Please Enter any Number: "))
result = square_sum(z) - sum_square(z)
print(int(result))



