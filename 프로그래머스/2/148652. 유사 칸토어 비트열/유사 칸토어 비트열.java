class Solution {
    public int solution(int n, long l, long r) {
        return dfs(n, 1, l, r);
    }

    public int dfs(int n, long sectionStart, long l, long r) {

        long length = (long) Math.pow(5, n);
        long sectionEnd = sectionStart + length - 1;

        if (sectionEnd < l ||r < sectionStart) return 0;

        if (l <= sectionStart && sectionEnd <= r) return (int) Math.pow(4, n);

        if (n == 0) return 1;

        int result = 0;

        long sectionSize = length / 5;

        for (int i = 0; i < 5; i++) {
            if (i == 2) continue;

            long nextSectionStart = sectionStart + sectionSize * i;

            result  += dfs(n - 1, nextSectionStart, l, r);
        }
        return result;
    }
}