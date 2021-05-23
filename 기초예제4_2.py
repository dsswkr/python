# 기초 예제 4-2

# 문자열이 정수로 바뀔 수 있는지 검사하는 함수
def isNumStr(s):
  try:
    int(s)
    return True
  except ValueError:
    return False

# 정수를 입력받아서 처리
num1 = input("정수 숫자를 입력하세요: ")
num2 = input("다음 정수를 입력하세요: ")

if isNumStr(num1) and isNumStr(num2):
  print(int(num1) - int(num2))
else:
  print("정수가 아닌 것이 포함되어 있습니다.")



