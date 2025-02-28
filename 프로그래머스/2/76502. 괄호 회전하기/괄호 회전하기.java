import java.util.*;

class Solution {
        public static int solution(String s) {
        int answer = 0;

        for (int i = 0; i < s.length() - 1; i++) {
            Stack<Character> stack = new Stack<Character>();
            String new_s = s.substring(i) + s.substring(0, i);
            int cnt = 0;
            char c = 'c';
            for (char ch : new_s.toCharArray()) {
                if (ch == '(' || ch == '{' || ch == '[') {
                    stack.add(ch);
                }

                if ((!stack.empty() && stack.peek() == '(' && ch == ')')
                        || (!stack.empty() && stack.peek() == '[' && ch == ']') ||
                        (!stack.empty() && stack.peek() == '{' && ch == '}')) {
                    stack.pop();
                    cnt += 1;
                }
            }
            if (stack.empty() && cnt > 0) {
                answer += 1;
            }
        }
        return answer;
    }
}