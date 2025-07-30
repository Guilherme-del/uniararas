import java.io.File
import com.fasterxml.jackson.module.kotlin.jacksonObjectMapper
import com.fasterxml.jackson.module.kotlin.readValue

data class Program(val program: String)

fun simulate(code: String): Boolean {
    return code.trim().uppercase() == "HALT"
}

fun main(args: Array<String>) {
    val size = if (args.isNotEmpty()) args[0] else "small"
    val path = "datasets/$size/halting.json"
    val content = File(path).readText()
    val mapper = jacksonObjectMapper()
    val programs: List<Program> = mapper.readValue(content)
    val halted = programs.count { simulate(it.program) }
    println("$halted de ${programs.size} programas halting ($size)")
}
