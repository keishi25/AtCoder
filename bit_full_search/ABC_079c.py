"""
https://atcoder.jp/contests/abc079/tasks/abc079_c
"""

import sys
input_list_str = list(input())
input_list = [int(i) for i in input_list_str]

operator_num = 3
total_num = 2 ** operator_num

for i in range(total_num):

    tmp_num = input_list[0]
    tmp_list = str(input_list[0])

    for j in range(operator_num):
        if (i >> (2-j)) & 1:
            tmp_num += input_list[j+1]
            tmp_list += "+" + str(input_list[j+1])
        else:
            tmp_num -= input_list[j+1]
            tmp_list += "-" + str(input_list[j+1])

    if tmp_num == 7:
        print(tmp_list+"=7")
        sys.exit()



