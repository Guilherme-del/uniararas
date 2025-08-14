import java.io.File

data class Item(val weight: Int, val value: Int)

fun knapsack(items: List<Item>, capacity: Int): Int {
    // Ordena por valor/peso decrescente
    val sorted = items.sortedByDescending { it.value.toDouble() / it.weight }

    var totalValue = 0
    var currentWeight = 0

    for (item in sorted) {
        if (currentWeight + item.weight <= capacity) {
            currentWeight += item.weight
            totalValue += item.value
        }
    }

    return totalValue
}

fun parseKnapsackJson(path: String): Pair<Int, List<Item>> {
    val content = File(path).readText()

    // Extrair capacidade
    val capacityRegex = """"capacity"\s*:\s*(\d+)""".toRegex()
    val capacity = capacityRegex.find(content)?.groupValues?.get(1)?.toIntOrNull() ?: 0

    // Extrair itens
    val itemRegex = """\{\s*"weight"\s*:\s*(\d+)\s*,\s*"value"\s*:\s*(\d+)\s*}""".toRegex()
    val items = itemRegex.findAll(content).map {
        val (w, v) = it.destructured
        Item(w.toInt(), v.toInt())
    }.toList()

    return capacity to items
}

fun main(args: Array<String>) {
    val size = if (args.isNotEmpty()) args[0] else "small"
    val path = "datasets/$size/knapsack.json"

    val (capacity, items) = parseKnapsackJson(path)

    if (items.isEmpty()) {
        println("Erro ao ler o arquivo ou nenhum item encontrado.")
        return
    }

    val result = knapsack(items, capacity)
    println("Valor aproximado (greedy) para ${items.size} itens (capacidade $capacity, $size): $result")
}
