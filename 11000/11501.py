import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    prices = list(map(int, input().split()))
    
    max_sell = 0
    profit = 0
    
    for p in reversed(prices):
        if p > max_sell:
            max_sell = p
        else:
            profit += max_sell - p
    print(profit)
# 최대다? 뒤에서부터 하면 어떨까 생각해보기


# import sys
# input = sys.stdin.readline

# T = int(input())

# for i in range(T):
#     N = int(input())

#     nums = list(map(int, input().split()))
#     value = 0 
    
#     while len(nums) > 1:
#         max_val = max(nums)
#         max_idx = nums.index(max_val)
        
#         if max_idx == 0:
#             nums = nums[1:]
#             continue
#         for j in range(max_idx):
#             value += max_val - nums[j] 
#         if max_idx == len(nums)-1:
#             break
#         else:
#             nums = nums[max_idx+1:]
    
#     print(value)
                

        