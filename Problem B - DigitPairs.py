'''
    Problem B: Digit Pairs
'''
class Solution(object):
  
    """ 
    Function to Take Input N and the Array
    This Function Includes:
        1. Input of n and Arr.
        2. Initializing Necessary Elements
    """
    def __init__(self):

        self.n = int(input())  ### Size of Array
        self.arr = list(map(int, input().split()))

        # assert len(self.arr) == self.n

        self.BitScore = [""] * self.n  # Contains the BitScore
        self.score = 0 ### Contains Current Score
        self.EvenPositionFrequency = [0] * 10 ### Even Position Frequency 
        self.OddPositionFrequency = [0] * 10 ### Odd Position Frequency
        self.PAIRS = [0] * 10  ### Answer ie. No. of bit Pairs

        self.findSolution() ### Pseudo Code to find Solution
        pass
    
    
    ### Calculate Bit Score
    def calculateBitScore(self):
        for i in range(len(self.BitScore)):
            self.score = str(
                11 * self.MaximumInTheArray(self.arr[i])
                + 7 * self.MinimumInTheArray(self.arr[i])
            )
            if len(self.score) > 2:
                self.score = self.score[-2:]
            self.BitScore[i] = self.score
    
    
    
    ### Calculate No. of Bit Pairs
    def calculateBitPairs(self):
        for i in range(10):
            if self.EvenPositionFrequency[i] <= 1 and self.OddPositionFrequency[i] <= 1:
                continue

            self.PAIRS[i] += self.findPairs(
                self.EvenPositionFrequency[i]
            ) + self.findPairs(self.OddPositionFrequency[i])
            self.PAIRS[i] = min(2, self.PAIRS[i])
    
    
    ### Calculating Frequencies for Odd and Even on Index of BitScore
    def calculateBitPairsForEvenOdd(self):
        for i in range(len(self.BitScore)):
            index = int(self.BitScore[i][0])

            if (i + 1) % 2 == 0:
                self.EvenPositionFrequency[index] += 1
            else:
                self.OddPositionFrequency[index] += 1
      
      
    """
    Function to find the Solution
    """
    def findSolution(self):
        
        ### Calculating the Bit Score
        self.calculateBitScore()
        
        
        ### Calculating Frequencies for Odd and Even
        ### Calculating Frequencies for Odd and Even on Index of BitScore
        self.calculateBitPairsForEvenOdd()
        
        
        ### Calculating No. of Bit Pairs
        self.calculateBitPairs()

      
    """
    Function to find the Maximum in the Number
    """
    def MaximumInTheArray(self, number):
      
        string_of_number = str(number) ### String of the Number
        i = 9
        while i >= 0:
            if str(i) in string_of_number:
                return i
            i -= 1

      
    """
    Function to find the Minimum in the Number
    """

    def MinimumInTheArray(self, number):
      
        string_of_number = str(number) ### String of the number
        i = 0
        while i <= 9:
            if str(i) in string_of_number:
                return i
            i += 1


    """
    Function to find the PAIRS
    """
    def findPairs(self, number):
      
        if number == 2:
            return 1
        if number >= 3:
            return 2
        return 0


    """
    Function to print the OUTPUT ie. No. of Pairs
    """
    def __del__(self):
        print(sum(self.PAIRS), end='')
        pass


      
"""
    Defining Main Function
"""
def main():
    obj = Solution()


    
if __name__ == "__main__":
    main()