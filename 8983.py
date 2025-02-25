import bisect

def get_closest_index(GUNS , value):
 idx = bisect.bisect_left(GUNS , curX)
 if idx >= len(GUNS):
  return len(GUNS) -1

 if idx == 0 :
  return 0

 return  idx if abs(value - GUNS[idx]) < abs(value - GUNS[idx-1]) else idx-1



N ,M , L = map(int, input().split())

GUNS = list(map(int, input().split()))

POS = []

answer = 0

for _ in range(M):
 x , y = map(int, input().split())

 POS.append((x,y))

GUNS.sort()

for pos in POS:
 curX , curY = pos
 if curY > L:
  continue

 
 idx = get_closest_index(GUNS , curX)

 min_value = abs(GUNS[idx] - curX) + curY
 
 if min_value <= L:
  
  answer+=1



print(answer)



"""
4 8 4
6 1 4 9
7 2
3 3
4 5
5 1
2 2
1 4
8 4
9 4


"""
