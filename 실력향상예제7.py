# 실력 향상 예제 7

data = [10, 6, 9, 8, 12]
total = 0

for i in range(0, 5): 
    total += data[i]
    print("%i일차 달린 거리: %2ikm" %(i+1, data[i]))
    
print("\n합계: %ikm, 평균: %ikm" %(total, total/5))
      

