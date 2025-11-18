import sys 
data = sys.stdin.read().split()

nums = list(map(int, data[1:]))

fb = [1]*40
for i in range(2, 40):
	fb[i] = fb[i-1] + fb[i-2]

for j in range(int(data[0])):
    if nums[j] == 0:
        print("1 0")
    elif nums[j] == 1:
        print("0 1")
    else:
        a = nums[j]
        print(fb[a -2] + " " + fb[a-1])


