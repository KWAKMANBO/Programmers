import java.io.*;
import java.util.*;

//Input1
//5 3
//        1 2 5 4 3
//        5 5 6 6 5

public class TwoArraysChangingElement {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        Integer[] array1 = new Integer[N];
        Integer[] array2 = new Integer[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            array1[i] = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            array2[i] = Integer.parseInt(st.nextToken());
        }


        Arrays.sort(array1);
        Arrays.sort(array2, Collections.reverseOrder());

        for (int i = 0; i < K; i++) {
            if (array1[i] < array2[i]) {
                int tmp = array1[i];
                array1[i] = array2[i];
                array2[i] = tmp;
            } else {
                break;
            }
        }
        int answer = 0;
        for (int i = 0; i < N; i++) {
            answer += array1[i];
        }

        System.out.println(answer);

    }
}
