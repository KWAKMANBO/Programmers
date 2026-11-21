import java.util.*;

class Solution {
    public int[] solution(int m, int n, int startX, int startY, int[][] balls) {
        int[] answer = new int[balls.length];

        for (int i = 0; i < balls.length; i++) {
            answer[i] = calculateMinDistance(startX, startY, balls[i][0], balls[i][1], m, n);
        }

        return answer;
    }

    public int calculateMinDistance(int x1, int y1, int x2, int y2, int m, int n) {
        int minDist = Integer.MAX_VALUE;
        // 왼쪽 벽 대칭
        if (x1 < x2 || y1 != y2) {
            int mirrorX = -x2;
            int mirrorY = y2;
            minDist = Math.min(minDist, calculateDistance(x1, y1, mirrorX, mirrorY));
        }

        // 아래 벽 대칭
        if (y1 < y2 || x1 != x2) {
            int mirrorX = x2;
            int mirrorY = -y2;
            minDist = Math.min(minDist, calculateDistance(x1, y1, mirrorX, mirrorY));
        }

        // 오른쪽 벽 대칭
        if (x1 > x2 || y1 != y2) {
            int mirrorX = 2 * m - x2;
            int mirrorY = y2;

            minDist = Math.min(minDist, calculateDistance(x1, y1, mirrorX, mirrorY));
        }

        // 위쪽 벽 대칭
        if (y1 > y2 || x1 != x2) {
            int mirrorX = x2;
            int mirrorY = 2 * n - y2;

            minDist = Math.min(minDist, calculateDistance(x1, y1, mirrorX, mirrorY));

        }

        return minDist;


    }


    public int calculateDistance(int x1, int y1, int x2, int y2) {
        return (int) (Math.pow(x1 - x2, 2) + Math.pow(y1 - y2, 2));
    }

}