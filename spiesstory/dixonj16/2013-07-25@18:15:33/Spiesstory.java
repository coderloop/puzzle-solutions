import java.io.*;

class Spiesstory {
  public static void main(String[] args) throws Exception {
    final BufferedReader br = new BufferedReader(new FileReader(args[0]));
    int cypher = Integer.parseInt(br.readLine()) % 26;
    cypher = cypher >= 0 ? 26 - cypher : Math.abs(cypher);

    // A-Z => 65 - 90
    // a-Z => 97 - 122
    int c;
    while ((c = br.read()) != -1) {
      if (c >= 97 && c <= 122) {
        c = ((c - 97) + cypher) % 26 + 97;
      }
      else if (c >= 65 && c <=90) {
        c = ((c - 65) + cypher) % 26 + 65;
      }
      System.out.write((char)c);
    }
  }
}
