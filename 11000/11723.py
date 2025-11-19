import sys
s1 = set()
data = sys.stdin.read().split()
N = int(data[0])

for i in range(N):
    func = data[1+2*i]
    
    if func not in ["all", "empty"]:
        x = int(data[2+2*i])

    if func == "add":
        s1.add(x)
    elif func == "remove":
        s1.remove(x)
    elif func == "check":
        if x in s1:
            print("1")
        else:
            print("0")
    elif func == "toggle":
        if x in s1:
            s1.remove(x)
        else:
            s1.add(x)
    elif func =="all":
        s1 = set(range(1, 21))
    elif func == "empty":
        s1.clear()