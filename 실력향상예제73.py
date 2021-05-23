# 실력 향상 예제 73

NUMBER = 258          # 변경할 10진수 숫자 지정 
MAX_OCTAL_LEN = 100   # 8진수 최대 한계 자릿수 지정

n = NUMBER
octal = []            # 8진수 값을 저장할 빈 리스트 생성

for i in range(MAX_OCTAL_LEN - 1):
  if n <= 7:
    break
  octal.insert(0, str(int(n % 8)))  # 리스트 앞쪽에 추가
  n /= 8;

octal.insert(0, str(int(n)))        # 남은 자리 값을 추가 

# 리스트를 문자열로 변환하여 출력
print("10진수 %i의 8진수 = %s" %(NUMBER, ''.join(octal)))
