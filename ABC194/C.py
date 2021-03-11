N = int(input())
A = list(map(int, input().split()))
ans = 0

"""
通常の2重ループでは、時間切れ
for i in range(1, N):
    for j in range(1, i+1):
        ans += (A[i] - A[i - j])**2

ans = N*(A[N]*A[N] + A[N - 1]*A[N - 1]+....) -2*(全ての組み合わせ)
"""

for i in range(N):
    ans += (N - 1) * A[i] * A[i]

for i in range(N - 1):
    for j in range(i + 1, N):
        ans -= 2 * A[i] * A[j]

print(ans)
