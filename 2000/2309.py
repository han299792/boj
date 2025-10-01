import sys
data = sys.stdin.read().split()

heights = list(map(int, data))
total = sum(heights)
heights.sort()

found = False
for i in range(len(heights)):
    for j in range(i+1, len(heights)):
        if total - (heights[i] + heights[j]) == 100:
            a = heights[i]
            b = heights[j]
            found = True
            break
    if found:
        break

heights.remove(a)
heights.remove(b)

for h in heights:
    print(h)
