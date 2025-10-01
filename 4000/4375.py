import sys
data = sys.stdin.read().split()

def get_digit(n):
    return len(str(n))

for x in data:
  x = int(x)
  rem = 1%x
  cnt = 1
  while rem != 0:
      rem = (rem*10 + 1)%x
      cnt += 1
  print(cnt)
        