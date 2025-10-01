import sys
input = sys.stdin.read().split()

T = int(input[0])
nums = list(map(int, input[1:]))

def g(n: int) -> int:
    res = 0
    i = 1
    while i <= n:
        q = n // i
        j = n // q
        res += q * (i + j) * (j - i + 1) // 2
        i = j + 1
    return res

out = []
for num in nums:
    out.append(str(g(num)))

sys.stdout.write("\n".join(out))
