import sys
input = sys.stdin.readline

data = input()

a, b, c = map(int, data)
print((a+b)%c)
print((a%c+b%c)%c)
print((a*b)%c)
print(((a%c)*(b%c))%c)