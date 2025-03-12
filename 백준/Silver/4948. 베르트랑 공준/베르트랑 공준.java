import java.io.*;
import java.util.*;
import java.lang.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        ArrayList<Integer> nums = new ArrayList<>();

        while (true) {
            int n = Integer.parseInt(br.readLine());
            if (n == 0) break;
            nums.add(n);
        }
        int max_num = 0;
        for (int i : nums) {
            max_num = Math.max(max_num, i);
        }

        int[] primes = getPrimes(max_num);
        StringBuilder sb = new StringBuilder();
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        for (int i : nums) {
            int cnt = 0;
            for (int j = i + 1; j < 2 * i +1; j++) {
                if (primes[j] != 0) {
                    cnt += 1;
                }
            }
            sb.append(cnt).append("\n");
        }
        System.out.println(sb);
    }

    public static int[] getPrimes(int n) {
        int max = n * 2;
        int[] arr = new int[max + 1];
        int end = (int) (Math.sqrt(max)) + 1;
        for (int i = 0; i < max + 1; i++) {
            arr[i] = i;
        }
        for (int i = 2; i < end; i++) {
            if (arr[i] == 0) continue;

            for (int j = i * i; j < max + 1; j += i) {
                arr[j] = 0;
            }

        }
        arr[0] =0;
        arr[1] =0;
        return arr;
    }
}
