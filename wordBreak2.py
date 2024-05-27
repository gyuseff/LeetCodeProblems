class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:

        output : list[str] = []

        min_len = min([len(x) for x in wordDict])

        def recursion(s: str, current_sol: str) -> None:
            if s == "":
                output.append(current_sol[1:])
                return
            if len(s) < min_len:
                return
            
            for w in wordDict:
                ls = len(s)
                lw = len(w)
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