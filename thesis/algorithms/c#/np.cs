using System;
using System.IO;
using System.Collections.Generic;

class Np
{
    static void Main(string[] args)
    {
        string tamanho = args.Length > 0 ? args[0] : "small";
        string path = $"datasets/{tamanho}/factoring.json";

        if (!File.Exists(path))
        {
            Console.WriteLine($"Arquivo não encontrado: {path}");
            return;
        }

        string json = File.ReadAllText(path);
        json = json.Trim().TrimStart('[').TrimEnd(']');
        string[] parts = json.Split(',');

        int count = 0;
        foreach (string part in parts)
        {
            if (int.TryParse(part.Trim(), out int n))
            {
                for (int i = 2; i * i <= n; i++)
                {
                    if (n % i == 0)
                    {
                        count++;
                        break;
                    }
                }
            }
        }

        Console.WriteLine($"Fatorados {count} números do dataset {tamanho}.");
    }
}
