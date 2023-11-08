SELECT nomeProfessor,descDisciplina FROM Professor AS Prof
	JOIN Departamento AS dep ON Prof.codDepartamento = dep.codDepartamento
    JOIN Disciplina AS disc ON dep.descDepartamento = disc.codDisciplina