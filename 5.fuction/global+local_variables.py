# 변수와 인수

# 전역변수와 지역변수의 차이를 알아보자

def add_two_num(a,b):
    print("덧셈중...")
    result = a + b
    return result # 지역변수 result

result = 0 # 전역변수 result
add_two_num(10, 13)
print(result)    