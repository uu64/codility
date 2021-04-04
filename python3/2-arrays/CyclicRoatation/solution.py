from collections import deque

def solution(A, K):
    d = deque(A)
    d.rotate(K)
    return list(d)

solution([3, 8, 9, 7, 6], 3)
