# 숫자인지 검사하기

# 숫자인지 검사 
def isNumber(s):
  try:
    float(s)
    return True
  except ValueError:
    return False

#정수인지 검사
def isInt(s):
  try:
    int(s)
    return True
  except ValueError:
    return False

# 테스트 예제
print(isNumber('10'))
print(isNumber(10))
print(isNumber('abc'))
print('----------------------')
print(isInt('10'))
print(isInt(10))
print(isInt('10.10'))
print(isInt('abc'))
