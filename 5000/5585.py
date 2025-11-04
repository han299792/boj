import sys

data = sys.stdin.read().split()
M = 1000 - int(data[0])

num = 0 
num += M//500
M = M%500
num += M//100
M = M%100
num += M//50
M = M%50
num += M//10
M = M%10
num += M//5
M = M%5
num += M//1
print(num)