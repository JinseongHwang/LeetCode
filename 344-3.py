# 문자열 조작
# 344. Reverse String
# 문자열 슬라이싱 사용

class Solution:
    def reverseString(self, s: List[str]) -> None:
        # 원래는 s = s[::-1] 도 정상적으로 작동해야 하지만 LeetCode 플랫폼에서 적용되지 않는 맹점이 있음.
        # 따라서 아래와 같은 꼼수 코드로 AC를 받을 수 있다.
        s[:] = s[::-1]
