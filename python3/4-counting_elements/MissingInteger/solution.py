import heapq

def solution(A):
    heapq.heapify(A)
    prev = 0
    while len(A) > 0:
        v = heapq.heappop(A)
        if v > prev + 1:
            return prev + 1
        if v > 0:
            prev = v
    return prev + 1

print(solution([-1, 1, 2, 3]))