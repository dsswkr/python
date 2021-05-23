# 실력 향상 예제 38

year = 1582

while (year < 1583 or year > 9999):
  year = int(input("윤년인지 확인할 연도를 네 자리로 입력하세요(1583~9999): "))

is_leap_year = ((not(year % 400)) or ((not(year % 4)) and (year % 100)))

print("%i년은 %s입니다." %(year, is_leap_year and "윤년" or "평년"))

