# Link: https://leetcode.com/problems/word-break-ii
# Status: Accepted and beats 97%!

# Problem statement: For a string "s" and a list of strings "wordDict" we want to return all the possible combinations
# of wordw in wordDict (can be repetated) so that it forms string "s"

# My solution: Use recursion that takes a current string "s" + wordDict + a current solution list
# Idea: Use backtracking to check all possible combinations and see if they work
# Base case 1: The current string is empty -> The current solution works -> append it to the output
# Base case 2: The current string is shorter than any word in wordDict -> I can't trim this string any longer
# In each recursive call I check if the current string "s" starts with each of the word, if it does, call recursion in s - word and add word to the solution

class Solution:

    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:

        output : list[str] = []

        min_len = min([len(x) for x in wordDict])

        def recursion(s: str, current_sol: str) -> None:
            #Base cases
            if s == "":
                output.append(current_sol[1:])
                return
            if len(s) < min_len:
                return
            
            #Actual recursive call

            for w in wordDict:
                ls = len(s)
                lw = len(w)
                
                #If length of the current string s is less than the current word (to avoid index out of range error)
                #AND s starts with the current word
                #Let's invoke the recursion on s trimed from the new word and append w to the current solution
                if ls >= lw:
                    if s[0:lw] == w:
                        new_s = s[lw:]
                        recursion(new_s, current_sol + " " + w)
        
        recursion(s, "")
    
        return output



        


if __name__ == "__main__":
    testcase_1: tuple[str,list[str]] = ("catsanddog", ["cat","cats","and","sand","dog"])
    testcase_2: tuple[str,list[str]] = ("pineapplepenapple", ["apple","pen","applepen","pine","pineapple"])
    testcase_3: tuple[str,list[str]] = ("catsandog", ["cats","dog","sand","and","cat"])

    testcases : list[list[list[int]]] = [testcase_1, testcase_2, testcase_3]

    for ts in testcases:
        print(Solution.wordBreak(self=None, s=ts[0], wordDict=ts[1]))