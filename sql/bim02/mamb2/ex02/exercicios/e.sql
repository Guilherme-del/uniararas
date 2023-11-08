SELECT nomeProfessor,descDepartamento FROM Professor AS Prof
	JOIN Departamento AS dep ON Prof.codDepartamento = dep.codDepartamento