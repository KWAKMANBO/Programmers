
class Solution {

    private final char[] characters = {'A', 'C', 'F', 'J', 'M', 'N', 'R', 'T'};

    public int solution(int n, String[] data) {
        boolean[] visited = new boolean[8];

        return dfs("", 0, data, visited);
    }

    public int dfs(String currentString, int depth,
                   String[] data, boolean[] visited) {

        // 8명의 순열이 완성되면 조건 검사
        if (depth == 8) {
            return isValid(currentString, data) ? 1 : 0;
        }

        int count = 0;

        for (int i = 0; i < characters.length; i++) {
            if (visited[i]) continue;

            // 선택
            visited[i] = true;

            // 하위 DFS에서 찾은 정답 개수 누적
            count += dfs(
                    currentString + characters[i],
                    depth + 1,
                    data,
                    visited
            );

            // 선택 취소 (백트래킹)
            visited[i] = false;
        }

        return count;
    }

    public boolean isValid(String photo, String[] data) {

        // 모든 조건을 만족해야 함
        for (String condition : data) {

            char startChar = condition.charAt(0);
            char endChar = condition.charAt(2);
            char operator = condition.charAt(3);
            int operand = condition.charAt(4) - '0';

            int startCharIndex = photo.indexOf(startChar);
            int endCharIndex = photo.indexOf(endChar);

            // 두 사람 사이에 있는 인원 수
            int distance = Math.abs(startCharIndex - endCharIndex) - 1;

            if (operator == '=' && distance != operand) {
                return false;
            } else if (operator == '>' && distance <= operand) {
                return false;
            } else if (operator == '<' && distance >= operand) {
                return false;
            }
        }

        return true;
    }
}
