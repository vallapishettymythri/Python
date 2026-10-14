#LONGEST COMMON PREFIX
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        s=""
        first=strs[0]
        for i in range(len(first)):
            for word in strs:
                 if i >= len(word) or first[i] != word[i]:
                    return s
            s += first[i]
        return s