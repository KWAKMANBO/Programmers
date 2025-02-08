import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        HashSet<String> inspect_set = new HashSet<>();
        for (int i = 0; i < N; i++) {
            inspect_set.add(br.readLine().strip());
        }

        String[] inspect_lst = new String[M];
        for (int i = 0; i < M; i++) {
            inspect_lst[i] = br.readLine().strip();
        }

        int answer = 0;

        for (int i = 0; i < M; i++) {
            if (inspect_set.contains(inspect_lst[i])) {
                answer += 1;
            }
        }
        bw.write(answer + "\n");
        bw.flush();
        bw.close();

    }
}