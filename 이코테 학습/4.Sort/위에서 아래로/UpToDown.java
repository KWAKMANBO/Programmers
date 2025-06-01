import java.io.*;
import java.util.*;

// Input1
// 3
// 15
// 27
// 12


public class UpToDown {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());

        ArrayList<Integer> array = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            array.add(Integer.parseInt(st.nextToken()));
        }
        Collections.sort(array);

        //System.out.println(Arrays.toString(array.toArray()));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();
        for (Integer a : array) {
            sb.append(a);
            sb.append(" ");
        }
        bw.write(String.valueOf(sb));
        bw.flush();
        bw.close();
    }
}

