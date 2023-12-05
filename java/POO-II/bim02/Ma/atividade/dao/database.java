package dao;

import model.Empresa;

public interface database {
    void delete(String nome);
    void update(Empresa e);
    void add(Empresa e);
    Empresa get(String nome);
}
