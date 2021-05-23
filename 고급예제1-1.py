# 고급 예제 1-1

import calendar
    
while (1):
  y = int(input("달력의 연도를 입력하세요(1583~9999): "))
  m = int(input("달력의 월을 입력하세요(1~12): "))    
  calendar.prmonth(y, m)   # 지정된 월의 달력을 출력
  calendar.prcal(y)        # 해당 연도 달력을 모두 출력
  



