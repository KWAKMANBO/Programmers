import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        HashMap<String, Integer> nametonum = new HashMap<>();
        HashMap<Integer, String> numtoname = new HashMap<>();

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            String s = st.nextToken();
            nametonum.put(s, i + 1);
            numtoname.put(i + 1, s);
        }


        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            String q = st.nextToken();
            if (isAlpha(q)) {
                sb.append(nametonum.get(q));
            } else {
                sb.append(numtoname.get(Integer.parseInt(q)));
            }
            sb.append("\n");
        }

        System.out.println(sb);
    }

    public static boolean isAlpha(String str) {
        for (int i = 0; i < str.length(); i++) {
            char c = str.charAt(i);
            if (!('A' <= c && c <= 'Z') && !('a' <= c && c <= 'z')) {
                return false;
            }
        }
        return true;
    }
}