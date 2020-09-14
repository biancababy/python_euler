"""""
def check_pythagorean(a, b, c):
	return (a**2) + (b**2) == (c**2)

SUM = 1000

for i in range(1, SUM):
	for j in range(i+1, SUM):
		c = SUM - (i + j)
		if(check_pythagorean(i, j, c)):
			if i + j + c == SUM:
				print(i * j * c)
				break
"""
import numpy


def check_pythagorean(a, b, c):
    return a ** 2 + b ** 2 == c ** 2

SUM =1000

for a in range(1, SUM):
    for b in range(a + 1, int(numpy.ceil((SUM - a) / 2. - 1))):
        c = 1000 - a - b
        if (check_pythagorean(a, b, c)):
            if a + b + c == SUM:
                print(a * b * c)
                break