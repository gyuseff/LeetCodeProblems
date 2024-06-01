# Link: https://leetcode.com/problems/roman-to-integer
# Status: Solution accepted and beats 94%

# Problem statement: Convert an string representing a Roman number to an integer.

# My solution is just iterate through the string with an index, making sure to follow the Roman number rules

class Solution:
    def romanToInt(self, s: str) -> int:
        index : int = 0
        output : int = 0
        s_len : int = len(s)
        while index < s_len:
            if s[index] == 'M':
                output += 1000
                index += 1
            elif s[index] == 'D':
                output += 500
                index += 1
            elif s[index] == 'C':
                output += 100
                index += 1
                if index < s_len:
                    if s[index] == 'M':
                        output += 800
                        index += 1
                    elif s[index] == 'D':
                        output += 300
                        index += 1
            elif s[index] == 'L':
                output += 50
                index += 1
            elif s[index] == 'X':
                output += 10
                index += 1
                if index < s_len:
                    if s[index] == 'C':
                        output += 80
                        index += 1
                    elif s[index] == 'L':
                        output += 30
                        index += 1
            elif s[index] == 'V':
                output += 5
                index += 1
            elif s[index] == 'I':
                output += 1
                index += 1
                if index < s_len:
                    if s[index] == 'X':
                        output += 8
                        index += 1
                    elif s[index] == 'V':
                        output += 3
                        index += 1
        return output
