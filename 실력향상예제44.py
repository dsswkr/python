# 실력 향상 예제 44

data = [1, 2, 5, 2, 4, 5, 1, 5, 5, 3, 3, 1]

for i in range(1, 6):
  count = 0
  for j in range(len(data)): 
    if (i == data[j]):
      count += 1
  print("%i:%i " %(i, count))


