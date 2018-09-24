// Uri 1002 - Área do Círculo
// Marta Laís

import java.io.IOException;
import java.util.Scanner;
import java.lang.Math;

public class Main {

	public static void main (String[] args) throws IOException {
		
        Scanner sc = new Scanner(System.in);

        double raio = sc.nextDouble();
        double area = 3.14159 * (raio * raio);

        System.out.printf("A=%.4f\n", area);
	}
}
