import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        HashMap<String, String> people = new HashMap<>();

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            String name = st.nextToken();
            String status = st.nextToken();
            people.put(name, status);
        }

        ArrayList<String> answer = new ArrayList<>();
        for (String p : people.keySet()) {
            if (people.get(p).equals("enter")) {
                answer.add(p);
            }
        }

        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        answer.sort(Collections.reverseOrder());
        for (String name : answer) {
            bw.write(name + "\n");
            bw.flush();
        }
        bw.close();
    }
}
