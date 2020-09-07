# series of prime numbers
"""""
upper = int(input("Enter any upper range: "))

for number in range(2,upper+1):
    # prime number is always greater than 1
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
              #  print(number, "is not a prime number")
                break
        else:
            #print(number, "is a prime number")
            print(number)
            pass
"""

# Python Program to find Prime Factors of a Number
#import numpy as np
Number = int(input(" Please Enter any Number: "))
i=1
#arr=[]
while (i <= Number):
    count = 0
    if (Number % i == 0):
        j = 1
        while (j <= i):
            if (i % j == 0):
                count = count + 1
            j = j + 1
        if (count == 2):
            print(" {} is a Prime Factor of {}" .format(i, Number))
            large =i
            #arr.append(i)  #storing in a list the values
    i = i + 1

print("Largest prime factor of {} is {}".format(Number,large))

#max_value = np.max(arr)   #if storing in an array
#print("Largest prime factor of {} is {}".format(Number,max_value))