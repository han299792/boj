import sys

T = int(input())

for _ in range(T):
    C = int(input())
    a1 = C//25
    b1 = C%25
    a2 = b1//10
    b2 = b1%10
    a3 = b2//5
    b3 = b2%5
    a4 = b3
    print(a1, a2, a3, a4)