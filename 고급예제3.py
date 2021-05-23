# 고급 예제 3

RED = 5
BLUE = 3
YELLOW = 1
FAIL = -1  
TOTAL = 10
message = "번 기회에서 빨간 풍선을 맞춘 숫자를 입력하세요(0~10): "

while True:
  red = int(input("\n%i%s" %(TOTAL, message)))
  if red >= 0 and red <= TOTAL:
    break
  
sum = red

if (red < TOTAL):
  while True:
    blue = int(input("\n%i%s" %(TOTAL - red, message)))
    if blue >= 0 and blue <= (TOTAL-sum):
      break
else:
  blue = 0

sum += blue

if (blue < (TOTAL-red)):
  while True:
    yello = int(input("\n%i%s" %(TOTAL-sum, message)))   
    if yello >= 0 and yello <= TOTAL - sum:
      break
    else:
      yello = 0

sum += yello
fail = TOTAL - sum

print("\n------------------------------------------------------------------------");
print("R(5점):%i회, B(3점):%i회, Y(1점):%i회, F(-1점):%i회" %(red, blue, yello, fail))
print("------------------------------------------------------------------------");
print("결과 점수 = %i" %(red*RED + blue*BLUE + yello*YELLOW + fail*FAIL))
print("------------------------------------------------------------------------");

