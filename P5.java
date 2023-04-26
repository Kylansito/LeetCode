//Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

import java.util.Scanner;

public class P5 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        char c;
        do{
            P5 s = new P5();
            System.out.println("Insert number: ");
            System.out.println(s.addDigits(sc.nextInt()));
            System.out.println("Do you want to continue? (y/n)");
            c = sc.next().charAt(0);
        }while(c != 'n');
    }
    public int addDigits(int num) {
        if (num < 10) return num;
        int sum = 0;
        while (num > 0) {
            int digit = num % 10;
            sum += digit;
            num /= 10;
        }
        return addDigits(sum);
    }
}
