import sys

sys.stdin = open("_최빈수구하기.txt")

T = int(input())

for i in range(T):
    test_case = input()
    score = list(input().split())
    score_set = list(set(score))
    cnt_list = []
    for j in score_set:
        cnt = score.count(j)
        cnt_list.append(cnt)

    print(f'#{test_case} {score_set[cnt_list.index(max(cnt_list))]}')

    # if cnt_list.count(max(cnt_list)) > 1:
    #     print(f'#{test_case} {max(score_set[cnt_list.index(max(cnt_list))])}')
    # else:
    #     print(f'#{test_case} {score_set[cnt_list.index(max(cnt_list))]}')

# A = {1, 2, 3}
# B = [1, 2, 3, 3, 2]
# C = []
# for i in A:
#     print(B.count(i))
#     C.append(B.count(i))
#     print(C)