import sys

def count_less_equal(n, x):
    """ x 이하의 숫자가 몇 개인지 카운트하는 함수 """
    count = 0
    for i in range(1, n + 1):
        count += min(n, x // i)  # 각 행에서 x 이하의 개수
    return count

def find_kth_number(n, k):
    left, right = 1, n * n  # B의 최소값과 최대값 범위
    answer = 0

    while left <= right:
        mid = (left + right) // 2
        if count_less_equal(n, mid) >= k:
            answer = mid  # 후보 정답
            right = mid - 1  # 더 작은 값이 가능한지 탐색
        else:
            left = mid + 1  # 너무 작은 경우 mid 증가

    return answer

# 입력
n = int(sys.stdin.readline().strip())
k = int(sys.stdin.readline().strip())

# 실행 및 출력
print(find_kth_number(n, k))
