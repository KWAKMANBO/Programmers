import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        int sum = 0;
        int cnt = 0;

        if (N > 2) {
            for (int i = 3; i < N + 1; i += 2) {
                sum += i;
                cnt += 1;
                if (sum >= N) break;
            }
            System.out.println(cnt);
        } else {
            System.out.println(1);
        }

    }
}
