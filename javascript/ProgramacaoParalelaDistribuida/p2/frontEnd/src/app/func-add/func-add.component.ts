import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { FuncionarioService } from '../funcionario.service';
import { Router } from '@angular/router';  // Importando o Router para navegação
import Swal from 'sweetalert2';  // Importando o SweetAlert2

@Component({
  selector: 'app-func-add',
  templateUrl: './func-add.component.html',
  styleUrls: ['./func-add.component.css']
})
export class FuncAddComponent implements OnInit {

  adicionarFuncionarioForm: FormGroup;

  constructor(
    private formBuilder: FormBuilder, 
    private funcionarioService: FuncionarioService,
    private router: Router  // Injetando o Router
  ) {
    this.createForm();
  }

  /**
   * Método responsável por tratar as validações do Form que criará um novo Funcionário:
   */
  createForm() {
    this.adicionarFuncionarioForm = this.formBuilder.group({
      nomeFuncionario: ['', Validators.required],
      cargo: ['', Validators.required],
      numeroIdentificador: ['', Validators.required]
    });
  }

  /**
   * Método responsável por adicionar um novo 'Funcionário' com ação do btn 'Adicionar Funcionário':
   */
  adicionarFuncionario() {
    if (this.adicionarFuncionarioForm.valid) {
      // Pegando os valores do formulário
      const { nomeFuncionario, cargo, numeroIdentificador } = this.adicionarFuncionarioForm.value;
      
      // Chamando o serviço para adicionar o funcionário
      this.funcionarioService.adicionarFuncionario(nomeFuncionario, cargo, numeroIdentificador).subscribe(
        (response) => {
          // Exibe o Swal de sucesso
          Swal.fire({
            icon: 'success',
            title: 'Funcionário adicionado!',
            text: 'O funcionário foi adicionado com sucesso.',
            confirmButtonText: 'Fechar'
          }).then(() => {
            // Redireciona para a página de listagem de funcionários após o sucesso
            this.router.navigate(['/funcionario']);
          });
        },
        (error) => {
          // Exibe o Swal de erro
          Swal.fire({
            icon: 'error',
            title: 'Erro!',
            text: 'Não foi possível adicionar o funcionário. Tente novamente.',
            confirmButtonText: 'Fechar'
          });
          console.error('Erro ao adicionar funcionário', error);
        }
      );
    } else {
      // Exibe o Swal de erro se o formulário não for válido
      Swal.fire({
        icon: 'warning',
        title: 'Campos obrigatórios!',
        text: 'Preencha todos os campos antes de adicionar.',
        confirmButtonText: 'Fechar'
      });
    }
  }

  ngOnInit() {
  }
}
