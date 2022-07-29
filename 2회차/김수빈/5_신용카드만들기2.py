import sys

sys.stdin = open("_신용카드만들기2.txt")

T = int(input())
first = ['3', '4', '5', '6', '9']

for i in range(1, T + 1):
    number = input()
    number_ = number.replace('-','')
    if number_[0] in first and len(number_) == 16:
        print(f'#{i} 1')
    else:
        print(f'#{i} 0')