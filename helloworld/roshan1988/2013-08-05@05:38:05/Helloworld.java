import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

class Helloworld {		
  public static void main(String[] args) {
  	try {
	BufferedReader br = new BufferedReader(new FileReader(args[0]));
    br.readLine();
		} catch (IOException e) {
			e.printStackTrace();
		}
    System.out.println("Hello World!");
  }
}
