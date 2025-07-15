import java.io.File
import com.fasterxml.jackson.module.kotlin.jacksonObjectMapper
import com.fasterxml.jackson.module.kotlin.readValue

data class Item(val weight: Int, val value: Int)
data class KnapsackInput(val capacity: Int, val items: List<Item>)

fun knapsack(items: List<Item>, capacity: Int): Int {
    val dp = IntArray(capacity + 1)
    for (item in items) {
        for (w in capacity downTo item.weight) {
            dp[w] = maxOf(dp[w], dp[w - item.weight] + item.value)
        }
    }
    return dp[capacity]
}

fun main(args: Array<String>) {
    val size = if (args.isNotEmpty()) args[0] else "small"
    val path = "../data/$size/knapsack_${size}.json"
    val content = File(path).readText()
    val mapper = jacksonObjectMapper()
    val input: KnapsackInput = mapper.readValue(content)
    val result = knapsack(input.items, input.capacity)
    println("Valor máximo para ${input.items.size} itens ($size): $result")
}
