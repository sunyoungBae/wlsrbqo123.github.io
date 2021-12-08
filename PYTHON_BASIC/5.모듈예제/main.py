# 모듈 기본 사용법
"""
import calc

a = calc.add(1, 2)
print("add = %d" % a)

m = calc.mul(2, 3)
print("mul = %d" % m)
"""


# 모듈에서 사용할 함수를 직접 지정
"""
from calc import sub, div

s = sub(5, 4)
print("sub = %d" % s)

d = div(6, 3)
print("div = %d" % d)

# 지정되지 않은 함수 호출시 에러
#a = add(1, 2)
#print("add = %d" % a)
"""

# 모듈에서 모든 함수를 불러오기
"""
from calc import *

s = sub(5, 4)
print("sub = %d" % s)

d = div(6, 3)
print("div = %d" % d)

a = add(1, 2)
print("add = %d" % a)
"""