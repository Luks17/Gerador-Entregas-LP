
package entidades;


public class ExemploEntidade {
    String nome;
    Integer idade;
    
    public ExemploEntidade(String nome, int idade) {
        this.nome = nome;
        this.idade = idade;
    }
    
    @Override
    public String toString() {
        return "Nome: " + this.nome + "\nIdade: " + this.idade.toString();
    }
}
