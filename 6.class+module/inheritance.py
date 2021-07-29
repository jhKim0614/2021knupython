class Student:
  def __init__(self, name, age):
    self.name = name 
    self.age = age
  def __str__(self):
    return '안녕하세요 저는 {}이고, 학생입니다.'.format(self.name)
      
class Estudent(Student):
  def __str__(self):
    return '안녕하세요 저는 {}이고, 초등학생입니다.'.format(self.name)
  def print_age(self):
    print('{}의 나이는 {}살입니다.').format(self.name, self.age)

class Mstudent(Student):
  def __str__(self):
    return '안녕하세요 저는 {}이고, 중학생입니다.'.format(self.name) 

sasumi=Student('사스미', 4)
haedal=Estudent('해달이',1)
boogie=Mstudent('부기',5) 

print(sasumi)
print(haedal)
print(boogie)

haedal.print_age()
# sasumi.print_age()