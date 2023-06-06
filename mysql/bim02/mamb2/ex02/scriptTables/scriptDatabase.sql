create database grupo7;
use grupo7;


CREATE TABLE `Departamento` (
  `codDepartamento` int NOT NULL AUTO_INCREMENT,
  `descDepartamento` varchar(45) NOT NULL,
  `codEscola` int NOT NULL,
  PRIMARY KEY (`codDepartamento`),
  KEY `fk_Departamento_1_idx` (`codEscola`),
  CONSTRAINT `codEscola` FOREIGN KEY (`codEscola`) REFERENCES `escola` (`codEscola`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `Disciplina` (
  `codDisciplina` int NOT NULL AUTO_INCREMENT,
  `descDisciplina` varchar(45) NOT NULL,
  `codDepartamento` int NOT NULL,
  PRIMARY KEY (`codDisciplina`),
  KEY `fk_Disciplina_1_idx` (`codDepartamento`),
  CONSTRAINT `fk_Disciplina_1` FOREIGN KEY (`codDepartamento`) REFERENCES `Departamento` (`codDepartamento`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `escola` (
  `codEscola` int NOT NULL AUTO_INCREMENT,
  `nomeEscola` varchar(45) NOT NULL,
  PRIMARY KEY (`codEscola`),
  UNIQUE KEY `codEscola_UNIQUE` (`codEscola`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `Professor` (
  `codProfessor` int NOT NULL AUTO_INCREMENT,
  `nomeProfessor` varchar(45) NOT NULL,
  `codTurma` int NOT NULL,
  `codDepartamento` int NOT NULL,
  PRIMARY KEY (`codProfessor`),
  KEY `fk_Professor_1_idx` (`codTurma`),
  KEY `fk_Professor_2_idx` (`codDepartamento`),
  CONSTRAINT `fk_Professor_1` FOREIGN KEY (`codTurma`) REFERENCES `Turmas` (`codDisciplina`),
  CONSTRAINT `fk_Professor_2` FOREIGN KEY (`codDepartamento`) REFERENCES `Departamento` (`codDepartamento`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `Turmas` (
  `codTurma` int unsigned NOT NULL AUTO_INCREMENT,
  `descTurma` varchar(45) NOT NULL,
  `codDisciplina` int NOT NULL,
  PRIMARY KEY (`codTurma`),
  KEY `fk_Turmas_1_idx` (`codDisciplina`),
  CONSTRAINT `fk_Turmas_1` FOREIGN KEY (`codDisciplina`) REFERENCES `Disciplina` (`codDisciplina`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
