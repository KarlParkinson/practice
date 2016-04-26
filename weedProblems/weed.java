import java.io.*;

public class weed {

    public static String reverse(String s) {
	int i = 0;
	int j = s.length() - 1;
	char[] str = s.toCharArray();
	while (i <= j) {
	    char temp = str[i];
	    str[i] = str[j];
	    str[j] = temp;
	    i++;
	    j--;
	}
	return new String(str);
    }

    public static int fib(int n) {
	return n <= 1 ? 1 : fib(n-1) + fib(n-2);
    }

    public static void multTable() {
	for (int i = 1; i <= 12; i++) {
	    for (int j = 1; j <= 12; j++) {
		System.out.printf("%4d", i*j);
	    }
	    System.out.println();
	}
    }

    public static void sumFile(String name) throws IOException {
	int total = 0;
	BufferedReader in = new BufferedReader(new FileReader(name));
	for (String s = in.readLine(); s != null; s = in.readLine()) {
	    total += Integer.parseInt(s);
	}
	System.out.println(total);
    }

    public static void printOdds() {
	for (int i = 1; i < 100; i++) {
	    if (i % 2 == 1) {
		System.out.println(i);
	    }
	}
    }

    public static void main(String[] args) {
	//System.out.println(reverse("karl"));
	//System.out.printf("%d\n", fib(5));
	//multTable();
	try {
	    sumFile("test_file_sum.txt");
	} catch (Exception e) {
	    e.printStackTrace();
	}
	System.out.println();
	printOdds();
    }
}
