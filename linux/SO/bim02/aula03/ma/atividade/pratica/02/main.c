#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>
#include <sys/types.h>

void handle_sigusr1(int signo) {
    if (signo == SIGUSR1) {
        printf("Algo não está certo...\n");
    }
}

void handle_sigkill(int signo) {
    if (signo == SIGKILL) {
        printf("Recebido SIGKILL. Terminando...\n");
        exit(EXIT_SUCCESS);
    }
}

int main() {
    pid_t pid = fork();

    if (pid == -1) {
        perror("Erro ao criar processo filho");
        exit(EXIT_FAILURE);
    }

    if (pid == 0) { // Código executado pelo processo filho
        signal(SIGUSR1, handle_sigusr1);
        signal(SIGKILL, handle_sigkill);

        while (1) {
            printf("Esperando...\n");
            sleep(1);
        }
    } else { // Código executado pelo processo pai
        sleep(15); // Espera 15 segundos

        printf("Enviando SIGUSR1 para o processo filho\n");
        kill(pid, SIGUSR1);

        sleep(35); // Espera mais 35 segundos

        printf("Enviando SIGKILL para o processo filho\n");
        kill(pid, SIGKILL);

        wait(NULL); // Espera pelo processo filho terminar
    }

    return 0;
}
