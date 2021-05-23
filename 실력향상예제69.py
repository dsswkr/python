# 실력 향상 예제 69

import time
from time import localtime, strftime

while True:
  print(strftime("%H:%M:%S", localtime()))
  time.sleep(1)   # 1초 기다림


