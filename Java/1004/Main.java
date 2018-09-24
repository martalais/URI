// Uri 1004 - Produto Simples
// Marta Laís

import java.io.IOException;
import java.util.Scanner;

public class Main {

	public static void main (String[] args) throws IOException {
		
        Scanner sc = new Scanner(System.in);
        int A,B;

        A = sc.nextInt();
        B = sc.nextInt();

        System.out.println("PROD = " + (A * B));
	}
}