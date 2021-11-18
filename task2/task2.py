import sys

FileCircle = sys.argv[1]
FilePoints = sys.argv[2]

FileCircle = open(FileCircle, 'r')
x0, y0 = [float(i) for i in FileCircle.readline().split()]
r = float(FileCircle.readline())

FilePoints = open(FilePoints, 'r')

for point in FilePoints.readlines():
    xn, yn = [float(i) for i in point.split()]
    distance = ((xn-x0)**2 + (yn-y0)**2)**(1/2) - r
    if distance == 0:
        print(0)
    if distance < 0:
        print(1)
    if distance > 0:
        print(2)
    
