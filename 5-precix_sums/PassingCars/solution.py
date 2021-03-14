def solution(A):
    count = 0
    ans = 0
    for v in A:
        if v == 0:
            count += 1
        else:
            ans += count
            if ans > 1000000000:
                return -1
    return ans

