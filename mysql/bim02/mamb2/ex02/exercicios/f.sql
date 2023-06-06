SELECT diretor,nomeEscola
FROM escola AS escolas
JOIN Departamento AS dep ON escolas.codEscola = dep.codEscola
JOIN Disciplina AS disc ON dep.codDepartamento = disc.codDepartamento
JOIN Turmas AS turma ON disc.descDisciplina = turma.codDisciplina
