# 실력 향상 예제 71-1

import math

MAX = 1000
n = 1

with open("피타고라스수.txt", "w") as f:  # 파일 열기
  for a in range(3, MAX, 2):   		  # a는 3보다 큰 홀수   
    aa = a*a
    for c in range(a+2, MAX+1, 2):	  # c는 a보다 큰 홀수 
      cc = c*c
      for b in range(2, MAX, 2):     	  # b는 c보다 작은 짝수면서
        if b < c and cc == aa + b*b: 	  # 피타고라스 숫자면 
          print("A = %3i, B = %3i, C = %3i" %(a, b, c))   # 화면 출력 
          f.write("[%4i] a = %3i, b = %3i, c = %3i\n" %(n, a, b, c)) # 파일 저장
          n +=  1

