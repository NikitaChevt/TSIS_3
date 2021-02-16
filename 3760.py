a = int(input())
d = {}
for i in range(a):
    first, second = input().split()
    d[second] = first
    d[first] = second

print(d[input()])