# 실력 향상 예제 13

def isNumber(s):
  try:
    float(s)
    return True
  except ValueError:
    return False

while True:
  num = input("정수 또는 실수를 입력하세요: ")
  if isNumber(num) == False:  # 입력 값을 숫자로 변환할 수 있는지 검사
    continue
  
  num = float(num)
  num2 = int(num)
  
  if -9999 == num2:
    break   
  elif num - num2 == 0.0:  # 소수점 이하 값이 없으면 정수로 인정  
    print("정수입니다.")
  else:
    print("실수입니다.")




  
