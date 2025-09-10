import sys
input = sys.stdin.readline

n = int(input())
for i in range(1, n+1):
    total_pairs = k*k + (k*k - 1) // 2
    attack_pairs = 4 * (k-1) * (k-2)
    print(total_pairs - attack_pairs)
