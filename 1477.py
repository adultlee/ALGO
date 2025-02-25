import sys
import heapq

# 입력 처리
N, M, L = map(int, input().split())
REST_STORES = list(map(int, input().split()))
REST_STORES = REST_STORES if REST_STORES else [0]
REST_STORES.append(L)  # 고속도로의 끝(L) 추가
REST_STORES.sort()

heap = []  # 최대 힙 (Python은 최소 힙이므로 음수로 저장)

# 초기 구간을 힙에 추가
for i in range(1, len(REST_STORES)):
    distance = REST_STORES[i] - REST_STORES[i-1]
    heapq.heappush(heap, (-distance, 1, distance))  # 최대 힙 구현을 위해 길이를 음수로 저장

# 휴게소 M개 추가
for _ in range(M):
    max_gap, count, original_length = heapq.heappop(heap)  # 가장 긴 구간을 꺼냄
    count += 1  # 분할 개수 증가
    heapq.heappush(heap, (-original_length // count, count, original_length))  # 새 구간 추가

# 최장 구간 길이 출력
max_gap, count, original_length = heapq.heappop(heap)
print((original_length // count) if original_length % count == 0 else (original_length // count) + 1)
