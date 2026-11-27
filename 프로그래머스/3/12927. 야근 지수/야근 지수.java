import java.util.*;

class Solution {

    public long solution(int n, int[] works) {
        long answer = 0;

        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());

        Arrays.stream(works).forEach(w -> pq.add(w));

        while (n > 0) {
            int maxValue = pq.poll();
            maxValue -= 1;
            pq.add(maxValue);
            n -= 1;
        }

        for (int i : pq.stream().mapToInt(Integer::intValue).toArray()){
            if(i >0) answer += i * i;
        }
        return answer;
    }
}