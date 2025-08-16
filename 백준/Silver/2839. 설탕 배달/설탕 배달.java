import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int answer = 0;

        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        while (N > 0) {
            if (N % 5 == 0) {
                answer += N / 5;
                break;
            }
            if (N < 3) {
                answer = -1;
                break;
            }
            N -= 3;
            answer++;
        }
        bw.write(String.valueOf(answer));
        bw.flush();
        bw.close();
    }
}