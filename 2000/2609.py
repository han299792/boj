import sys
data = sys.stdin.read().split()

a = int(data[0])
b = int(data[1])

x,y = a,b
while y!=0:
    x,y = y, x%y

result1 = x
result2 = a*b//result1

print(result1)
print(result2)

