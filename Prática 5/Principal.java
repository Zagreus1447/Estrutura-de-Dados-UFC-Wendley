/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package pratica51;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class Principal {

    /**
     * @param args the command line arguments
     */
public static void leitor(String path) throws IOException{
        BufferedReader buffRead = new BufferedReader(new FileReader(path));
        String linha = "";
            while (true){
                if (linha != null){
                    System.out.println(linha);
                }
            else{
                linha = buffRead.readLine();    
                break;
                  }   
            buffRead.close();
            }
    }
public static void escritor(String path) throws IOException{
    BufferedWriter buffWrite = new BufferedWriter(new FileWriter(path));
        String linha = "";
        Scanner in = new Scanner(System.in);
    System.out.println("Escreve Algo: ");
    linha = in.nextLine();
    buffWrite.append(linha + "\n");
    buffWrite.close();
    
}    
public static void main(String args[]) throws IOException{
    String path = "c:\\Arquivo2.txt";
    
    escritor(path);
    leitor(path);
}
}
