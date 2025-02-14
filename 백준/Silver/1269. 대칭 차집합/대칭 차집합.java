import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        HashSet<Integer> nset = new HashSet<>();
        HashSet<Integer> mset = new HashSet<>();

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            nset.add(Integer.parseInt(st.nextToken()));
        }

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < m; i++) {
            mset.add(Integer.parseInt(st.nextToken()));
        }

        ArrayList<Integer> answer = new ArrayList<>();

        for (int i : nset) {
            if (!mset.contains(i)) {
                answer.add(i);
            }
        }

        for (int i : mset) {
            if (!nset.contains(i)) {
                answer.add(i);
            }
        }
        System.out.println(answer.size());
    }
}
