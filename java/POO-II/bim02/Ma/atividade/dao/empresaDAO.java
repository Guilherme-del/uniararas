package dao;

import model.Empresa;

import java.util.ArrayList;

public class empresaDAO implements database{

    static private ArrayList<Empresa> db = new ArrayList<>();
    static private empresaDAO instancia = null;

    //Construtor de um singleton é privado!
    private empresaDAO() { }

    static public empresaDAO getInstancia() {

        if (instancia == null)
            instancia = new empresaDAO();

        return instancia;
    }

    @Override
    public void delete(String nome) {
        db.removeIf((a) -> a.getNome().equals(nome));
        System.out.println("Empresa deletada com sucesso!");
    }

    @Override
    public void update(Empresa e) {

        Empresa resultado = this.get(e.getNome());

        resultado.setNome(e.getNome());
        resultado.setDescricao(e.getDescricao());
        resultado.setTotalFuncionarios(e.getTotalFuncionarios());

        System.out.println("Empresa atualizada com sucesso!");
    }

    @Override
    public void add(Empresa e) {
        db.add(e);
        System.out.println("Empresa adicionada com sucesso!");
    }

    @Override
    public Empresa get(String nome) {
            return db.stream().filter(e -> e.getNome().equals(nome)).findFirst().orElse(null);
    }
}
