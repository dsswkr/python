# 실력 향상 예제 32

PI = 3.141592
volume = 1000.0

# 구의 체적 = 4 * PI * r * r * r / 3   
radius = pow(volume * 3.0 / 4.0 / PI, 1.0/3.0)

print("구의 반지름은 약 %.2fcm입니다." % radius)
