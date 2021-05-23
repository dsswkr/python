# 실력 향상 예제 43

my_money = 110000
days = 0

while (my_money >= 0):   # 돈이 남아 있으면... 
  my_money -= 3000 if (days % 7) != 0 and days > 0 else 6000
  days += 1

##while (my_money >= 0):   # 돈이 남아 있으면... 
##  if ((days % 7) != 0 and days > 0):   # 7일차가 아니면... 
##          my_money -= 3000
##  else:
##          my_money -= 6000
##  days += 1

print("용돈을 %i일까지 사용할 수 있습니다." %days)
        
