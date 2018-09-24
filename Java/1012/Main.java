// Uri 1012 - Área
// Marta Laís

import java.io.IOException;
import java.util.Scanner;

public class Main {

	public static void main (String[] args) throws IOException {
		
        Scanner sc = new Scanner(System.in);
        
        double A = sc.nextDouble();
        double B = sc.nextDouble();
        double C = sc.nextDouble();
        
        double Triangulo = (A * C) / 2.0;
        double Circulo = 3.14159 * (C * C);
        double Trapezio = ((A + B) * C) / 2.0;
        double Quadrado = B * B;
        double Retangulo = A * B;

        System.out.printf("TRIANGULO: %.3f\n", Triangulo);
        System.out.printf("CIRCULO: %.3f\n", Circulo);
        System.out.printf("TRAPEZIO: %.3f\n", Trapezio);
        System.out.printf("QUADRADO: %.3f\n", Quadrado);
        System.out.printf("RETANGULO: %.3f\n", Retangulo);
        
	}
}