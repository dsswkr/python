# 실력 향상 예제 27

TIME = 9         # 하루에 공부한 시간
YEARS = 35       # 공부한 햇수 
LEAP_YEARS = 8   # 윤년 횟수

total = (TIME * YEARS * 365) + (TIME * LEAP_YEARS)
# total = TIME * (YEARS * 365 + LEAP_YEARS) 

print("하루 9시간씩 35년(윤년 8회) 공부한 시간: %i 시간" % total)
