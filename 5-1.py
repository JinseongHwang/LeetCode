# 문자열 조작
# 5. Longest Palindromic Substring
# 투포인터

from typing import *


class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(L, R):
            while 0 <= L and R <= len(s) and s[L] == s[R - 1]:
                L -= 1
                R += 1
            return s[L + 1: R - 1]

        if len(s) < 2 or s == s[::-1]:
            return s

        result = ''
        for i in range(len(s) - 1):
            result = max(result,
                         expand(i, i + 1),
                         expand(i, i + 2),
                         key=len)
        return result


