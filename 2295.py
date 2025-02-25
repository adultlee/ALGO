import sys
import bisect

def find_max_d(n, arr):
    arr.sort()  # 정렬 (O(N log N))

    two_sums = []
    
    # 모든 두 수의 합을 저장 (O(N²))
    for i in range(n):
        for j in range(i, n):
            two_sums.append(arr[i] + arr[j])
    
    # 두 수의 합을 정렬 (이분 탐색을 위해) (O(N² log N))
    two_sums.sort()

    # 가장 큰 값부터 탐색 (O(N log N))
    for k in range(n-1, -1, -1):  # pick = arr[k]를 고정
        for z in range(k+1):  # z를 0 ~ k에서 선택
            target = arr[k] - arr[z]  # x + y = pick - z
            
            # `two_sums`에서 target을 찾는 이분 탐색 (O(log N))
            idx = bisect.bisect_left(two_sums, target)
            if idx < len(two_sums) and two_sums[idx] == target:
                return arr[k]  # 최댓값을 찾으면 즉시 반환

    return -1  # (항상 존재하는 입력이므로 실행될 일 없음)

# 입력
n = int(sys.stdin.readline().strip())
arr = [int(sys.stdin.readline().strip()) for _ in range(n)]

# 실행 및 출력
print(find_max_d(n, arr))
