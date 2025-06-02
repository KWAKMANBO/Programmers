import javax.sound.midi.Soundbank;
import java.util.*;
import java.io.*;
import java.lang.*;
import java.util.stream.Collector;

//Input1
//2
//홍길동 95
//이순신 77

public class SortScoreStudentProblem {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());

        ArrayList<Student> array = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            String name = st.nextToken();
            int score = Integer.parseInt(st.nextToken());
            ArrayList<Student> student = new ArrayList<>();
            Student s = new Student(name, score);

            array.add(s);
        }

        array.sort(new StudentCompartor());
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuffer sb = new StringBuffer();

        for (Student s : array) {
            sb.append(s.getName());
            sb.append(' ');
        }
        bw.write(String.valueOf(sb));
        bw.flush();
        bw.close();
    }

    static public class Student {
        String name;
        int score;

        private Student(String name, int score) {
            this.name = name;
            this.score = score;
        }

        @Override
        public String toString() {
            return this.name + " " + this.score;
        }

        public String getName() {
            return this.name;
        }
    }

    static class StudentCompartor implements Comparator<Student> {
        @Override
        public int compare(Student s1, Student s2) {
            // 양수 -> 오름차순
            // 음수 -> 내림차순
            return s1.score - s2.score;
        }
    }

}
