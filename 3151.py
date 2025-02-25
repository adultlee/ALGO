N = int(input())
NUMBERS = sorted(list(map(int, input().split())))  # 정렬 필수
answer = 0

# i를 고정하고, 나머지 두 숫자는 투 포인터를 활용하여 찾기
for i in range(N):
    left, right = 0, N - 1  # 투 포인터 사용
    while left < right:
        if left == i:  # i와 같은 숫자는 제외
            left += 1
            continue
        if right == i:  # i와 같은 숫자는 제외
            right -= 1
            continue

        three_sum = NUMBERS[left] + NUMBERS[right] + NUMBERS[i]

        if three_sum == 0:
            # `left`와 `right`가 같은 값이 여러 개 있을 경우 한 번에 개수 추가
            l_count, r_count = 1, 1

            while left + 1 < right and NUMBERS[left] == NUMBERS[left + 1]:
                left += 1
                l_count += 1  # `left`가 같은 값이면 개수 증가
            
            while right - 1 > left and NUMBERS[right] == NUMBERS[right - 1]:
                right -= 1
                r_count += 1  # `right`가 같은 값이면 개수 증가
            
            # 경우의 수를 모두 추가 (l_count * r_count)
            answer += l_count * r_count

            left += 1
            right -= 1
        elif three_sum < 0:
            left += 1
        else:
            right -= 1

print(answer)
