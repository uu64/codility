class Solution {
    public int[] solution(int N, int[] A) {
        int[] counters = new int[N];
        for (int i = 0; i < N; i++) {
            counters[i] = 0;
        }
        for (int i = 0; i < A.length; i++) {
            A[i] -= 1;
        }

        int maxVal = 0;
        int offset = 0;
        for (int a: A) {
            if (a == N) {
                offset = maxVal;
            } else {
                if (counters[a] < offset) {
                    counters[a] = offset;
                }
                counters[a] += 1;
                if (maxVal < counters[a]) {
                    maxVal = counters[a];
                }
            }
        }

        for (int i = 0; i < N; i++) {
            if (counters[i] < offset) {
                counters[i] = offset;
            }
        }

        return counters;
    }
}