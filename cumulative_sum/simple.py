"""
https://atcoder.jp/contests/abc122/tasks/abc122_c
累積和を使用することで、計算回数を減らす
"""

N, Q = list(map(int, input().split()))
S = input()
accum_list = [0]

for i in range(len(S) - 1):
    if S[i] == "A" and S[i + 1] == "C":
        accum_list.append(1 + accum_list[i])
    else:
        accum_list.append(accum_list[i])


for i in range(Q):
  l, r = list(map(int, input().split()))
  print(accum_list[r - 1] - accum_list[l - 1])





