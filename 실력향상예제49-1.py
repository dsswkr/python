# 실력 향상 예제 49-1

names = set()

for i in range(10):
  name = input("이름을 입력하세요: (종료: <엔터>)")
  if name == "":
    print("종료합니다.")
    break
  if (name in names):
    print("같은 이름이 이미 존재합니다.")
  else:
    names.add(name)


