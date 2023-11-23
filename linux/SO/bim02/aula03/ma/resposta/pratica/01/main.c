/*
Em sistemas operacionais baseados em Unix/Linux,
pode-se usar a função fork() para criar um processo filho e execvp() para
executar o comando desejado.
*/

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>

int main(int argc, char *argv[])
{
    if (argc < 2)
    {
        fprintf(stderr, "Uso: %s <diretório>\n", argv[0]);
        exit(EXIT_FAILURE);
    }

    pid_t pid = fork();

    if (pid == -1)
    {
        perror("Erro ao criar processo filho");
        exit(EXIT_FAILURE);
    }

    if (pid == 0)
    { // Código executado pelo processo filho
        if (chdir(argv[1]) == -1)
        {
            perror("Erro ao executar o comando cd");
            exit(EXIT_FAILURE);
        }

        // Se você quiser realizar mais ações no processo filho após o cd, adicione-as aqui

        exit(EXIT_SUCCESS);
    }
    else
    { // Código executado pelo processo pai
        // Aguardar o processo filho terminar
        int status;
        waitpid(pid, &status, 0);

        if (WIFEXITED(status))
        {
            printf("Processo filho terminou com código de saída %d\n", WEXITSTATUS(status));
        }
        else
        {
            printf("Processo filho terminou anormalmente\n");
        }
    }

    return 0;
}
