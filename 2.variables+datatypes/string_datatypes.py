#기본문자열
s2 = 'Hello, Haedal!'
print(s2)
S2 = 'Hello, Headal!'
print(S2)

#이스케이프 코드
# \n, \t, \\, \', \"
longtext1 = """Hello, Headla!
My name is Haedal Prongraming."""
print(longtext1)
longtext2 = 'Hello, Headla! \n My name is Haedal Prongraming.'
print(longtext2)

#String Interpolation
a = 123
new_q = f'{a}'
print(new_q)

# 문자열 옛날 방식
print(f'%s %s' % ('one', 'two'))

#pyformat
print('{} {}'. format('one', 'two'))

# f-string 
a, b = 'one', 'two'
print(f'{a} {b}')

#exaple
name = "해달"
eng_name = "Headal"
print("안녕하세요. {1}입니다. My name is {0}".format(eng_name, name))
print(f'안녕하세요. {name}입니다')

# 문자열 인덱싱
a = "Hello, Haedal!"
print(a[1])

#문자열 슬라이싱
a = "Hello, Haedal!"
print(a[4:9])

# 문자열의 길이를 구하는 len()
print(len(a))

# 문자열의 최대, 최소를 구하는 max(), min()
# 아스키코드 -> 
a = '312'
b = 'bac'
print(min(a))
print(max(a))
print(min(b))
print(max(b))
print(a+b)
print(min(a+b))
print(max(a+b))

# 소문자, 대문자로 변화해주는 lower() , upper()
a = 'This is Apple'
print(a.lower())
print(a.upper())

#문자열을 구분자에 따라 나누는 split()
a = "안녕, 나는, 해달이야"
print(a.split(sep=','))
b = "안녕 나는 해달이야"
print(b.split( ))

#여러개의 문자열 사이에 구분자를 넣어주는 join()
mylist = ['안녕', '나는', '해달']
mystring = '_'.join(mylist)
print(mystring)