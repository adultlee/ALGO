import math


def solution(n, s, a, b, fares):
    answer = math.inf
    
    graph = [[math.inf] * (n+1) for _ in range(n+1)]
    
    for start, end ,value in fares:
        graph[start][end] = value
        graph[end][start] = value
        
        graph[start][start] = 0
        graph[end][end] = 0
        
        
    for mid in range(1,n+1):
        for start in range(1,n+1):
            for end in range(1,n+1):
                SUM = graph[start][mid] + graph[mid][end]
                CUR = graph[start][end]
                
                if start == mid or mid == end: # 이 부분도 마찬가지
                    continue
                
                graph[start][end] = min(SUM , CUR)
                graph[end][start] = min(SUM , CUR) # 이 로직은 중복되므로 지워도 괜찮 O(n^3)에서 반으로 줄어드니 의미가 있는것
                
    
    
    for mid in range(1, n+1):
        answer = min(answer , graph[s][mid] + graph[mid][a] + graph[mid][b])
    
    return answer

"""
왜인지 모르겠으나 시간초과 발생, 약간 더 최적화 할 방법이 있을듯
"""