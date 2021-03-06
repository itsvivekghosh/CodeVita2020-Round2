"""
    Psudo Code to find Solution
"""
def findSolution(n, bribes, groom):

    ans = 0 ### Answer
    count_m = groom.count('m') ### Count for each 'm' in GROOMS Array
    count_r = groom.count('r') ### Count for each 'r' in BRIBES array

    array = [value for value in bribes] ### Making a list of brides

    ### Iterating over each element of Bribe and check for relevant condition
    for x in bribes:

        """ 
            If the value is 'r' then:
            1. Check if r is count of 'r' is zero, if yes, then ans is length of array
            2. Or if no, decrease the value of count of r and pop the first element from array. 
        """
        if x == 'r':
            if count_r == 0: ### IF there are no 'r' in the queue
                ans = len(array)
                break
            count_r -= 1
            array.pop(0)
        
        
        elif x == 'm':
            if count_m == 0: ### If there are no 'm' in the queue
                ans = len(array)
                break
            count_m -= 1
            array.pop(0)

    """ 
        Return answer
    """
    return ans


### Main function()
#### Driver Code
def main():
    n = int(input())
    bribes = input()
    groom = input()
    print(findSolution(n, bribes, groom))



if __name__ == '__main__':
    main()

"""
4
rmrm
mmmr

4
rrmm
mrmr
"""

### 0
### 2