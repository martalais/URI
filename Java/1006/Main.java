// Uri 1006 - Média 2
// Marta Laís

import java.io.IOException;
import java.util.Scanner;

public class Main {

	public static void main (String[] args) throws IOException {
		
        Scanner sc = new Scanner(System.in);
        double A,B,C;

        A = sc.nextDouble();
        B = sc.nextDouble();
        C = sc.nextDouble();
        
        double media = ((A * 2.0) + (B * 3.0) + (C * 5.0)) / 10.0;

        System.out.printf("MEDIA = %.1f\n", media);
	}
}