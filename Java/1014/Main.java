// Uri 1013 - O Maior
// Marta Laís

import java.io.IOException;
import java.util.Scanner;

public class Main {

	public static void main (String[] args) throws IOException {
		
        Scanner sc = new Scanner(System.in);
        
        double Distancia = sc.nextDouble();
        double Litros = sc.nextDouble();

        double Total = Distancia / Litros;

        System.out.printf("%.3f km/l\n", Total);
	}
}