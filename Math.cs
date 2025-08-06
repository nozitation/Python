using System;

public class System_ {
    static class Math {
        public const double E = 2.718281828459045;
        public const double PI = 3.141592653589793;
        public static double Pow(double bs, int ex) {
            double result = 1;
            for (int i = 0; i < ex; i++) {
                result *= bs;
            }
            return result;
    }
        public static double Max(double a, double b) {
            return a > b ? a: b;
        }
        public static double Min(double a, double b) {
            return a > b ? b : a;
        }
        public static double Abs(double a) {
            if(a + a < a) {
                return -a;
            }
            else {
                return a;
            }
        }
        public static double sqrt(double n) {
            double result = 1;
            // x = 1
            // repeat 10 times:  x = (x + n / x) / 2
            // return x.
            for (int i=0; i<10; i++) {
                result = (result + n / result) / 2;
            }
            return result;
            
        }
        public static int Fac(int bs) {
        int result = 1;
        for (int i = 1; i <= bs; i++) {
            result *= i;
        }
        return result;
    }
        public static double Sin(double theta) {
        double rad = theta * Math.PI / 180; // degrees to radians
        return rad - (Pow(rad, 3) / Fac(3)) + (Pow(rad, 5) / Fac(5)) - (Pow(rad, 7) / Fac(7));
    }
        public static double Cos(double theta) {
        double rad = theta * Math.PI / 180; // degrees to radians
        return 1 - (Pow(rad, 2) / Fac(2)) + (Pow(rad, 4) / Fac(4)) - (Pow(rad, 6) / Fac(6));
    }
    }
    static void Main(string[] args) {
        Console.WriteLine($"E: {Math.E}");
        Console.WriteLine($"PI: {Math.PI}");
        Console.WriteLine($"Max one and two: {Math.Max(1, 2)}");
        Console.WriteLine($"Min one and two: {Math.Min(1, 2)}");
        Console.WriteLine($"Abs of negative two: {Math.Abs(-2)}");
        Console.WriteLine($"Sin of 60 degrees: {Math.Sin(60)}");
        Console.WriteLine($"Cos of 60 degrees: {Math.Cos(60)}");
        Console.WriteLine($"Square root of two: {Math.sqrt(2)}");
        

    }
}