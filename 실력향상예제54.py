# 실력 향상 예제 54

PI = 3.141592
diameter=0

while diameter <= 0: 
  diameter = int(input("표면적을 구할 구의 지름을 입력하시오: "))

serface_area = 4.0 * PI * (diameter / 2) * (diameter / 2)
print("지름이 %.1f인 구의 표면적 = %.3f" %(diameter, serface_area))
