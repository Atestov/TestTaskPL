import sys

file = open(sys.argv[1], 'r')
s = [int(i) for i in file.readlines()]
average = round(sum(s)/len(s))
print(sum(abs(i-average) for i in s))
