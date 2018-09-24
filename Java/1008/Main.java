// Uri 1008 - Salário
// Marta Laís

import java.io.IOException;
import java.util.Scanner;

public class Main {

	public static void main (String[] args) throws IOException {
		
        Scanner sc = new Scanner(System.in);
        
        int A = sc.nextInt();
        int B = sc.nextInt();
        double C = sc.nextDouble();

        System.out.printf("NUMBER = %d\n", A);
        System.out.printf("SALARY = U$ %.2f\n", (B * C));
	}
}