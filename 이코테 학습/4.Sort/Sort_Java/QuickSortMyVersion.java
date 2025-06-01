import java.util.*;

public class QuickSortMyVersion {
    public static void main(String[] args) {
        int[] array = {5, 7, 9, 0, 3, 1, 6, 2, 4, 8};
        quick_sort(array, 0, array.length - 1);

        System.out.println(Arrays.toString(array));
    }

    static public void quick_sort(int[] array, int start, int end) {
        if (start >= end) return;

        int pivot = start;
        int left = start + 1;
        int right = end;

        while (left <= right) {
            while (left <= end && array[left] <= array[pivot]) left++;

            while (right > start && array[right] >= array[pivot]) right--;
            if (left < right) {
                int tmp = array[left];
                array[left] = array[right];
                array[right] = tmp;
            } else {
                int tmp = array[pivot];
                array[pivot] = array[right];
                array[right] = tmp;
            }
        }
        quick_sort(array, start, right - 1);
        quick_sort(array, right + 1, end);

    }

}
