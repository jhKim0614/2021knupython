# for문 활용한 파일 출력(쓰기)
f = open('haedal_for.txt', 'w')

for i in range(100):
  f.write(f"Hello Haedal! {i}\n")

print("쓰기 종료")

f.close()