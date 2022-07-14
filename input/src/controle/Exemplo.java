
package controle;

import entidades.ExemploEntidade;


public class Exemplo {
    public static void main(String args[]) {
        ExemploEntidade entidade = new ExemploEntidade("Jeremias", 37);
        
        System.out.println(entidade.toString());
    }
}
