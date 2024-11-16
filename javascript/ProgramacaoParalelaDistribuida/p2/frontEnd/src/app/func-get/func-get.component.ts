import { Component, OnInit } from '@angular/core';
import Funcionario from '../Funcionario';
import { FuncionarioService } from '../funcionario.service';
import Swal from 'sweetalert2';  // Importando SweetAlert2

@Component({
  selector: 'app-func-get',
  templateUrl: './func-get.component.html',
  styleUrls: ['./func-get.component.css']
})
export class FuncGetComponent implements OnInit {

  funcionarios: Funcionario[] = [];

  constructor(private funcionarioService: FuncionarioService) { }

  ngOnInit() {
    this.funcionarioService
      .getFuncionarios()
      .subscribe((data: Funcionario[]) => {
        this.funcionarios = data;
      });
  }

  // Método para excluir um funcionário com confirmação
  excluirFuncionario(id: string) {
    Swal.fire({
      title: 'Tem certeza?',
      text: 'Você não poderá reverter essa ação!',
      icon: 'warning',
      showCancelButton: true,
      confirmButtonText: 'Sim, excluir!',
      cancelButtonText: 'Cancelar'
    }).then((result) => {
      if (result.value) { // Verificando se a confirmação foi dada
        // Chama o serviço para excluir o funcionário
        this.funcionarioService.excluirFuncionario(id).subscribe({
          next: () => {
            Swal.fire(
              'Excluído!',
              'O funcionário foi excluído com sucesso.',
              'success'
            );
            // Recarrega a lista de funcionários
            this.funcionarios = this.funcionarios.filter(func => func._id !== id);
          },
          error: (err) => {
            Swal.fire(
              'Erro!',
              'Ocorreu um erro ao excluir o funcionário.',
              'error'
            );
            console.error('Erro ao excluir funcionário:', err);
          }
        });
      }
    });
  }
}
