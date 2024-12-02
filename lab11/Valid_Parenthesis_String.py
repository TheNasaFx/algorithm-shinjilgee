class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        low = 0  
        high = 0  

        for char in s:
            if char == '(':
                low += 1
                high += 1
            elif char == ')':
                low = max(low - 1, 0)
                high -= 1
            elif char == '*':
                low = max(low - 1, 0)  
                high += 1 

            if high < 0:
                return False

        return low == 0
