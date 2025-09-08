import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
expected = n * (n + 1) // 2
print(expected - sum(nums))
