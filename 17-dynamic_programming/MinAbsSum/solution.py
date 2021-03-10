import sys

sys.setrecursionlimit(50000)
memo = {}

def solution(A):
    ans = None
    for i in range(2**len(A)):
        seq = format(i, '0{}b'.format(len(A)))
        val = recursion(A, seq)
        if ans is None or abs(val) < ans:
            ans = abs(val)
    return ans



def recursion(A, seq):
    if len(A) == 1:
        return A[0] if seq[0] == '1' else -A[0]
    else:
        if seq[1:] in memo:
            rec = memo[seq[1:]]
        else:
            rec = recursion(A[1:], seq[1:])
            memo[seq[1:]] = rec
        return A[0] + rec if seq[0] == '1' else -A[0] + rec


print(solution([1, 5, 2, -2]))