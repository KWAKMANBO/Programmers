import java.util.*;


class Solution {

    public int[] solution(int m, int n, int[][] picture) {

        boolean[][] visited = new boolean[100][100];

        int maxSizeOfOneArea = 0;
        int areaNumbers =  0;

        int[] answer = new int[2];

        for (int i = 0; i < picture.length; i++) {
            for (int j = 0; j < picture[0].length; j++) {
                if (picture[i][j] != 0 && !visited[i][j]) {
                    maxSizeOfOneArea = Math.max(maxSizeOfOneArea, bfs(new int[]{i, j}, picture, visited));
                    areaNumbers++;
                }
            }
        }

        answer[0] = areaNumbers;
        answer[1] = maxSizeOfOneArea;
        return answer;
    } 

    static public int bfs(int[] startNode, int[][] picture, boolean[][] visited) {
        Queue<int[]> queue = new ArrayDeque<>();
        queue.add(startNode);
        visited[startNode[0]][startNode[1]] = true;
        int cnt = 1;

        while (!queue.isEmpty()) {
            int[] node = queue.poll();
            int x = node[0];
            int y = node[1];


            int[] dx = {-1, 1, 0, 0};
            int[] dy = {0, 0, -1, 1};

            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                // 방문 X && 다음 탐색칸이 같다면 && nx가 0과 101사이 && ny가 101 사이
                if ((0 <= nx && nx < picture.length) &&
                        (0 <= ny && ny < picture[0].length) &&
                        !visited[nx][ny] &&
                        picture[nx][ny] == picture[x][y]
                ) {
                    queue.add(new int[]{nx, ny});
                    visited[nx][ny] = true;
                    cnt++;
                }
            }

        }
        return cnt;
    }


}