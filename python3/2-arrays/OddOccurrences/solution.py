from collections import Counter

def solution(A):
    occurrences = Counter(A)
    for k in occurrences:
        if occurrences[k] % 2 == 1:
            return k
    # should not happen
    return -1

