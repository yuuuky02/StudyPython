print("hello world")

# 3. 자료형
print(3)
print(3.14)
print("큰 따옴표")
print('작은 따옴표')

# 4. 변수
a = 100
b = '변수'
print(str(a) + b)

# 5. 변수 이름
# 문자 또는 _로 시작 / 문자, 숫자, _로 구성 / 공백 X, 특수문자 X / 대소문자 구분 / 키워드 (예약어) X 
# / 소문자 단어, _로 구분된 단어들(권장)
# ex) name, _name / name123, _name_456 / na me(x), $_name_^^(x) / name, Name, NAME / True, False, for, ...

# 6. 형 변환
# int()정수로, float()실수로, str()문자로

# 7. 연산자
# +, - , *, /
#  % 나머지, // 몫, ** 거듭제곱
# 비교 연산자 
# >, >=, <, <=, ==, !=
# 논리 연산자
# and, or, not
print(not 3<5) # False
# 멤버 연산자
# in, not in
print('c' in 'cat') # True
print('c' not in 'cat') # False

# 8. 불리안
# bool()
print(bool('hello')) # True, 값이 있음
print(bool('     ')) # True, 값이 있음
print(bool('')) # False, 값이 없음
print(bool(3)) # True, 0이 아닌 수 값이 있음
print(bool((0))) # False, 값이 없음
print(bool(None)) # False, 값이 없음
print(bool('False')) # True, 빈 문자열이 아닌 값이 있음

# 9. 주석
# 한 줄 주석
'''
여러 줄 주석
'''

# 10. 인덱스와 슬라이싱
# 0부터 시작
lang = 'PYTHON'
print(lang[0]) # P, 0은 앞에서부터
print(lang[-1]) # N, -1은 뒤에서부터
print(lang[1:]) # YTHON, 1부터 끝까지
print(lang[:]) # PYTHON, 전체
print(lang[2:5]) # THO, 2부터 5미만

# 11. 문자열 처리
num = 3
num += 2
print(num)
print(len('snacks'))

# 12. 문자열 메소드
# 문자열.메소드(...)
letter = 'how are YOU'
print(letter.lower())
print(letter.upper())
print(letter.capitalize()) # 첫 글자만 대문자로, How are you
print(letter.title()) # 각 단어들의 첫 글자만 대문자로, How Are You
print(letter.swapcase()) # 대소문자 뒤바꾸기,
print(letter.split()) # 문자열 나누기,
print(letter.count('how')) # 1, how가 얼마나 쓰였는지
