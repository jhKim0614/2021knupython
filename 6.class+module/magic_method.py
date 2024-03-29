# 클래스-붕어빵 만들기
class FishBread:
    # 매소드 만들기
    # 붕어빵 굽기
    def __init__(self, ingredients, price):
        self.__ingredients = ingredients
        self.__price = price
    
    # 붕어빵 살펴보기
    def __str__(self):
        return '{}붕어빵, 가격 {}원'.format(self.__ingredients, self.__price)

    def __add__(self, other):
        return self.__price + other.__price

# 객체(인스턴스)-붕어빵 만들기
a = FishBread('팥',400)
b = FishBread('슈크림',500)

a.make_FB()
b.make_FB()

print(a)
print(b)

print('붕어빵 a,b 합쳐 %d원' % (a+b))