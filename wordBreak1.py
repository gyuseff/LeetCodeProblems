# Link: https://leetcode.com/problems/word-break
# Status: Accepted and beats 93.42%!

# Problem statement: For a string "s" and a list of strings "wordDict"; 
# return true if there is a possible way to form s, concatenating the strings in wordDict

# Had tried with recursion; it works but in certain testcases it exceeds runtime
# Solution uses a Dynamic programming approach; as the whole string must be created with the wordDict:
# 1 -> Create a list of len(s) + 1 booleans with default false and list[0] = True; the list represents that I can create the substring up to each position. So if list[i] == True, it means I can use a combination of the strings in wordDict to create substring s[:i]
# 2 -> Iterate through the string; if list[i] is true, then iterate thorugh each word w of wordDict, if s[i:i+len(w)] == w (the current substring of s starts with w) -> list[i + lw] == True
# 3 -> When finishing the iteration, if the last boolean of the list is True, then we can recreate the whole string s with a concatenation of wordDict

class Solution:
    
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        
        ls = len(s)

        if ls == 0:
            return False
        
        solutions = [False for x in range(ls+1)]
        solutions[0] = True

        for i in range(ls):
            if solutions[i]:
                for w in wordDict:
                    lw = len(w)
                    if i + lw < ls + 1:
                        if s[i:i+lw] == w:
                            solutions[i+lw] = True
        
        return solutions[-1]
    

if __name__ == "__main__":
    testcase_1: tuple[str,list[str]] = ("catsanddog", ["cat","cats","and","sand","dog"])
    testcase_2: tuple[str,list[str]] = ("pineapplepenapple", ["apple","pen","applepen","pine","pineapple"])
    testcase_3: tuple[str,list[str]] = ("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"])

    testcase_4 : tuple[str, list[str]] = ("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", ["aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa","ba"])

    testcases : list[tuple[str,list[str]]] = [testcase_1, testcase_2, testcase_3, testcase_4]

    for ts in testcases:
        print(ts)
        print(Solution.wordBreak(self=None, s=ts[0], wordDict=ts[1]))