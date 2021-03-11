N = int(input())
A_B = [list(map(int, input().split())) for i in range(N)]

"""
A,B異なるとどちらかの最大
A<B同じだと、和となる
"""

min_A_B = float('inf')

for i in range(N):
    for j in range(N):
        if i == j:
            min_A_B = A_B[i][0] + A_B[j][1] if (A_B[i][0] + A_B[j][1]) < min_A_B else min_A_B
        else:
            min_A_B = max(A_B[i][0], A_B[j][1]) if max(A_B[i][0], A_B[j][1]) < min_A_B else min_A_B

print(min_A_B)