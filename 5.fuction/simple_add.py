# 간단한 덧셈 함수
def add_two_num(a,b):
    print("덧셈중...")
    result = a + b # 지역변수 result
    return result  # 함수 결과값
    # return 5

# 전역변수 value
value = add_two_num(10, 13)
print(value)    