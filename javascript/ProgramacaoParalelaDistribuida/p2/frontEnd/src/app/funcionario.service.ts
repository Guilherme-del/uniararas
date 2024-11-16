import { Injectable } from "@angular/core";
import { HttpClient } from "@angular/common/http";
import { Router } from "@angular/router";
import { Observable } from "rxjs";

import Funcionario from './Funcionario';

@Injectable({
  providedIn: "root",
})
export class FuncionarioService {
  // ==> Uri da api (Back-End)
  uri = "http://localhost:8000/api";

  // Injetando o Router no construtor
  constructor(private http: HttpClient, private router: Router) {}

  // Método responsável por adicionar um novo 'Funcionário' btn 'Adicionar Funcionário':
  /**
   * Método para adicionar um novo funcionário.
   * Agora retorna um Observable para que possamos usar o subscribe.
   */
  adicionarFuncionario(nomeFuncionario: string, cargo: string, numeroIdentificador: string): Observable<Funcionario> {
    const novoFuncionario = { nomeFuncionario, cargo, numeroIdentificador };
    return this.http.post<Funcionario>(`${this.uri}/funcionarios`, novoFuncionario);
  }

  /**
   * Método responsável por selecionar todos os 'Funcionários'
   */
  getFuncionarios() {
    // ==> (GET - Url no Back-End): http://localhost:8000/api/funcionarios
    return this.http.get(`${this.uri}/funcionarios`);
  }
  // Método para buscar um funcionário por ID
  getFuncionarioById(id: string): Observable<Funcionario> {
    return this.http.get<Funcionario>(`${this.uri}/funcionarios/${id}`);
  }

  // Método para atualizar um funcionário
  updateFuncionario(
    id: string,
    funcionario: Funcionario
  ): Observable<Funcionario> {
    return this.http.put<Funcionario>(
      `${this.uri}/funcionarios/${id}`,
      funcionario
    );
  }
  // Método para excluir um funcionário
  excluirFuncionario(id: string): Observable<void> {
    return this.http.delete<void>(`${this.uri}/funcionarios/${id}`);
  }
}
