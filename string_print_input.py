print("안녕하세요?")
name=input("이름을 입력하세요: ")

print("입력한 이름은 {s}입니다.".format(s=name)) # 방식 1
print("입력한 이름은 {}입니다.".format(name))    # 방식 2
print("입력한 이름은 %s입니다." %(name))         # 방식 3

