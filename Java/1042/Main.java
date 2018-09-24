import java.io.IOException;
import java.util.Scanner;
 
public class Main {
 
    public static void main(String[] args) throws IOException {
          
        int Minimo1, Minimo2 = 0, Minimo3 = 0;

        Scanner sc = new Scanner(System.in);

        int X = sc.nextInt();
        int Y = sc.nextInt();
        int Z = sc.nextInt();
        
        Minimo1 = Math.min(X, Math.min(Y, Z));

        if (Minimo1 == X) {
        Minimo2 = Math.min(Y, Z);
        Minimo3 = Math.max(Y, Z);
        }
        
        if (Minimo1 == Y) {
        Minimo2 = Math.min(X, Z);
        Minimo3 = Math.max(X, Z);
        }
        
        if (Minimo1 == Z) {
        Minimo2 = Math.min(X, Y);
        Minimo3 = Math.max(X, Y);
        }

        System.out.print(Minimo1+"\n"+Minimo2+"\n"+Minimo3+"\n\n");
        System.out.print(X+"\n" +Y+"\n" +Z+"\n");
    
    }
}