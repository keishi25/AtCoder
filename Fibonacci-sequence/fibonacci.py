"""
# フィボナッチ数列
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987
F0 = 0,
F1 = 1,
Fn+2 = Fn + Fn+1 (n ≥ 0)

# n番目のフィボナッチ数列を出す
# 再帰を使用する
"""


def get_fibonacci_num(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return get_fibonacci_num(n - 1) + get_fibonacci_num(n - 2)

a = get_fibonacci_num(10)
print(a)