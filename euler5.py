
"""
The ans must be the LCM of the numbers 1 to n.
To find LCM of numbers from 1 to n –

1.Initialize ans = 1.
2.Iterate over all the numbers from i = 1 to i = n.
3.At the i’th iteration ans = LCM(1, 2, …….., i). This can be done easily as LCM(1, 2, …., i) = LCM(ans, i).
		Thus at i’th iteration we just have to do –
			ans = LCM(ans, i) 
     			    = ans * i / gcd(ans, i) [Using the below property,
                                 a*b = gcd(a,b) * lcm(a,b)
"""

import math

# Returns the lcm of first n numbers
def lcm(n):
	ans = 1
	for i in range(1, n + 1):
		ans = int((ans * i) / math.gcd(ans, i))
	return ans

# main program

n = int(input(" Please Enter range: "))
# n = 20
print(lcm(n))