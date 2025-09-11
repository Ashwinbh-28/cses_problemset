import sys
input = sys.stdin.readline

n = int(input())

total = n * (n+1) // 2

if total % 2 != 0:
    print("NO")
else:
    print("YES")
    target = total // 2
    set1, set2 = [], []

    for i in range(n, 0, -1):
        if target >= i:
            set1.append(i)
            target -= i
        else:
            set2.append(i)

    # Output result
    print(len(set1))
    print(*set1)
    print(len(set2))
    print(*set2)
