# 실력 향상 예제 58-1
import random

nums = [i for i in range(100)]
random.shuffle(nums)

print("현재 리스트 항목")
print(nums)

for i in range(1, len(nums)):
  for j in range(0, len(nums)-1): 
    if nums[i] < nums[j]: 
      nums[i], nums[j] = nums[j], nums[i]

print("\n오름차순 정렬된 리스트 항목")
print(nums)

       
