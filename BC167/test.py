"""
解法
→bit全探索
対象
→冪集合（要素nに対して、考えられる組み合わせが2^n）
サンプル問題
→moneyを超えない、組み合わせを選べ
"""

money = 500
item = (("みかん", 100), ("りんご", 200), ("ぶどう", 300))
n = len(item)
for i in range(2 ** n):
    bag = []
    total = 0
    for j in range(n):  # このループが一番のポイント
        if ((i >> j) & 1):  # 順に右にシフトさせ最下位bitのチェックを行う
            bag.append(item[j][0])  # フラグが立っていたら bag に果物を詰める
            total += item[j][1]
    if total < money:
        print(bag)

