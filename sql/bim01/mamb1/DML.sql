insert into estados(NomeEstado) values("SP");
select * from estados;
insert into afetados(nome, CodEstado, ano, cpfPessoa) values("joão", 1, "2009", "123.456.897-x");
insert into pessoas(CPF, nome, CodEstado) values("123.456.789.-x", "ricardo", 1);
insert into afetados(nome, CodEstado, ano, cpfPessoa) values("ricardo", 1, "2009", "123.456.789.-x");

UPDATE `ods13`.`pessoas` SET `CPF` = '123.456.789-x', `nome` = 'gomes' WHERE (`CPF` = '123.456.789.-x');
insert into estados(NomeEstado) values("RJ");
select * from estados
DELETE FROM `ods13`.`estados` WHERE (`CodEstado` = '2');
