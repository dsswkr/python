# 고급 예제 4

menu = "1. 전체이름 보기\n2. 성만 보기\n3.”이름만 보기\n4. 끝내기\n메뉴 번호를 선택하세요(1~4): "
names = ["홍길동", "이동묵", "원종호", "최종현" ]
count = len(names)

while True:
  n = int(input("\n%s" %menu))
  if n == 4:
    break
  if n == 1:
    print("\n[전체 이름 목록]")
    for i in range(count):
      print(names[i])
  elif n == 2:
    print("\n[성만 보기]")
    for i in range(count): 
      print(names[i][0])
  elif n == 3: 
    print("\n[이름만 보기]");
    for i in range(count): 
      print(names[i][1:])
  else:
    print("메뉴 번호를 정확하게 선택하세요.") 



