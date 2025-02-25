def min_time_to_pass(N, M, times):
    left, right = 1, min(times) * M  # 최솟값과 최댓값 설정

    while left <= right:
        mid = (left + right) // 2
        count = sum(mid // t for t in times)  # 현재 mid 시간 내 심사 가능한 사람 수

        if count > M:  # 모든 사람을 심사할 수 있다면 시간 줄이기
            right = mid-1
        elif count == M:
            right = mid
        else:  # 부족하면 시간 늘리기
            left = mid + 1
    
    return left  # 최소 시간

# 입력 받기
N, M = map(int, input().split())
times = [int(input()) for _ in range(N)]

# 결과 출력
print(min_time_to_pass(N, M, times))
