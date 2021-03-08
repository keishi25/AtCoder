"""
問題リンク
https://atcoder.jp/contests/keyence2020/tasks/keyence2020_b

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

ans = 1
# 重なりがないところを貪欲に探索
for i in range(len(start_end_list) - 1):
    start_before = start_end_list[i][0]
    end_before = start_end_list[i][1]
    start_after = start_end_list[i + 1][0]
    end_after = start_end_list[i + 1][1]

    if end_before < start_after:
        ans += 1

print(ans)