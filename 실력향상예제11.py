# 실력 향상 예제 11

total = 0

for i in range(1, 11):
    print("%2i의 4승 = %5i" %(i, pow(i, 4)))
    total += pow(i, 4)   #total += i**4

print("\n전체 합계 = %i" % total)

    
