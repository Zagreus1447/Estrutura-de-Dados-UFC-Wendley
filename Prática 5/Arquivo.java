package pratica5;

        import java.io.FileWriter; //adicionar pacote acima
        import java.io.IOException;
        import java.io.PrintWriter;
        import java.util.Scanner;
/**
 *
 * @author azael
 */
public class Arquivo {

    public static void main(String[] args) throws IOException {    
        Scanner ler = new Scanner(System.in);
        int i, n;
        
        System.out.printf("Informe o número para a tabuada:\n");
        n = ler.nextInt();    
        
        FileWriter arq = new FileWriter("c:\\Tabuada.txt", true); //verificar permissão    
        PrintWriter gravarArq = new PrintWriter(arq);    
        
        gravarArq.printf("+--Resultado--+%n");    
        for (i=1; i<=10; i++) {        
            gravarArq.printf("| %2d X %d = %2d |%n", i, n, (i*n));
        }    
        gravarArq.printf("+-------------+%n");    
        arq.close();    
        System.out.printf("\nTabuada do %d foi gravada com sucesso em \"d:\\Tabuada.txt\".\n", n);}
    
}
