def solution(A):
    allSum = sum(A)
    ans = 2001
    subSum = 0
    for i in range(len(A)-1):
        subSum += A[i]
        diff = abs(subSum - (allSum - subSum))
        if diff < ans:
            ans = diff
    return ans
