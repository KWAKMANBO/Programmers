import java.util.*;

public class CountingSortMyVersion {
    public static void main(String[] args) {
        int[] array = {7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2};
        int[] counts = new int[array.length + 1];
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < array.length; i++) {
            counts[array[i]]++;
        }

        for (int i = 0; i < array.length; i++) {
            for (int j = 0; j < counts[i]; j++) {
                sb.append(i);
                sb.append(' ');
            }
        }
        System.out.println(sb);
    }
}
