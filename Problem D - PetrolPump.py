''' 
	Problem D: Petrol Pump
'''

class Solution(object):
  	
    def __init__(self):
      	self.arr = list(map(int, input().split()))
        self.difference = self.findDifference()

        self.min_prob = (sum(self.arr) - self.difference) / 2
        self.max_prob = min_prob + self.difference

        pass
      
    def __del__(self):
      	print(self.max_prob)
      
    def findSolution(self):

        size = len(self.arr)-1
        sumOfArray = sum(self.arr)

        memory = [[0 for i in range(sumOfArray+1)] for j in range(sumOfArray+1)]

        for i in range( + 1):
            memory[i][0] = True

        for i in range(1, sumOfArray+1):
            dp[0][i] = False


        for i in range(1, size+1):
            for j in range(1, sumOfArray+1):

                memory[i][j] = memory[i-1][j]

                if self.arr[i-1] <= j:
                    memory[i][j] |=memory[i-1][j-self.arr[i-1]]

            for j in range(sumOfArray//2, -1, -1):

                if memory[size] is True:
                    diff = sumOfArray - (2*j)
                    break
            return
      

def main():
  	pass
  

if __name__ is '__main__':
  	main()

''' 
1 2 3 4 5 10 11 3 6 16
'''
### 31


'''
25 30 35 20 90 110 45 70 80 12 30 35 85
'''
### 335