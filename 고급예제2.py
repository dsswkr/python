# 고급 예제 2

# 데이터를 튜플에 저장 
s = ("In the clear morning, I transplant a tree from the yard to a forest.", 
  "I am writing a letter with dew drops in selected, treasured words,", 
  "wiping my hands with an apron, the deep mind concentrated.", 
  "As a river cannot fill the sea even if it reached there, so is my thought.", 
  "Long accumulated times form dew in the eye, drop by drop.", 
  "It feels like yesterday when I innocently sown seed; yet it has been", 
  "twenty - eight years for its budding and growing in all seasons.", 
  "It grew with branches and flowers to be a pride and joy of the garden;", 
  "it endured the scorching summer and severe cold winter every year.", 
  "When the tree stands in the forest, it may get weary, but I move it", 
  "with a joyful heart. I know how all other trees were like, for I believe", 
  "in the big hands that raised them, blocking the storm, covering the frost.", 
  "The hands convince me of their protection, flowering, and fruitfulness.", 
  "I can see two trees standing side by side on one hill, blooming fruitfully.", 
  "As singing flowers bloom and the sound of bells ring,", 
  "I pray for plentiful bearing of fruits.", 
  "Let us all stand as majestic trees every time in the eyes of love.")

a = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

data = { }            # 문자 횟수를 저장할 사전

def push_ch(c):
  if c.isalpha(): 
    if c in data:     # 이전에 저장된 문자 또는 숫자면 횟수를 증가함
      data[c] += 1
    else:  	      # 새로운 문자 또는 숫자면 추가하고 1로 초기화 
      data[c] = 1

#--------------------------------------------------------------
# 메인 처리 

for i in range(len(s)):
  for c in range(len(s[i])):
    push_ch(s[i][c])

for i in range(len(a)): 
  if a[i] in data:
    print(a[i] + ":" + str(data[a[i]]))






