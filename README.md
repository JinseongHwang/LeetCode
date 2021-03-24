# LeetCode

## 학습 목적 및 기대하는 바

- 영어 독해 실력 향상.
- Python 언어에 대한 이해, 익숙해짐.
- 향후 데이터 처리, 인공지능 관련 기능 개발 시 바로 투입 가능하게 함.



<br>



## 참고 자료

- [LeetCode](https://leetcode.com/)
- [파이썬 코딩도장](https://dojang.io/course/view.php?id=7)
- [파이썬 알고리즘 인터뷰, 박상길 저, 책만, 2020](http://www.kyobobook.co.kr/product/detailViewKor.laf?mallGb=KOR&ejkGb=KOR&barcode=9791189909178)



<br>



## 알게된 내용 정리

### 분할 상환 분석과 동적 배열(예정)

동적 배열에 대한 분할 상환 분석을 진행한다.   
또한 동적 배열을 resizing하는 비율, Growth Factor에 대해 학습 후 블로그에 포스팅한다.   
ex) C++: std::vector, Java: ArrayList, Python: list   

### 빠른 입력
```python
import sys
input = sys.stdin.readline
```
위와 같이 작성한 후 input() 그대로 사용하면 보다 빠르게 입력을 받을 수 있다.

### 문자열 슬라이싱
- 문자열을 다루는 Python 내장 기능이다. 매우 훌륭한 성능을 가진다. 따라서 가능하다면 문자열 처리는 문자열 슬라이싱 방법으로 처리하는 습관을 가지자.    

|  0   |  1   |  2   |  3   |  4   |
| :--: | :--: | :--: | :--: | :--: |
|  안  |  녕  |  하  |  세  |  요  |
|  -5  |  -4  |  -3  |  -2  |  -1  |

- `S[1:4]` : 인덱스 1 이상 4 전까지 (1 ~ 3)
- `S[1:-2]` : 인덱스 1 이상 -2 전까지 (1 ~ 2)
- `S[1:]` : 인덱스 1 부터 끝까지 (1 ~ 4)
- `S[:]` : 문자열의 사본 (0 ~ 4)
- `S[1:100]` : 끝이 초과한다면 있는 최대길이만큼 (1 ~ 4)
- `S[-1]` : 끝에서 1번째 (4)
- `S[-4]` : 끝에서 4번째 (1)
- `S[:-3]` : 처음부터 끝에서 3번째 문자 전까지 (0 ~ 1)
- `S[-3:]` : 끝에서 3번째 문자부터 끝까지 (2 ~ 4)
- `S[::1]` : 문자열의 사본 (0 ~ 4)
- `S[::-1]` : 뒤집은 문자열 (4 ~ 0)

### 람다식

```python
s = ['2 A', '1 B', '4 C', '1 A']

sorted(s)
>>> ['1 A', '1 B', '2 A', '4 C']

def func(x):
    return x.split()[1], x.split()[0]
s.sort(key=func)
>>> ['1 A', '2 A', ' 1 B', '4 C']

s.sort(key=lambda x: (x.split()[1], x.split()[0]))
>>> ['1 A', '2 A', ' 1 B', '4 C']
```

### 자료구조

```python
# 기본 key값이 존재하지 않더라도 삽입 시에 키를 생성해줌
from collections import defaultdict

# 숫자를 저장할 수 있는 딕셔너리 - default value: 0
numberDict = defaultdict(int)
numberDict = defaultdict(lambda : 0)

# list를 저장할 수 있는 딕셔너리 - default value: []
listDict = defaultdict(list)

# set을 저장할 수 있는 딕셔너리 - default value: empty set
setDict = defaultdict(set)
```

### 정렬

```python
a = [2, 5, 1, 9, 7]
sorted(a) # 정렬된 결과를 반환한다.
>>> [1, 2, 5, 7, 9]
a # 하지만 원본 List는 정렬되지 않는다.
>>> [2, 5, 1, 9, 7]

a = 'zbdaf'
sorted(a) # 각 문자로 분할 후 정렬된 List를 반환한다.
>>> ['a', 'b', 'd', 'f', 'z']
''.join(sorted(a)) # List형태를 빈 문자로 join하면 문자열로 만들 수 있다.
>>> 'abdfz'

a = [4, 1, 3, 2, 3]
a.sort() # sort()는 원본 List 자체를 정렬하고, None을 반환한다. 대입하지말자.
>>> [1, 2, 3, 3, 4]

a = ['cde', 'cfc', 'abc', 'a', 'cdef']
sorted(a)
>>> ['a', 'abc', 'cde', 'cdef', 'cfc']
sorted(a, key=len) # 문자열 길이로 정렬
>>> ['a', 'cde', 'cfc', 'abc', 'cdef']

def fn(s):
    return s[0], s[-1]
sorted(a, key=fn) # 첫 문자 또는 마지막 문자로 정렬
>>> ['a', 'abc', 'cfc', 'cde', 'cdef']

# 람다식으로 간소화
sorted(a, key=lambda s: (s[0], s[-1]))
>>> ['a', 'abc', 'cfc', 'cde', 'cdef']
```