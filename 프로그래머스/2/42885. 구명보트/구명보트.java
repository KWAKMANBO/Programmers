import java.util.*;

class Solution {
    static public int solution(int[] people, int limit) {
        int answer = 0;
        int s = 0;
        int e = people.length - 1;
        Arrays.sort(people);
        while (s <= e) {
            if (people[s] + people[e] <= limit) {
                s += 1;
                e -= 1;
                answer += 1;
            } else if (people[s] + people[e] > limit) {
                answer += 1;
                e -= 1;
            }
        }
        return answer;
    }
}