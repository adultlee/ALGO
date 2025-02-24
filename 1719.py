import sys
import math

ip = sys.stdin.readline  # 빠른 입력

N, M = map(int, ip().split())  # 입력

graph = [[math.inf] * N for _ in range(N)]
edge = [[[] for _ in range(N)] for _ in range(N)]  # 최단 경로를 저장할 리스트

# 간선 입력 및 초기 설정
for _ in range(M):
    start, end, cost = map(int, ip().split())
    start, end = start - 1, end - 1  # 0-index 변환

    if cost < graph[start][end]:  # 더 짧은 경로가 있다면 갱신
        graph[start][end] = cost
        graph[end][start] = cost
        edge[start][end] = [start + 1, end + 1]  # 직접 연결된 경우
        edge[end][start] = [end + 1, start + 1]

    graph[start][start] = 0
    graph[end][end] = 0
    edge[start][start] = [0, "-"]
    edge[end][end] = [0, "-"]

# 플로이드-워셜 알고리즘으로 최단 경로 갱신 및 저장
for mid in range(N):
    for start in range(N):
        for end in range(N):
            if start == mid or mid == end or start == end:
                continue  # 중간 노드가 출발지나 목적지와 같으면 스킵

            SUM = graph[start][mid] + graph[mid][end]
            CUR = graph[start][end]

            if CUR > SUM:  # 더 짧은 경로 발견
                graph[start][end] = SUM
                graph[end][start] = SUM

                # 기존 경로 + 중간 노드 + 목적지 노드
                edge[start][end] = edge[start][mid] + edge[mid][end][1:]
                edge[end][start] = edge[end][mid] + edge[mid][start][1:]

for row in edge:
    print(" ".join(str(e[1]) if len(e) > 1 else "0" for e in row))
