import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { FuncionarioService } from '../funcionario.service';
import Swal from 'sweetalert2';

@Component({
  selector: 'app-func-edit',
  templateUrl: './func-edit.component.html',
  styleUrls: ['./func-edit.component.css']
})
export class FuncEditComponent implements OnInit {

  funcionarioId: string; // Variável para armazenar o ID do funcionário
  editForm: FormGroup; // Formulário reativo

  constructor(
    private route: ActivatedRoute, // Para capturar o ID da URL
    private router: Router, // Para redirecionamento após edição
    private funcionarioService: FuncionarioService, // Serviço de funcionários
    private fb: FormBuilder // Para criação do formulário reativo
  ) { }

  ngOnInit(): void {
    // Captura o ID do funcionário da URL
    this.funcionarioId = this.route.snapshot.paramMap.get('id');

    // Inicializa o formulário reativo
    this.editForm = this.fb.group({
      nomeFuncionario: ['', Validators.required],
      cargo: ['', Validators.required],
      numeroIdentificador: ['', Validators.required]
    });

    // Chama o serviço para buscar o funcionário por ID
    this.funcionarioService.getFuncionarioById(this.funcionarioId).subscribe(
      (funcionario) => {
        // Preenche o formulário com os dados do funcionário
        this.editForm.patchValue({
          nomeFuncionario: funcionario.nomeFuncionario,
          cargo: funcionario.cargo,
          numeroIdentificador: funcionario.numeroIdentificador
        });
      },
      (error) => {
        // Caso ocorra um erro ao buscar os dados
        Swal.fire('Erro!', 'Não foi possível carregar os dados do funcionário.', 'error');
        console.error('Erro ao carregar dados do funcionário', error);
      }
    );
  }

  // Método para enviar o formulário
  onSubmit(): void {
    if (this.editForm.valid) {
      const updatedFuncionario = this.editForm.value; // Dados do formulário

      // Chama o serviço para atualizar o funcionário
      this.funcionarioService.updateFuncionario(this.funcionarioId, updatedFuncionario).subscribe(
        () => {
          // Sucesso! Redireciona para a lista de funcionários
          Swal.fire('Sucesso!', 'Funcionário atualizado com sucesso!', 'success');
          this.router.navigate(['/funcionario']);
        },
        (error) => {
          // Caso ocorra um erro ao atualizar
          Swal.fire('Erro!', 'Ocorreu um erro ao atualizar o funcionário.', 'error');
          console.error('Erro ao atualizar funcionário', error);
        }
      );
    }
  }
}
