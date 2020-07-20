### Import Math Librar for math.ceil()
import math

### Factorial of 1 to 30 Numbers
factorial = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 
3628800, 39916800, 479001600, 6227020800, 87178291200, 1307674368000, 20922789888000,
355687428096000, 6402373705728000, 121645100408832000, 2432902008176640000, 51090942171709440000, 1124000727777607680000,
25852016738884976640000, 620448401733239439360000, 15511210043330985984000000, 403291461126605635584000000,
10888869450418352160768000000, 304888344611713860501504000000, 8841761993739701954543616000000, 265252859812191058636308480000000
] ### Factorials of First 30 Numbers:: Source==> https://www.mymathtables.com/numbers/100-factorial-tables-chart.html


#### This class Contains the Pseudo Code of the Problem
class Solution(object):

	""" Function for Input Data and calculating
	1. Remaining LuckyAttack
	2. Probability of Lucky
	3. Probability of Not Lucky
	4. Current Fraction
	"""
	def __init__(self):
		### Input Data into A, H, L1, L2 , M, C as A, H, num1, num2, M, c
		A, H, num1, num2, M, C = list(map(int, input().split()))

		number1, number2 = 0, 0

		### Base Condition
		if (A + C) * M < H:
			print("RIP")
			return

		if (A * M) >= H:
			number1, number2 = 1, 1
			numer = number1/(self.findEuclideanGCD(number1, number2))
			denom = number2/(self.findEuclideanGCD(number1, number2))

			print("{}/{}".format(numer, denom))
			return

		remaining = H - (A * M)
		rLuckyAttack = math.ceil(remaining / C)

		currentFraction = [0, 1]
		probabililityLucky = [num1//(self.findEuclideanGCD(num1, num2)), num2//(self.findEuclideanGCD(num1, num2))]
		probabililityNotLucky = self.PerformSubtraction([1, 1], probabililityLucky)

		for i in range(rLuckyAttack, M+1):
			currentProbability = self.PerformMultiplication(self.PerformCombination(M, i), self.PerformExponential(probabililityLucky, i))
			currentNotProbability = self.PerformExponential(probabililityNotLucky, M-i)
			currentProbability = self.PerformMultiplication(currentProbability, currentNotProbability)
			currentFraction = self.PerformAddition(currentFraction, currentProbability)

		print("{}/{}".format(currentFraction[0], currentFraction[1]))
		pass

	""" 
	Using Euclidean GCD Algorithm for finding Greatest Common Divisor or HCF of two numbers
	"""
	def findEuclideanGCD(self, a, b): ### Snippet Taken from GFG
	    if (a == 0):
	        return b
	    return self.findEuclideanGCD(b % a, a)
	    

	"""Function for subtraction """
	def PerformSubtraction(self, number1, number2):
		numer = number1[0] * number2[1] - number2[0]*number1[1]
		denom = number1[1] * number2[1]

		num = numer//self.findEuclideanGCD(numer, denom)
		den = denom//self.findEuclideanGCD(numer, denom)

		return [num, den]


	""" Function for Addition"""
	def PerformAddition(self, number1, number2):

		numer = number1[0]*number2[1] - number2[0] * number1[1]
		denom = number1[1]*number2[1]

		num = numer//self.findEuclideanGCD(numer, denom)
		den = denom//self.findEuclideanGCD(numer, denom)

		return [num, den]


	""" Function for Multiplications"""
	def PerformMultiplication(self, number1, number2):
		numer = number1[0] * number2[0]
		denom = number1[1] * number2[1]

		num = numer//self.findEuclideanGCD(numer, denom)
		den = denom//self.findEuclideanGCD(numer, denom)

		return [num, den]


	"""Function for Performing Exponentials"""
	def PerformExponential(self, number1, size):
		ans=[1, 1]
		for i in range(size):
			ans = self.PerformMultiplication(ans, number1)
		return ans


	""" Function for calculating nCr (Combinations)"""
	def PerformCombination(self, N, R):
		if N == R or R == 0:
			return [1, 1]

		if R == 1 or R == N-1:
			return [N, 1]

		numer = factorial[N]
		denom = factorial[R] * factorial[N-R]

		num = numer//self.findEuclideanGCD(numer, denom)
		den = denom//self.findEuclideanGCD(numer, denom)

		return [num, den]


	def __del__(self):
		pass


### Main Function
def main():
	T = int(input())
	for case in range(T):
		obj = Solution()



if __name__ == '__main__':
	main()

"""
2
10 33 7 10 3 2
10 999 7 10 3 2
"""

### 98/125
### RIP