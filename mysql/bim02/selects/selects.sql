/*Quero saber quais os alunos tem aula com quais professores
*/

SELECT * FROM Pessoa as Pessoinha
		inner join Aluno on Pessoinha.cpf = Aluno.cpf
        inner join Matricula_Disciplina as Md on Md.ra_aluno = Aluno.ra
        inner join Disciplina as dcplina on Md.cod_disciplina = dcplina.codigo
        inner join Professor as Prof on dcplina.cod_prof = Prof.codigo
        inner join Pessoa as PessoinhaSegunda on PessoinhaSegunda.cpf = Pessoinha.cpf;

/*Quero saber quantas disciplinas cada professor ministra nome seguida do numero*/

select Pessoinha.nome as NomeProfessor,count(Disciplina.codigo) as contadorDeMaterias from Disciplina				 
				inner join Professor as Prof on Prof.codigo = Disciplina.cod_prof
                inner join Pessoa as Pessoinha on Pessoinha.cpf = Prof.cpf
                group by Pessoinha.nome;