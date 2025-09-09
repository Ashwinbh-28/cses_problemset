import sys
input = sys.stdin.readline

# take input of length of array
n = int(input())
# individual elements of array
arr = list(map(int, input().split()))
# function for the program

moves = 0
for i in range(1,n):
    if arr[i] < arr[i-1]:
        moves += arr[i-1] - arr[i]
        arr[i] = arr[i-1]

print(moves)
