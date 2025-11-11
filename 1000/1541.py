import sys

data = sys.stdin.readline().strip() 

A = []
B = []

para = "" 

for char in data:
    if char.isdigit():
        para += char
    else:
        A.append(int(para)) 
        B.append(char)
        para = ""
A.append(int(para))
i = 0 
while i < len(B):
    if B[i] == '+':
        a = A.pop(i+1)
        A[i] = A[i] + a
        B.pop(i)
    else:
        i += 1
ans = A[0]       
for i in range(1, len(A)):
    ans -= A[i]
print(ans)
