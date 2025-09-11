import sys
input = sys.stdin.readline

n = int(input())
for i in range(1, n+1):
    total_pairs = i*i * (i*i - 1) // 2
    attack_pairs = 4 * (i-1) * (i-2)
    print(total_pairs - attack_pairs)


