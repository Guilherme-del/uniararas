import java.io.*;
import java.util.*;
import java.nio.file.Files;
import java.nio.file.Paths;

public class Np {
    public static boolean evaluateClause(List<Integer> clause, Map<Integer, Boolean> assignment) {
        for (int lit : clause) {
            int var = Math.abs(lit);
            boolean value = assignment.getOrDefault(var, false);
            if ((lit > 0 && value) || (lit < 0 && !value)) return true;
        }
        return false;
    }

    public static boolean isSatisfiable(List<List<Integer>> clauses, int numVars) {
        int total = 1 << numVars;
        for (int mask = 0; mask < total; mask++) {
            Map<Integer, Boolean> assignment = new HashMap<>();
            for (int i = 0; i < numVars; i++) {
                assignment.put(i + 1, ((mask >> i) & 1) == 1);
            }
            boolean allTrue = true;
            for (List<Integer> clause : clauses) {
                if (!evaluateClause(clause, assignment)) {
                    allTrue = false;
                    break;
                }
            }
            if (allTrue) return true;
        }
        return false;
    }

    public static List<List<Integer>> readSAT(String path) throws IOException {
        String content = new String(Files.readAllBytes(new File(path).toPath()));
        content = content.replaceAll("[\\[\\]\\n\\r]", "").trim();
        String[] clauses = content.split("},");
        List<List<Integer>> cnf = new ArrayList<>();
        for (String clause : clauses) {
            String[] nums = clause.replaceAll("[^0-9,\\-]", "").split(",");
            List<Integer> current = new ArrayList<>();
            for (String num : nums) {
                if (!num.isEmpty()) current.add(Integer.parseInt(num));
            }
            if (!current.isEmpty()) cnf.add(current);
        }
        return cnf;
    }

    public static void main(String[] args) throws IOException {
        String size = args.length > 0 ? args[0] : "small";
        String path = "datasets/" + size + "/sat.json";
        List<List<Integer>> cnf = readSAT(path);
        boolean sat = isSatisfiable(cnf, 20);
        System.out.println("SAT (" + size + "): " + (sat ? "Satisfatível" : "Insatisfatível"));
    }
}
