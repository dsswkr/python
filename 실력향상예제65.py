# 실력 향상 예제 65

date1 = '2016/10/05'
date2 = '2016/07/05'
date3 = '2016/10/13'

def convert(date):
  d = date.split('/')
  return str(int(d[0]))+'년'+str(int(d[1]))+'월'+str(int(d[2]))+'일'
  
print(date1 + ' --> ' + convert(date1) + '\n')
print(date2 + ' --> ' + convert(date2) + '\n')
print(date3 + ' --> ' + convert(date3) + '\n')
