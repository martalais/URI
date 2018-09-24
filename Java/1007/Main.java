// Uri 1007 - Diferença
// Marta Laís

import java.io.IOException;
import java.util.Scanner;

public class Main {

	public static void main (String[] args) throws IOException {
		
        Scanner sc = new Scanner(System.in);
        int A,B,C,D;

        A = sc.nextInt();
        B = sc.nextInt();
        C = sc.nextInt();
        D = sc.nextInt();

        int media = (A * B - C * D);

        System.out.printf("DIFERENCA = %d\n", media);
	}
}