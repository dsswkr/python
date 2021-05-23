# 실력 향상 예제 70

import time

dw = ['월', '화', '수', '목', '금', '토', '일']
t = time.localtime()

print("%s년 %s월 %s일, %s요일" %(t.tm_year, t.tm_mon, t.tm_mday, dw[t.tm_wday]))

#tm_wday 값은 0이 월요일입니다.
