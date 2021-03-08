"""
https://nashidos.hatenablog.com/entry/2020/08/20/223104
エラトステネスの篩を用いて、素数を抽出する
"""


def sieve_of_eratosthenes(n):
    """
    概要
    １．２からnまでの整数の配列を準備する
    ２．配列の中で一番小さい数字の取得。一時保存配列に格納
    ３．1.の倍数を2.の配列から除去する
    ４．2.3を繰り返す。2.で取得する数字が、n**0.5以下まで繰り返す
    ５．残った配列と一時保存配列をマージする
    :param n: 任意の整数
    :return: ans: 2からnまでの素数の配列
    """
    integer_list = [i for i in range(2, n+1)]
    tmp_prime_list = []
    while integer_list[0] <= n**0.5:
        min_prime = integer_list.pop(0)
        tmp_prime_list.append(min_prime)
        integer_list = [e for e in integer_list if not e % min_prime == 0]

    tmp_prime_list.extend(integer_list)

    return tmp_prime_list


if __name__ == "__main__":

    ans = sieve_of_eratosthenes(100)
    print(ans)
