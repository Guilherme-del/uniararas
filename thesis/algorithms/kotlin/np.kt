import java.io.File
import kotlin.math.abs

fun parseClauses(raw: String): List<List<Int>> {
    return raw
        .replace("[", "")
        .replace("]", "")
        .split(",")
        .mapNotNull { it.trim().toIntOrNull() }
        .chunked(3) // cada cláusula tem 3 literais
}

fun evaluateClause(clause: List<Int>, assignment: Map<Int, Boolean>): Boolean {
    return clause.any { lit ->
        val value = assignment[abs(lit)] ?: false
        (lit > 0 && value) || (lit < 0 && !value)
    }
}

fun isSatisfiable(clauses: List<List<Int>>, numVars: Int): Boolean {
    val total = 1.shl(numVars)
    for (mask in 0 until total) {
        val assignment = (1..numVars).associateWith { ((mask shr (it - 1)) and 1) == 1 }
        if (clauses.all { evaluateClause(it, assignment) }) return true
    }
    return false
}

fun main(args: Array<String>) {
    val size = if (args.isNotEmpty()) args[0] else "small"
    val path = "datasets/$size/sat.json"
    val raw = File(path).readText()
    val clauses = parseClauses(raw)
    val sat = isSatisfiable(clauses, 20)
    println("SAT ($size): ${if (sat) "Satisfatível" else "Insatisfatível"}")
}
