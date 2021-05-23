# 실력 향상 예제 33

money = 1000000.0	  # 원금 
interest = 0.05	          # 이자율 
years = 10.0	          # 기간 (년) 

# 받는 금액 계산
ret = money * pow(1.0 + interest, years)

print("%i원을 %i년 간 연%i%% 복리 저축 시 찾는 금액: %i원" %(int(money), int(years), int(interest*100), int(ret)))

