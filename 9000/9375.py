import sys

def solve():
    input_data = sys.stdin.read().split()
    
    iterator = iter(input_data)

    T = int(next(iterator))
    
    for _ in range(T):
        n = int(next(iterator))
        
        clothes = {}
        
        for _ in range(n):
            next(iterator) 
            category = next(iterator)
            
            if category in clothes:
                clothes[category] += 1
            else:
                clothes[category] = 1
        
        result = 1
        for count in clothes.values():
            result *= (count + 1)
        
        print(result - 1)

if __name__ == '__main__':
    solve()