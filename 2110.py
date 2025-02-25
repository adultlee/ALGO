import sys
import math
import bisect

N , M = map(int, input().split())

Numbers = []

def get_count_list(numbers, term):
    cur = numbers[0]
    last = numbers[-1]
    count = [cur]
    idx = 0

    while cur <= last:
        index = bisect.bisect_left(numbers, cur)
        idx += 1

        if index >= len(numbers):  # bisect가 리스트 끝까지 갔다면 종료
            break

        if cur in numbers:  # 현재 값이 정확히 리스트에 존재하는 경우 추가
            count.append(cur)
            cur += term  # term만큼 증가
        else:  # 리스트에 없을 경우, bisect가 반환한 값 기준으로 추가
            count.append(numbers[index-1])
            cur = numbers[index-1] + term  # 다음 위치로 이동

    return sorted(list(set(count)))  # 중복 제거 후 정렬된 리스트 반환



for _ in range(N):
 Numbers.append(int(input()))

Numbers.sort()

start = 1
end = Numbers[len(Numbers) -1] * 2

result = 1

print(get_count_list(Numbers , 1))
print(get_count_list(Numbers , 100))

print( result)

"""
11 2
1
2
3
4
5
6
7
8
9
10
100

11 3
1
2
3
4
5
6
7
8
9
10
100

6 3
1
5
10
20
25
30

10 4
1
3
7
9
13
17
21
25
29
33

"""

