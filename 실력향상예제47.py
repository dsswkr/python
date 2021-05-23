# 실력 향상 예제 47

sum = 0
s1 = "3...1...4"
s2 = "1...9..2..2..1"

for i in range(len(s1)): 
  if s1[i].isdigit(): 
    sum += int(s1[i])
    
for i in range(len(s2)): 
  if s2[i].isdigit(): 
     sum += int(s2[i])

print("'%s' 문장과 '%s' 문장에 나오는 숫자 합 = %i" %(s1, s2, sum))
