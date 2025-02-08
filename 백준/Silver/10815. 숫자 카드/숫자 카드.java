
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.HashSet;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        // 문자열을 입력받을 BufferedReader 객체 생성
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // 문자열을 출력해줄 BuffredWriter 객체 생성
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        // 첫번쨰 입력
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        HashSet<Integer> target = new HashSet<>();
        for (int i = 0; i < n; i++) {
            target.add(Integer.parseInt(st.nextToken()));
        }

        // 두번째 입력
        int m = Integer.parseInt(br.readLine());
        int[] nums = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        StringBuilder answer = new StringBuilder();

        for (int i = 0; i < nums.length; i++) {
            if (target.contains(nums[i])) {
                answer.append("1 ");
            } else {
                answer.append("0 ");
            }
        }

        bw.write(answer + "\n");
        bw.flush();
        bw.close();


    }
}
