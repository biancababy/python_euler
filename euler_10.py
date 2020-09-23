
"""
n = 1 x n
    a x b
    ..
    sqrt(n) x sqrt (n)
    ..
    b x a
    n x 1
"""

import time
import math


def is_prime_v(n):
    #return "True" if n is prime else "False
    count =0
    math_divisor = math.floor(math.sqrt(n))

   # if n == 1:
       # return False  #1 is not prime nor composite
    if n == 2:
        return True
    elif n > 2 and n % 2 == 0:
        return False

    for d in range(3, 1+ math_divisor,2):
        if n % d == 0:
            return False
    return True

t0 =time.time()        #Time Function
sum = 0
for i in range(2,2000000):
    if(is_prime_v(i)):
        sum = sum + i
print("Sum required: ",sum)

t1= time.time()
print("time required: ",t1 - t0)
