import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int[] wines = new int[n + 1];
        for (int i = 1; i < n + 1; i++) {
            st = new StringTokenizer(br.readLine());
            wines[i] = Integer.parseInt(st.nextToken());
        }
        int[] dp = new int[n + 1];
        int answer = 0;
        if (n >= 1) {
            dp[1] = wines[1];
            answer = dp[1];
        }
        if (n >= 2) {
            dp[2] = wines[1] + wines[2];
            answer = dp[2];
        }

        for (int i = 3; i < n + 1; i++) {
            dp[i] = Math.max(dp[i - 1], dp[i - 2] + wines[i]);
            dp[i] = Math.max(dp[i], dp[i - 3] + wines[i - 1] + wines[i]);
            if (dp[i] > answer) {
                answer = dp[i];
            }
        }
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write(String.valueOf(answer));
        bw.flush();
        bw.close();
    }
}