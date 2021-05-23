# 실력 향상 예제 66

length = 0

while length < 3:
  name = input("\n당신의 이름을 입력하세요(세 글자 이상): ")
  length = len(name)

name = name[:length - 1] + '*'	

print("당신의 이름은(끝 글자는 * 대체): %s\n" %name)

	
