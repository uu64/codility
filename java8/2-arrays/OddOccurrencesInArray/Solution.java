import java.util.*;
class Solution {
    public int solution(int[] A) {
        Arrays.sort(A);
        int idx = 0;
        while (idx < A.length - 1) {
            if (A[idx] == A[idx+1]) {
                idx += 2;
                continue;
            } else {
                return A[idx];
            }
        }
        return A[A.length - 1];
    }
}
