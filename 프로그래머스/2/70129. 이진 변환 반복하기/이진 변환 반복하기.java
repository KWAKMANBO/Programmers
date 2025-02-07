

import java.util.*;

class Solution {

    public static int[] solution(String s) {
        int[] answer = {0, 0};
        while (!Objects.equals(s, "1")) {
            for (int i = 0; i < s.length(); i++) {
                if (s.charAt(i) == '0') {
                    answer[1] += 1;
                }
            }
            s = s.replaceAll("0", "");
            s = Integer.toBinaryString(s.length());
            answer[0] += 1;
        }
        return answer;
    }
}