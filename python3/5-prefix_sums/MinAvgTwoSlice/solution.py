def solution(A):
    N = len(A)
    ans = 0
    maxv = (A[0] + A[1]) / 2
    for i in range(N):
        if i < N-1:
            tmp = (A[i] + A[i+1]) / 2
            if tmp < maxv:
                maxv = tmp
                ans = i
        if i < N-2:
            tmp = (A[i] + A[i+1] + A[i+2]) / 3
            if tmp < maxv:
                maxv = tmp
                ans = i
    return ans