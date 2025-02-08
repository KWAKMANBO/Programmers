class Solution {
 public int[] solution(int brown, int yellow) {
        int[] answer = {0, 0};
        for (int i = 1; i <= yellow; i++) {
            if (yellow % i == 0) {
                int w = i;
                int h = yellow / i;
                if ((2 * w + 2 * h + 4) == brown) {
                    answer[0] = w + 2;
                    answer[1] = h + 2;
                }
            }
        }
        return answer;
    }
}