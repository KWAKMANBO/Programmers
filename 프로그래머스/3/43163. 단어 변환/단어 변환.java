import java.util.*;


class Solution {
    
    
    public int solution(String begin, String target, String[] words) {
        Queue<Information> queue = new ArrayDeque<>();
        queue.add(new Information(begin, 0));

        HashSet<String> visited = new HashSet<>();
        visited.add(begin);

        int wLength = words.length;
        int bLength = begin.length();


        int cnt = 0;
        while (!queue.isEmpty()) {
            Information node = queue.poll();

            if (node.word.equals(target)) return node.cnt;

            for (int i = 0; i < wLength; i++) {
                String word = words[i];
                int diff = 0;

                for (int j = 0; j < bLength; j++) {
                    if (node.word.charAt(j) != word.charAt(j)) diff++;

                    if (diff > 1) break;
                }

                if (diff == 1 && !visited.contains(word)) {
                    queue.add(new Information(word, node.cnt + 1));
                    visited.add(word);
                }
            }
        }
        return 0;
    }

    static public class Information {
        public String word;
        public int cnt;

        Information(String word, int cnt) {
            this.word = word;
            this.cnt = cnt;
        }

        @Override
        public String toString() {
            return "word : " + word + ", cnt : " + cnt;
        }
    }



}