# Link: https://leetcode.com/problems/reverse-integer
# Status: Solution accepted and beats 91.64%

# Problem statement: Given a list of strings, return the common prefix between all of them.
# My solution is to loop through the chars and add them to the output if it is in all the strings. If it is not in all of them, then return the output

class Solution(object):
    def longestCommonPrefix(self, strs: list[str]):
        
        output : str = ""
        i : int = 0
        max_len = min([len(x) for x in strs])
        while i < max_len:
            in_all : bool = True
            current_char : chr = strs[0][i]
            for w in strs:
                if w[i] != current_char:
                    in_all = False
            if in_all:
                output += current_char
                i += 1
            else:
                break
        
        return output




    def _longestCommonPrefix(self, strs):
        """
        Old solution for Python (not 3)
        :type strs: List[str]
        :rtype: str
        """
        
        output = ""
        
        sorted_list = sorted(strs,key=len)
        
        for i in range(len(sorted_list[0])):
            equal = 1
            candidate = sorted_list[0][i]
            for s in sorted_list:
                if s[i] != candidate:
                    equal = 0
            
            if equal == 1:
                output += candidate
            else:
                return output
            
        return output


if __name__ == "__main__":
    testcases = [["flower","flow","flight"], ["dog","racecar","car"]]

    for ts in testcases:
        print(f"testcase: {ts}, result: {Solution.longestCommonPrefix(None,ts)}")