SELECT descDepartamento,Count(descDisciplina)
FROM Departamento AS dep
JOIN Disciplina AS disc ON dep.codDepartamento = disc.codDepartamento
group by descDepartamento
