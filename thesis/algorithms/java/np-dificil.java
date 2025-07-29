import java.io.*;
import java.util.*;

public class NPDificil {
    public static void main(String[] args) throws IOException {
        String size = args.length > 0 ? args[0] : "small";
        String path = "../datasets/" + size + "/halting_" + size + ".json";
        BufferedReader reader = new BufferedReader(new FileReader(path));
        String line;
        int halted = 0, total = 0;
        while ((line = reader.readLine()) != null) {
            if (line.contains("program")) total++;
            if (line.contains("HALT")) halted++;
        }
        reader.close();
        System.out.println(halted + " de " + total + " programas halting (" + size + ")");
    }
}
