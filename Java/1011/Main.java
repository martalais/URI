// Uri 1011 - Esfera
// Marta Laís

import java.io.IOException;
import java.util.Scanner;

public class Main {

	public static void main (String[] args) throws IOException {
		
        Scanner sc = new Scanner(System.in);
        
        double Raio = sc.nextDouble();

        double Total = (4.0/3.0) * (3.14159 * (Raio * Raio * Raio));

        System.out.printf("VOLUME = %.3f\n", Total);
	}
}