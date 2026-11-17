import java.util.*;

class Solution {
    static int N = 8;

    static char[] characters = {'A', 'C', 'F', 'J', 'M', 'N', 'R', 'T'};
    static boolean[] visited = new boolean[N];
    static ArrayList<String> photos = new ArrayList<>();


    public int solution(int n, String[] data) {
        photos.clear();
        dfs("", 0);
        int answer = photos.size();


        for (String photo : photos) {
            for (int i = 0; i < n; i++) {
                char startChar = data[i].charAt(0);
                char endChar = data[i].charAt(2);
                char operator = data[i].charAt(3);
                int operand = data[i].charAt(4) - '0';


                int startCharIndex = photo.indexOf(startChar);
                int endCharIndex = photo.indexOf(endChar);

                if (operator == '=' && Math.abs(startCharIndex - endCharIndex) - 1 != operand) {
                    answer--;
                    break;
                } else if (operator == '>' && Math.abs(startCharIndex - endCharIndex) - 1 <= operand) {
                    answer--;
                    break;
                } else if (operator == '<' && Math.abs(startCharIndex - endCharIndex) - 1 >= operand) {
                    answer--;
                    break;
                }


            }
        }


        return answer;
    }

    static public void dfs(String currentString, int depth) {

        if (depth == 8) {
            photos.add(currentString);
            return;

        }

        for (int i = 0; i < characters.length; i++) {
            if (visited[i]) continue;

            visited[i] = true;
            dfs(currentString + characters[i], depth + 1);
            visited[i] = false;
        }


    }
}