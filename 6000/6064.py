import sys
data = sys.stdin.read().split()

nums = list(map(int, data))

for i in range(1, nums[0]*4, 4):
    for j in range (0, nums[i]*nums[i+1], nums[i]):
        if (j + nums[i+2] - nums[i+3]) % nums[i+1] == 0 :
            print(j + nums[i+2])
            break
    else: 
        print("-1")
        