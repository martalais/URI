// Uri 1005 - Média 1
// Marta Laís

import java.io.IOException;
import java.util.Scanner;

public class Main {

	public static void main (String[] args) throws IOException {
		
        Scanner sc = new Scanner(System.in);
        double A,B;

        A = sc.nextDouble();
        B = sc.nextDouble();

        double media = ((A * 3.5) + (B * 7.5)) / 11.0;

        System.out.printf("MEDIA = %.5f\n", media);
	}
}