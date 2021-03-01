# 문자열 조작
# 344. Reverse String
# 투포인터 사용

class Solution:
    def reverseString(self, s: List[str]) -> None:
        listLen = len(s)
        for i in range(listLen // 2):
            s[i], s[listLen - i - 1] = s[listLen - i - 1], s[i] # swap
