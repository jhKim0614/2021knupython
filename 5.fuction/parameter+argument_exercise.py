# 인수의 순서를 바꿔보기
def add_two_num(a,b): # 매개변수
    print("덧셈중...")
    print(a, b)
    result = a + b # 지역변수 result
    return result  # 함수 결과값

value = add_two_num(b=10, a=13) # 인수
print(value)  


# 매개변수에 기본값을 넣어주자
def add_two_num(a=100,b=200):
    print("덧셈중...")
    print(a, b)
    result = a + b
    return result

value1 = add_two_num(10,13)
value2 = add_two_num(10)
value3 = add_two_num(b=10)
value4 = add_two_num()
print(value1,value2,value3,value4)

# 가장 뒤의 변수부터 기본값 지정
def add_two_num(a=100, b): #불가능
    ...
def add_two_num(a, b=100): #가능    
    ...