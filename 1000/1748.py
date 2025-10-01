import sys
data = sys.stdin.read().split()
data = int(data[0])
cnt = 0 
for i in range(len(str(data)), 0, -1):
    if data > 0 :
        para = data - 10**(i-1) + 1
        cnt += para*i
        data -= para
      
print(cnt)
    