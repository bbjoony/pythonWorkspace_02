#chapter03_01
#숫자형

#파이썬 지원 자료형
"""
    int : 정수
    float: 실수
    complex : 복소수
    bool : 불린
    str : 문자형(시퀀스)
    list : 리스트(시퀀스)
    tuple : 튜플(시퀀스)
    set : 집합
    dict : 사전
"""
# 데이터 타입
str1 = "Python"
bool = True
str2 = 'Anaconda'
float = 10.0
int = 7
list  = [str1, str2]
dict = {
    "name": "Machine learning",
    "version" : 2.0    
}
tuple = (7, 8, 9)
set = {3, 6, 9}

#데이터 타입 출력
print(type(str1))
print(type(bool))
print(type(str2))
print(type(float))
print(type(int))
print(type(list))
print(type(dict))
print(type(tuple))
print(type(set))

#숫자형 연산자
"""
+
-
*
/
// :  몫
% : 나머지
abs(x) : 절대값
pow(x, y) : x**y -> 2**3
"""

#정수 선언
i = 77
i2 = -14
big_int = 77777777777777999999999999999

#정수 출력
print(i)
print(i2)
print(big_int)
print()

#실수 출력
f = 0.99999
f2 = 3.141592
f3 = -3.9
f4 = 3/9

print(f)
print(f2)
print(f3)
print(f4)
print()

#연산 실습
i1 = 39
i2 = 939
big_int1 = 1231498997891274791823
big_int2 = 898718963786968219819279123819
f1 = 1.234
f2 = 3.123

#+
print(">>>>>> +")
print("i1 + i2 : ", i1 + i2)
print("f1 + f2 : ", f1 + f2)
print("big_int1 + big_int2 : ", big_int1 + big_int2)
print()

#*
print(">>>>>> *")
print("i1 * i2 : ", i1 * i2)
print("f1 * f2 : ", f1 * f2)
print("big_int1 * big_int2 : ", big_int1 * big_int2)




