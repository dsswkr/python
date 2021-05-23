# 두 값을 교환하여 돌려주는 swap 함수

x = 100
y = 200

def swap(a, b):
  return b, a
#----------------------

print(x)
print(y)

x, y = swap(x, y)

print(x)
print(y)
