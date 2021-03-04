"""
例題 1
みかん（100円）りんご（200円）ぶどう（300円）がそれぞれ1つずつ果物屋さんにありました。
財布の中には300円ありますが、考え得るすべての買い物パターンを列挙しなさい。

bit全探索を使用する
2進数表記にしたときに、1のフラグが立っているかどうか確認する
確認方法は、bit演算で1と同じ（＆）か確認する
"""
fruits = [[100, "みかん"], [200, "りんご"], [300, "ぶどう"]]
total_num = 2**3
ans = []

for num in range(1, total_num):   # 何も買わないケースの排除
    tmp_money = 0
    tmp_fruits_list = []
    for i in range(len(bin(num)) - 2):  # 2進数表記のobを削除
        if (num >> i) & 1:
            tmp_money += fruits[i][0]
            tmp_fruits_list.append(fruits[i][1])

    tmp_fruits_list.append(tmp_money)  # 最終金額をフルーツのリストに追加
    if tmp_money <= 300:
        ans.append(tmp_fruits_list)

print(ans)