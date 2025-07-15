import java.io.File
import com.fasterxml.jackson.module.kotlin.jacksonObjectMapper
import com.fasterxml.jackson.module.kotlin.readValue
import kotlin.math.abs

fun evaluateClause(clause: List<Int>, assignment: Map<Int, Boolean>): Boolean {
    return clause.any { lit ->
        val value = assignment[abs(lit)]
        (lit > 0 && value == true) || (lit < 0 && value == false)
    }
}

fun isSatisfiable(clauses: List<List<Int>>, numVars: Int): Boolean {
    val total = 1.shl(numVars)
    for (mask in 0 until total) {
        val assignment = mutableMapOf<Int, Boolean>()
        for (i in 0 until numVars) {
            assignment[i + 1] = (mask.shr(i) and 1) == 1
        }
        if (clauses.all { evaluateClause(it, assignment) }) {
            return true
        }
    }
    return false
}

fun main(args: Array<String>) {
    val size = if (args.isNotEmpty()) args[0] else "small"
    val path = "../data/$size/sat_${size}.json"
    val content = File(path).readText()
    val mapper = jacksonObjectMapper()
    val clauses: List<List<Int>> = mapper.readValue(content)
    val result = isSatisfiable(clauses, 20)
    println("SAT ($size): ${if (result) "Satisfatível" else "Insatisfatível"}")
}
