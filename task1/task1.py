import sys

n = int(sys.argv[1])
m = int(sys.argv[2]) - 1

res = "1"
x = m % n 
while x != 0:
    res += str(x + 1)
    x = (x + m) % n
print(res)
