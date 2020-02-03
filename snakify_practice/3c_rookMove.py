# This program takes the coordinates of a rook and a destination and determines whether it is possible for it to move:
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if x1 == x2 or y1 == y2:
    print ("YES")
else:
    print ("NO")
