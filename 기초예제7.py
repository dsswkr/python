# 기초 예제 7

name = input("이름을 입력하세요: ")
n = name.strip()

if(n != ""): 
  print("입력한 이름은 %s입니다." %n)
else: 
  print("입력한 이름이 없습니다.")


