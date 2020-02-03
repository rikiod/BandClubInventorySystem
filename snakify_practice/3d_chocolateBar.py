# This program determines if a chocolate bar with dimensions n by m would be able to be divided into a bar with k squares.
n = float(input())
m = float(input())
k = float(input())
portion = n * m

if k < portion and ((k % n == 0) or (k % m == 0)):
    print("YES")
else:
    print("NO")