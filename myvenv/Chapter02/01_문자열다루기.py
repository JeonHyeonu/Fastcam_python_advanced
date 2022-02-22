# 1. replace
# 문자열 교체
x = '오늘 날씨는 흐림입니다.'.replace("흐림", "맑음")

print(x)

# 2. find
# 문자열 찾기
y = 'Hello world'.find('world') # 문자열을 찾아서 첫번째 index 값을 가져옴
print(y)

# 3. split
# 문자열 분리
# 구분되는 문자 또는 공백을 기준으로 나눔
z = '나이키신발 265 X1212 78000'.split() 
print(z)
a = '나이키신발:265:X1212:78000'.split(':')
print(a)

# 4. strip
# 문자열 공백 제거
b = '   Yeah    '.lstrip()
print(b)
c = '   Yeah    '.rstrip()
print(c)
d = '   Yeah    '.strip()
print(d)