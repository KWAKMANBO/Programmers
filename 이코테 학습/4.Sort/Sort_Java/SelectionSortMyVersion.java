import java.util.Arrays;

public class SelectionSortMyVersion {
    public static void main(String[] args) {
        int[] array = {7, 5, 9, 0, 3, 1, 6, 2, 4, 8};

        for (int i = 0; i < array.length - 1; i++) {
            int min_index = i;
            for (int j = i + 1; j < array.length; j++) {
                if (array[j] <= array[min_index]) min_index = j;
            }
            int tmp = array[i];
            array[i] = array[min_index];
            array[min_index] = tmp;
        }
        System.out.println(Arrays.toString(array));
    }
}
