# 실력 향상 예제 51

while True:
  dan = int(input("구구단의 단을 입력하세요(2~9; 0=종료): "))

  if dan == 0: break
  if dan < 2 or dan > 9: continue

  print("\n[%i단]" % dan)
  for i in range(1, 10):
    print("%i x %i = %2i" %(dan, i, dan*i))
  print("");

print("종료합니다.")
