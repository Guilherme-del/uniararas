import java.io.*;
import java.nio.file.*;

public class Np {
    public static boolean hasFactor(int n) {
        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) return true;
        }
        return false;
    }

    public static void main(String[] args) {
        String tamanho = args.length > 0 ? args[0] : "small";
        String datasetPath = "datasets/" + tamanho + "/factoring.json";

        try {
            String content = new String(Files.readAllBytes(Paths.get(datasetPath))).trim();
            // Remove colchetes e espaços extras
            content = content.replace("[", "").replace("]", "").replaceAll("\\s", "");

            if (content.isEmpty()) {
                System.out.printf("Nenhum número no dataset %s.%n", tamanho);
                return;
            }

            String[] parts = content.split(",");
            int count = 0;
            for (String part : parts) {
                int n = Integer.parseInt(part);
                if (hasFactor(n)) count++;
            }

            System.out.printf("Fatorados %d números do dataset %s.%n", count, tamanho);

        } catch (IOException e) {
            System.out.println("Erro ao ler o arquivo: " + e.getMessage());
        } catch (NumberFormatException e) {
            System.out.println("Erro ao converter número: " + e.getMessage());
        }
    }
}
