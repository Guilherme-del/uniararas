select c.tipocontrato, f.nome from fornecedores f 
		 join contratos c on c.codigofornecedor = f.codigofornecedor;
