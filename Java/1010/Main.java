// Uri 1009 - Salário com Bônus
// Marta Laís

import java.io.IOException;
import java.util.Scanner;

public class Main {

	public static void main (String[] args) throws IOException {
		
        Scanner sc = new Scanner(System.in);
        
        int Prod1 = sc.nextInt();
        int Quant1 = sc.nextInt();
        float Preco1 = sc.nextFloat();
        float Total1 = Quant1 * Preco1;

        int Prod2 = sc.nextInt();
        int Quant2 = sc.nextInt();
        float Preco2 = sc.nextFloat();
        float Total2 = Quant2 * Preco2;

        System.out.printf("VALOR A PAGAR: R$ %.2f\n", Total1 + Total2);
	}
}
