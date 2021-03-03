"""
https://atcoder.jp/contests/abc189/tasks/abc189_c
"""

N = int(input())
A = list(map(int, input().split()))
ans = []
for i in range(len(A)):
    tmp_result = A[i]  # 初回のみ実行
    for j in range(i, len(A) - 1):
        if A[i] <= A[j + 1]:
            tmp_result += A[i]
        else:
            break

    ans.append(tmp_result)
print(ans)
print(max(ans))
