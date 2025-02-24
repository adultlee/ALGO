import sys
import math
sys.setrecursionlimit(10**6)

N = int(input())
M = int(input())

graph = [[math.inf for _ in range(N)] for _ in range(N)]

for _ in range(M):
 start , end , value = map(int, input().split())
 graph[start-1][end -1] = min(value, graph[start-1][end -1])

 graph[start-1][start-1] = 0
 graph[end-1][end-1] = 0



for mid in range(N):
 for start in range(N):
  for end in range(N):
   graph[start][end] = min(graph[start][mid] + graph[mid][end] , graph[start][end])

for r in range(N):
 for c in range(N):
  if graph[r][c] == math.inf:
   graph[r][c] = 0

for g in graph:
 print(*g)

