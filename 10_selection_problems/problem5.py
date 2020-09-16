N, A, B = list(map(int, input().split()))
tot = 0

for i in range(N):
    s = str(i+1)

    ll = list(map(int, s))
    ans = sum(ll)

    if A <= ans <= B :
        tot += i+1

print(tot)

