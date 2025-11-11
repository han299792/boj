import sys 
data = sys.stdin.read().strip()

def A(data):
    digits_str = str(data)
    digits_int = list(map(int, digits_str))

    if sum(digits_int)%3 != 0:
        return "-1"
    if "0" not in digits_str:
        return "-1"
    
    digits_int.sort(reverse=True)
    para = ""
    for i in range(len(digits_int)):
        para += str(digits_int[i])
    return para
        
    
    
print(A(data))