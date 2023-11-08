import java.util.Scanner;

/**
 *
 * @author user_le2_17
 */
public class Main {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
          float cont = 0;
          float[] Array = new float[3];
    
          for(int i = 0; i < Array.length; i++){
              Array[i] = sc.nextInt();
          }
          for(int i = 0; i<Array.length; i++){
              cont = cont + Array[i];
          }      
          float media = cont/Array.length;
          System.out.println("Media desses 3 numeros são: " + media);
          
          float DivMedia = cont/media;
          System.out.println("Divisão da soma pela media: " + DivMedia);
        }      
   }
}