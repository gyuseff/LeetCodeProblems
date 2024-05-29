# Link: https://leetcode.com/problems/word-break
# Status: Solution not accepted

# Problem statement: For a string "s" and a list of strings "wordDict"; 
# return true if there is a possible way to form s, concatenating the strings in wordDict

# Had tried with recursion; it works but in certain testcases it exceeds runtime
# Current solution tries a Dynamic programming approach, however it is wrong.
# It uses a pointer to a current index to start, checks if I can add any word that goes through that index and moves
# It is a wrong algorithm, because it allows for the superposition of words

class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:

        index = 0
        ls = len(s)
        while index < ls:
            for w in wordDict:
                j = 0
                lw = len(w)
                found = False
                while j < lw:
                    try:
                        if s[index-j:index-j+lw] == w:
                            found = True
                            break
                        else:
                            j += 1
                    except:
                        j = lw
                        break
                if j < lw:
                    index += (lw - j)
                    break
            if not found:
                return False
        
        if index >= ls:
            return True

    

if __name__ == "__main__":
    testcase_1: tuple[str,list[str]] = ("catsanddog", ["cat","cats","and","sand","dog"])
    testcase_2: tuple[str,list[str]] = ("pineapplepenapple", ["apple","pen","applepen","pine","pineapple"])
    testcase_3: tuple[str,list[str]] = ("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"])

    testcase_4 : tuple[str, list[str]] = ("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", ["aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa","ba"])

    testcases : list[tuple[str,list[str]]] = [testcase_1, testcase_2, testcase_3, testcase_4]

    for ts in testcases:
        print(Solution.wordBreak(self=None, s=ts[0], wordDict=ts[1]))