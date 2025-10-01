import sys
input = sys.stdin.readline

count = int(input().strip())
data = input().strip()
divisors = list(map(int, data.split()))

divisors.sort()
result = divisors[0]*divisors[-1]
print(result)