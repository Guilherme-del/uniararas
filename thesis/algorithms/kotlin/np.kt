import java.io.File

fun hasFactor(n: Int): Boolean {
    for (i in 2..Math.sqrt(n.toDouble()).toInt()) {
        if (n % i == 0) return true
    }
    return false
}

fun main(args: Array<String>) {
    val tamanho = if (args.isNotEmpty()) args[0] else "small"
    val path = "datasets/$tamanho/factoring.json"

    try {
        val raw = File(path).readText().trim()
        val numbers = raw.removePrefix("[").removeSuffix("]")
            .split(",").mapNotNull { it.trim().toIntOrNull() }

        var count = 0
        for (n in numbers) {
            if (hasFactor(n)) count++
        }

        println("Fatorados $count números do dataset $tamanho.")
    } catch (e: Exception) {
        println("Erro: ${e.message}")
    }
}
