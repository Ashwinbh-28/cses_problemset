import sys
input = sys.stdin.readline

s = input().strip()
max_len = 1
current_len = 1

for i in range(1, len(s)):
    if s[i] == s[i-1]:
        current_len += 1
        max_len = max(max_len, current_len)
    else:
        current_len = 1

print(max_len)
