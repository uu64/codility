class Solution {
    public int solution(int N) {
        char[] chars = Integer.toBinaryString(N).toCharArray();
        int ans = 0;
        int lastIdx = -1;
        for (int i = 0; i < chars.length; i++) {
            char c = chars[i];
            if (c == '1') {
                int gap = i - lastIdx - 1;
                if (lastIdx != -1 && ans < gap) {
                    ans = gap;
                }
                lastIdx = i;
            }
        }
        return ans;
    }
}

