# 리스트 할당 방식

x = [1,2,3,4,5]
y = x

y[2] = 0

"""
Y에 X 리스트값을 할당 (복사형식)해서 사용하려고 했는데,
y 인덱스값 2에 해당하는 값인 "3" 을 "0" 으로 바꿨더니
x, y 리스트 모두가 변함. 이는 x와 y가 같은 리스트값을 받아 사용했기 때문
"""

print(x)
print(y)
print(id(x))
print(id(y))

"""
이를 해결하기 위해서는 copy() 코드를 사용해야함
ex) y = x.copy()
"""

# 리스트 복사 방식
a = [5,6,7,8,9]
b = a.copy()

b[2] = 0
print(a)
print(b)
print(id(a))
print(id(b))



# 중첩 리스트 복사 방식
"""
다차원 리스트는 copy 모듈에서 deepcopy 를 사용해 복사해야함
ex) y = copy.deepcopy(x)
"""
import copy

c = [[1,2], [3,4,5]]
d = copy.deepcopy(c)
d[0][0] = 0
print(c)
print(d)

