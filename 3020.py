import sys
import bisect

N , H = map(int, input().split())

BOT = []
TOP = []

for i in range(N):
 if i %2 == 0:
  BOT.append(int(input()))
 else :
  TOP.append(int(input()))

BOT.sort()
TOP.sort()

answer = [N , 0]

for layer in range(1, H+1):
 BOT_count = len(BOT) - bisect.bisect_left(BOT , layer) # layer 보다 작은 값의 개수를 새서 반환 
 TOP_count = len(TOP) - bisect.bisect_right(TOP , H-layer)
 COUNT = BOT_count + TOP_count


 if answer[0] > COUNT:
  answer = [COUNT , 1]
 elif answer[0] == COUNT:
  answer = [COUNT , answer[1] +1 ]

print(*answer)
 