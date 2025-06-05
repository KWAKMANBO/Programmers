import java.lang.reflect.Array;
import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        ArrayDeque<Integer> queue = new ArrayDeque<>();
        ArrayList<Integer> answer = new ArrayList<>();


        for (int i = 1; i < N + 1; i++) {
            queue.add(i);
        }

        while (!queue.isEmpty()) {
            for (int i = 1; i < K + 1; i++) {
                if (i != K) {
                    queue.add(queue.pop());
                } else {
                    answer.add(queue.pop());
                }

            }
        }
        StringBuffer sb = new StringBuffer();
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        sb.append("<");
        for (int i = 0; i < answer.size(); i++) {
            sb.append(answer.get(i));

            if (i != answer.size() - 1) {
                sb.append(",");
                sb.append(" ");
            }
        }
        sb.append(">");
        bw.write(String.valueOf(sb));
        bw.flush();
        bw.close();
    }
}