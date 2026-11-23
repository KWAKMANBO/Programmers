
import java.util.*;

class Solution { 

    public static void main(String[] args) {
        Solution s = new Solution();

        System.out.println(Arrays.toString(s.solution(new String[]{"SL", "LR"})));
        System.out.println(Arrays.toString(s.solution(new String[]{"S"})));
        System.out.println(Arrays.toString(s.solution(new String[]{"R", "R"})));
    }


    public int[] solution(String[] grid) {
        ArrayList<Integer> numbers = new ArrayList<>();
        int m = grid.length;
        int n = grid[0].length();


        boolean[][][] visited = new boolean[m][n][4];

        int[][] direction = new int[][]{{-1, 0}, {0, 1}, {1, 0}, {0, -1}};

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                // 0 - 상
                // 1 - 우
                // 2 - 하
                // 3 - 좌

                for (int k = 0; k < 4; k++) {
                    if (visited[i][j][k]) continue;

                    int cnt = 0;

                    int r = i;
                    int c = j;
                    int d = k;
                    while (!visited[r][c][d]) {
                        visited[r][c][d] = true;
                        cnt++;

                        if (grid[r].charAt(c) == 'L') {
                            d = (d + 3) % 4;
                        } else if (grid[r].charAt(c) == 'R') {
                            d = (d + 1) % 4;
                        }

                        r = (r + direction[d][0] + m) % (m);
                        c = (c + direction[d][1] + n) % n;


                    }

                    numbers.add(cnt);
                }
            }
        }

        int[] answer = numbers.stream().mapToInt(Integer::intValue).toArray();
        Arrays.sort(answer);

        return answer;
    }


}