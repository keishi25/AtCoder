"""
問題リンク
https://atcoder.jp/contests/keyence2020/tasks/keyence2020_b

解説リンク
https://nashidos.hatenablog.com/entry/2020/01/19/120045

方針
リストに始点と終点を格納し、終点でソート
小さい順に、範囲が重なりがないところをカウントアップしていく

"""

N = int(input())
start_end_list = []
for i in range(N):
    x, l = list(map(int, input().split()))
    # 始点と終点を格納
    start_end_list.append([x - l, x + l])

# 終点でソート
start_end_list = sorted(start_end_list, key=lambda x: x[1])

ans = N

# 重なりが発生している箇所を間引く
for i in range(len(start_end_list) - 1):

    if start_end_list[i][1] > start_end_list[i + 1][0]:
        # 重なりがある場合、間引く処理を行うため、座標の書き換えを行っている
        start_end_list[i + 1][1] = start_end_list[i][1]
        ans -= 1

print(ans)
