import java.io.File

fun mergeSort(arr: List<Int>): List<Int> {
    if (arr.size <= 1) return arr
    val middle = arr.size / 2
    val left = mergeSort(arr.subList(0, middle))
    val right = mergeSort(arr.subList(middle, arr.size))
    return merge(left, right)
}

fun merge(left: List<Int>, right: List<Int>): List<Int> {
    val result = mutableListOf<Int>()
    var i = 0
    var j = 0
    while (i < left.size && j < right.size) {
        if (left[i] <= right[j]) {
            result.add(left[i])
            i++
        } else {
            result.add(right[j])
            j++
        }
    }
    result.addAll(left.drop(i))
    result.addAll(right.drop(j))
    return result
}

fun main(args: Array<String>) {
    val size = if (args.isNotEmpty()) args[0] else "small"
    val path = "datasets/$size/merge_sort.json"

    val content = File(path).readText()
        .replace("[", "")
        .replace("]", "")
        .trim()

    val arr = if (content.isNotEmpty()) content.split(",").map { it.trim().toInt() } else listOf()
    val sorted = mergeSort(arr)

    println("Ordenado ${sorted.size} elementos ($size)")
}
