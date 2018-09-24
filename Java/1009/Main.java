// Uri 1009 - Salário com Bônus
// Marta Laís

import java.io.IOException;
import java.util.Scanner;

public class Main {

	public static void main (String[] args) throws IOException {
		
        Scanner sc = new Scanner(System.in);
        
        String Nome = sc.next();
        float SalarioFixo = sc.nextFloat();
        float Vendas = sc.nextFloat();

        System.out.printf("TOTAL = R$ %.2f\n", SalarioFixo + (Vendas * 0.15));
	}
}