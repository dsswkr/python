# 실력 향상 예제 22

num = -1
num2 = 0;

while num < 10 or num > 99999999:
  num = int(input("2~8자리 양의 정수를 입력하세요: "))
		
while num > 0:
  num2 *= 10
  num2 += int(num % 10)
  num = int(num / 10)
	
print("뒤집힌 숫자: %i" %int(num2))


#문자열을 이용한 방법
#
#num = -1
#
#while num < 10 or num > 99999999:
#  num = int(input("2~8자리 양의 정수를 입력하세요: "))
#
#num2 = ''.join(reversed(str(num)))   # 문자열 뒤집기 reversed 함수 이용
#print("뒤집힌 숫자: %s" %num2)
