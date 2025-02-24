import sys
import math

input = sys.stdin.readline 
N ,M = map(int, input().split())
graph = [[0 for _ in range(N)] for _ in range(N)]

for _ in range(M):
 start , end = map(int, input().split())
 graph[start-1][end-1] = -1
 graph[end-1][start-1] = 1

C = int(input())

for mid in range(N):
 for start in range(N):
  for end in range(N):
   graph[start][end] = -1 if graph[start][mid] == -1 and  graph[mid][end] == -1 else graph[start][end]
   graph[end][start] = 1 if graph[end][mid] == 1 and  graph[mid][start] == 1 else graph[end][start]

answer = []

for _ in range(C):
 start , end = map(int, input().split())
 answer.append(graph[start-1][end-1])


for a in answer:
 print(a)


## 하지만 시간 복잡도 이슈 발생 pypy로 제출
 

