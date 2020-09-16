N = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
#b = sum([j if i%2 == 0 else -j for i, j in(enumerate(a))])
b = sum(a[0::2]) - sum(a[1::2])
print(b)

