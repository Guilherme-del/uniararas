import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router'; // Importe o Router
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})

export class FuncionarioService {
  // ==> Uri da api (Back-End)
  uri = 'http://localhost:8000/api';

  // Injetando o Router no construtor
  constructor(private http: HttpClient, private router: Router) { }

  // Método responsável por adicionar um novo 'Funcionário' btn 'Adicionar Funcionário':
  adicionarFuncionario(nomeFuncionario, cargo, numeroIdentificador) {
    const objFuncionario = {
      nomeFuncionario,
      cargo,
      numeroIdentificador
    };

    // ==> (POST - URL no Back-End:): http://localhost:8000/api/funcionarios
    this.http.post(`${this.uri}/funcionarios`, objFuncionario).subscribe({
      next: () => {
        this.router.navigate(['/funcionario']); // Redireciona para a rota /funcionario
      },
      error: (err) => {
        console.error('Erro ao adicionar funcionário:', err);
      }
    });
  }

  /**
   * Método responsável por selecionar todos os 'Funcionários'
   */
  getFuncionarios() {
    // ==> (GET - Url no Back-End): http://localhost:8000/api/funcionarios
    return this.http.get(`${this.uri}/funcionarios`);
  }

    // Método para excluir um funcionário
    excluirFuncionario(id: string): Observable<void> {
      return this.http.delete<void>(`${this.uri}/funcionarios/${id}`);
    }
}