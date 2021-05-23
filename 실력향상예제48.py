# 실력 향상 예제 48

while True:
  num1 = int(input("사칙연산에 사용할 처음 정수를 입력하세요: "))
  op = input("사칙연산 번호 1~4를 입력하세요(1:'+', 2:'-', 3:'/', 4:'*'): ")
  num2 = int(input("사칙연산에 사용할 다음 정수를 입력하세요: "))
  if op == '1' or op == '+':
    print("%i + %i = %i" %(num1, num2, num1+num2))
  elif op == '2' or op == '-':
    print("%i - %i = %i" %(num1, num2, num1-num2))
  elif op == '3' or op == '/':
    if num2 == 0:
      print("[에러!] 0으로 나눌 수 없습니다.")
    else:
      print("%i / %i = %i" %(num1, num2, num1/num2))           
  elif op == '4' or op == '*':
    print("%i x %i = %i" %(num1, num2, num1*num2))
  else:  
    print("[에러!] 사칙 연산자는 1~4 숫자나 부호로 선택하세요.")


