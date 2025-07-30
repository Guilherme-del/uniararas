using System;
using System.IO;
using System.Linq;

class MergeSortProgram {
    static void MergeSort(int[] array, int left, int right) {
        if (left < right) {
            int middle = (left + right) / 2;
            MergeSort(array, left, middle);
            MergeSort(array, middle + 1, right);
            Merge(array, left, middle, right);
        }
    }

    static void Merge(int[] array, int left, int middle, int right) {
        int[] leftArray = new int[middle - left + 1];
        int[] rightArray = new int[right - middle];

        Array.Copy(array, left, leftArray, 0, leftArray.Length);
        Array.Copy(array, middle + 1, rightArray, 0, rightArray.Length);

        int i = 0, j = 0, k = left;
        while (i < leftArray.Length && j < rightArray.Length)
            array[k++] = (leftArray[i] <= rightArray[j]) ? leftArray[i++] : rightArray[j++];

        while (i < leftArray.Length) array[k++] = leftArray[i++];
        while (j < rightArray.Length) array[k++] = rightArray[j++];
    }

    static int[] ParseJsonArray(string json) {
        string clean = json.Trim().TrimStart('[').TrimEnd(']');
        return clean.Split(',').Select(s => int.Parse(s.Trim())).ToArray();
    }

    static void Main(string[] args) {
        string size = args.Length > 0 ? args[0] : "small";
        string path = $"datasets/{size}/merge_sort.json";

        if (!File.Exists(path)) {
            Console.WriteLine("Arquivo não encontrado.");
            return;
        }

        string json = File.ReadAllText(path);
        int[] array = ParseJsonArray(json);

        Console.WriteLine($"Ordenando {size} elementos...");
        MergeSort(array, 0, array.Length - 1);
        Console.WriteLine($"Ordenado {array.Length} elementos ({size})");
    }
}
