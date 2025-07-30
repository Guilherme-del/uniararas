import java.io.*;
import java.util.*;

public class P {
    public static void mergeSort(int[] arr, int l, int r) {
        if (l < r) {
            int m = (l + r) / 2;
            mergeSort(arr, l, m);
            mergeSort(arr, m + 1, r);
            merge(arr, l, m, r);
        }
    }

    public static void merge(int[] arr, int l, int m, int r) {
        int[] left = Arrays.copyOfRange(arr, l, m + 1);
        int[] right = Arrays.copyOfRange(arr, m + 1, r + 1);
        int i = 0, j = 0, k = l;

        while (i < left.length && j < right.length) {
            arr[k++] = (left[i] <= right[j]) ? left[i++] : right[j++];
        }
        while (i < left.length) arr[k++] = left[i++];
        while (j < right.length) arr[k++] = right[j++];
    }

    public static int[] readJsonArray(String path) throws IOException {
        String content = new String(Files.readAllBytes(new File(path).toPath()));
        content = content.replace("[", "").replace("]", "").trim();
        String[] parts = content.split(",");
        return Arrays.stream(parts).mapToInt(Integer::parseInt).toArray();
    }

    public static void main(String[] args) throws IOException {
        String size = args.length > 0 ? args[0] : "small";
        String path = "datasets/" + size + "/merge_sort.json";
        int[] arr = readJsonArray(path);
        mergeSort(arr, 0, arr.length - 1);
        System.out.println("Ordenado " + arr.length + " elementos (" + size + ")");
    }
}
