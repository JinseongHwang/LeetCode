# 문자열 조작
# 125. Valid Palindrome
# 리스트로 변환

class Solution:
    def isPalindrome(self, s: str) -> bool:
        compressed = []
        for c in s:
            if c.isalnum():  # 알파벳 & 숫자
                compressed.append(c.lower())

        L, R = 0, len(compressed) - 1
        while R - L >= 1:
            if compressed[L] != compressed[R]:
                return False
            L += 1
            R -= 1

        return True
