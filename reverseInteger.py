# Link: https://leetcode.com/problems/reverse-integer
# Status: Solution accepted and beats 76%

# Problem statement: Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-2**31, 2**31 - 1], then return 0.

# My solution is to create a list with all the digits -> reverse it -> join them
# If the solution is out the limits, then return 0
# Disclamer: I should assume the environment does not allow you to store 64-bit integers (signed or unsigned). I'm not taking that into account on this solution
# Idea: Use bit manipulation to solve problem

class Solution:
    def reverse(self, x: int) -> int:
        digit_list : list[int] = []
        sign : int = (x > 0)*1 + (x < 0)*(-1)
        x = abs(x)
        while x != 0:
            rem : int = x % 10
            x = x // 10
            digit_list.append(rem)

        out : int = 0
        ln : int = len(digit_list)
        for i in range(ln):
            out += digit_list[i]*(10**(ln - 1 - i))
        
        out = sign*out

        if out < -2**31 or out > 2**31-1:
            return 0
        return out

    def _reverse(self, x):
        """
        Old solution for Python (not 3)
        :type x: int
        :rtype: int
        """
        """
        output = 0
        
        div = abs(x)
        res = 0
        
        while(div != 0):
            res = div % 10
            div = div//10
            output = output*10 + res
        
        """
        
        output = str(abs(x))
        output = output[::-1]
        output = int(output)
        
        if x < 0:
            output = -output
            
        if output < -2**31 or output > 2**31-1:
            return 0
        
        return output


if __name__ == "__main__":
    testcases = [-123]

    for ts in testcases:
        print(f"testcase: {ts}, result: {Solution.reverse(None,ts)}")