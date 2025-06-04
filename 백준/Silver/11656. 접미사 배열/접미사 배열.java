import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        String s = st.nextToken().strip();
        ArrayList<String> lst = new ArrayList<>();
        for (int i = 0; i < s.length(); i++) {
            lst.add(s.substring(i));
        }

        Collections.sort(lst);

        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuffer sb = new StringBuffer();

        for (String str : lst) {
            sb.append(str);
            sb.append("\n");
        }
        bw.write(String.valueOf(sb));
        bw.flush();
        bw.close();

    }
}