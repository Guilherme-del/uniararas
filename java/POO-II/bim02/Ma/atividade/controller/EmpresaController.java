package controller;

import model.Empresa;
import model.EmpInovacao;
import model.EmpresaInfra;
import dao.empresaDAO;
import dao.database;

public class EmpresaController {
    public static void adicionarEmpresa(String nome, String descricao, int func, int op) {
        Empresa input = null;
        if (op == 1) {
            input = new EmpresaInfra();
            input.setNome(nome);
            input.setDescricao(descricao);
            input.setTotalFuncionarios(func);
        } else if (op == 2) {
            input = new EmpInovacao();
            input.setNome(nome);
            input.setDescricao(descricao);
            input.setTotalFuncionarios(func);
        }

        empresaDAO.getInstancia().add(input);

    }
    public static void vizualizarEmpresa(String nome) {
        database db = empresaDAO.getInstancia();

        Empresa e = db.get(nome);

        System.out.println("Nome: " + e.getNome());
        System.out.println("Descricao: " + e.getDescricao());
        System.out.println("Total funcionarios: " + e.getTotalFuncionarios());
    }
    public static void deleteEmpresa(String nome) {
        database db = empresaDAO.getInstancia();

        Empresa e = db.get(nome);

        db.delete(nome);
        System.out.println("Aluno deletado com sucesso!");
    }


    public static void updateEmpresa(String nome,String descricao,int func) {
        database db = empresaDAO.getInstancia();

        Empresa e = db.get(nome);

        e.setNome(nome);
        e.setDescricao(descricao);
        e.setTotalFuncionarios(func);

        db.update(e);

        System.out.println("Empresa atualizada com sucesso!");
    }
}
