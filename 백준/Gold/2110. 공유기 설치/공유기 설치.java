import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int C = Integer.parseInt(st.nextToken());

        ArrayList<Integer> homes = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            homes.add(Integer.parseInt(st.nextToken()));
        }
        Collections.sort(homes);
        int start = 1;
        int end = homes.get(N - 1) - homes.get(0);
        int answer = 0;

        while (start <= end) {
            int mid = (start + end) / 2;
            int current_home = homes.get(0);
            int cnt = 1;
            for (int i = 1; i < N; i++) {
                if (homes.get(i) >= current_home + mid) {

                    cnt += 1;
                    current_home = homes.get(i);
                }
            }

            if (cnt >= C) {
                start = mid + 1;
                answer = mid;
            } else {
                end = mid - 1;
            }

        }
        System.out.println(answer);
    }
}