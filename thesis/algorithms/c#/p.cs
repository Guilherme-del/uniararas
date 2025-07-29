using System;
using System.IO;
using System.Text.Json;
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
        int[] leftArray = array[left..(middle + 1)];
        int[] rightArray = array[(middle + 1)..(right + 1)];

        int i = 0, j = 0, k = left;

        while (i < leftArray.Length && j < rightArray.Length) {
            if (leftArray[i] <= rightArray[j]) {
                array[k++] = leftArray[i++];
            } else {
                array[k++] = rightArray[j++];
            }
        }

        while (i < leftArray.Length) array[k++] = leftArray[i++];
        while (j < rightArray.Length) array[k++] = rightArray[j++];
    }

    static void Main(string[] args) {
        string size = args.Length > 0 ? args[0] : "small";
        string path = $"../datasets/{size}/merge_sort_{size}.json";

        if (!File.Exists(path)) {
            Console.WriteLine("Arquivo não encontrado.");
            return;
        }

        int[] array = JsonSerializer.Deserialize<int[]>(File.ReadAllText(path));
        MergeSort(array, 0, array.Length - 1);
        Console.WriteLine($"Ordenado {array.Length} elementos ({size})");
    }
}
