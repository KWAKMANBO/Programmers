import java.util.*;

class Solution {
      public int[] solution(int[] numbers) {
        int[] answer = new int[numbers.length];
        for (int i = 0; i < numbers.length; i++) {
            answer[i] = -1;
        }
        Stack<Integer> stack = new Stack<>();

        for(int i =0; i < numbers.length; i++){
            while(!stack.empty() && numbers[stack.peek()] < numbers[i]){
                answer[stack.pop()] = numbers[i];
            }
            stack.add(i);
        }

        return answer;
    }
}