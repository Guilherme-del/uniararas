import java.io.File

fun simulate(code: String): Boolean {
    return code.trim().uppercase() == "HALT"
}

fun main(args: Array<String>) {
    val size = if (args.isNotEmpty()) args[0] else "small"
    val path = "datasets/$size/halting.json"
    val content = File(path).readText()

    val regex = Regex("\"program\"\\s*:\\s*\"(.*?)\"")
    val matches = regex.findAll(content)

    val programs = matches.map { it.groupValues[1] }.toList()
    val halted = programs.count { simulate(it) }

    println("$halted de ${programs.size} programas halting ($size)")
}
