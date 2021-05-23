# 실력 향상 예제 46

num = []
phone = input("전화번호를 '-'를 포함하여 입력하세요.: ")

num = [phone[i] for i in range(len(phone)) if phone[i].isdigit()]

##for i in range(0, len(phone)):
##  if phone[i].isdigit():
##    num.append(phone[i])

print("숫자만 남긴 전화번호: %s" % ''.join(num))
