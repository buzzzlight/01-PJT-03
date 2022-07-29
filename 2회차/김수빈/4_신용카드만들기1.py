import sys

sys.stdin = open("_신용카드만들기1.txt")

T = int(input())

for i in range(1, T + 1):
    number = list(map(int, input().split()))
    odd = sum(number[0:15:2]) * 2   # 홀수자리 숫자 합 X 2
    even = sum(number[1:15:2])      # 짝수자리 숫자 합
    total = odd + even
    N = 10 - (total % 10)
    if N == 10:
        N = 0
    print(f'#{i} {N}')