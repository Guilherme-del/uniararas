import java.io.*;
import java.util.regex.*;

public class NpDificil {
    public static void main(String[] args) throws IOException {
        String size = args.length > 0 ? args[0] : "small";
        String path = "datasets/" + size + "/halting.json";
        StringBuilder content = new StringBuilder();
        BufferedReader reader = new BufferedReader(new FileReader(path));
        String line;
        while ((line = reader.readLine()) != null) content.append(line);
        reader.close();

        Pattern pattern = Pattern.compile("\"program\"\\s*:\\s*\"(.*?)\"");
        Matcher matcher = pattern.matcher(content.toString());

        int halted = 0, total = 0;
        while (matcher.find()) {
            total++;
            String prog = matcher.group(1).trim().toUpperCase();
            if (prog.equals("HALT")) halted++;
        }

        System.out.println(halted + " de " + total + " programas halting (" + size + ")");
    }
}
