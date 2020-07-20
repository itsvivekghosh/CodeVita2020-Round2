'''
    Problem E: Grooving Monkeys
'''

### Pseudo Code
class Solution(object):
  
    ### Initializer or Contructor to Input Data ie. N and Array
    def __init__(self):
      
        self.n = int(input())
        self.arr = list(map(int, input().split()))
        self.ans = 0

        self.findSolution()
        pass
    
    
    '''
        Destructor to print Answer or 
        minimum number of seconds after which all the monkeys are in their initial position
    '''
    def __del__(self):
        
        print(self.ans, end=" ")
        pass
    
    
    ### Insert 0 in the Beggining and Initialize 0 array of size (n + 1)...
    def processInputs(self):

        self.arr.insert(0, 0)
        self.temp = [i for i in range(self.n + 1)]
        self.OriginalPosition = self.temp
        pass
    
    
    ### Pseudo Code to Find Solution
    def findSolution(self):

        self.processInputs()
        while 1:

            diffn = [0 for i in range(self.n + 1)]

            for i in range(1, self.n + 1):
                diffn[self.arr[i]] = self.temp[i]

            self.ans += 1

            if self.OriginalPosition == diffn:
                break

            self.temp = diffn

        pass


### Main Function      
def main():
    t = int(input())
    while t:
        obj = Solution()
        t -= 1


        
if __name__ == "__main__":
    main()
