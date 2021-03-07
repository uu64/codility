# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    s = format(N, 'b')
    ans = 0
    idx = 0
    for i in range(1, len(s)):
        if s[i] == '1':
            d = i - idx - 1
            if d > ans:
                ans = d
            idx = i

    return ans


print(solution(15))