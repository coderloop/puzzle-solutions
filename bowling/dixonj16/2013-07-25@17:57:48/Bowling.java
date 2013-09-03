import java.io.FileReader;
import java.io.BufferedReader;

public class Bowling {
  public static void main(String[] args) throws Exception {
    final BufferedReader br = new BufferedReader(new FileReader(args[0]));
    int score = 0, m1 = 1, m2 = 1, f = 0;
    while (br.ready()) {
      byte[] line = br.readLine().getBytes();
      for (int i = 0; i < line.length; i+=2) {
        final byte b = line[i];
        f++;
        if (b == 'X') {
          score += 10 * m1;
          m1 += (m1 == m2 && f < 10) ? 1 : 0;
          m2 += (m2 < 2 && f < 10) ? 1 : 0;
          if (f >= 10) {
            m1 = (m2 != 1) ? m2 : 1;
            m2 -= (m2 != 1) ? 1 : 0;
          }
        } else {
          final int b1 = b - 48;
          if (line.length <= i+2) {
            score += b1*m1;
            continue;
          }
          int b2 = (line[i+2] == '/') ? 10-b1 : line[i+2]-48;
          if (b2 >= 0 && b2 <= 10) i+=2;
          else b2 = 0;
          score += b1*m1 + b2*m2;
          m1 = (b1+b2 == 10 && f < 10) ? 2 : 1; m2 = 1;
        }
      }
      System.out.println(score);
      score = 0; m1 = 1; m2 = 1; f = 0;
    }
  }
}