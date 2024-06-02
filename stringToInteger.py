# Link: https://leetcode.com/problems/string-to-integer-atoi
# Status: Solution accepted and beats 90.96%

# Problem statement: Implement the atoi function, which takes a string and converts it into a 32-bit signed integer

# We must follow the following rules:
# 1 -> Ignore the leading whitespaces
# 2 -> If the first proper character is "-" it is negative, if it is a digit or "+" it is positive
# 3 -> Current output starts as 0
# 4 -> Ignore leading zeros
# 5 -> Add digits until the string finishes or there is a non-digit character
# 6 -> Round the resultant number to -2**31 or 2**31 -1

# Solution uses an iterative approach fulling all the rules


class Solution:
    def myAtoi(self, s: str) -> int:
        
        #In case the string is empty, return 0
        if s == "":
            return 0
        
        #First let's ignore the leading whitespaces

        index : int = 0
        N : int = len(s)
        while index < N and s[index] == ' ':
            index += 1

        if index == N:
            return 0

        #Now, let's check if we have a sign
        sign : int = 1

        if s[index] == '-':
            sign = -1
            index += 1
        elif s[index] == '+':
            index += 1
        
        if index == N:
            return 0
        
        #Now, let's ignore leading zeros

        while index < N and s[index] == '0':
            index += 1
        
        if index == N:
            return 0

        out : int = 0

        while(index < N and (s[index] >= '0' and s[index] <= '9')):
            out = out*10 + int(s[index])
            index += 1

        out = sign * out

        if out < -2**31:
            return -2**31
        elif out > 2**31-1:
            return 2**31-1
        
        return out


    def _myAtoi(self, s):
        """
        Old solution for Python (not 3)
        Accepted and beats 89.91%
        :type s: str
        :rtype: int
        """
        sign = 1
        index = 0
        output = 0
        N = len(s)
        
        if N == 0:
            return 0
        
        while(index < N and s[index] == ' '):
            index+=1
        
        if index >= N:
            return 0
        
        if s[index] == '-':
            sign = -1
            index += 1
        elif s[index] == '+':
            index += 1
        
        while(index < N and (s[index] >= '0' and s[index] <= '9')):
            output = output*10 + int(s[index])
            index += 1
            
        output = output*sign
            
        if output < -2**31:
            return -2**31
        elif output > 2**31-1:
            return 2**31-1
        
        return output