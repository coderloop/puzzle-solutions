import java.io.FileReader;
import java.io.BufferedReader;

public class Netconnections {

  private static int[] array;

  public static void main(String[] args) throws Exception {
    final BufferedReader br = new BufferedReader(new FileReader(args[0]));
  
    final int nodeCount = Integer.parseInt(br.readLine());
    array = new int[nodeCount];
    for (int i = 0; i < array.length; i++) {
      array[i] = -1;
    }

    int successes = 0;
    int fails = 0;

    while (br.ready()) {
      String line = br.readLine();
      char c = line.charAt(0);
      int fs = line.indexOf(' ', 1);
      int ls = line.lastIndexOf(' ');
      int a = Integer.parseInt(line.substring(fs+1, ls)) - 1;
      int b = Integer.parseInt(line.substring(ls+1)) - 1;

      if (c == 'c') {
        int setA = find(a);
        int setB = find(b);
        if (setA != setB)
          union(setA, setB);
      } else {
        if (find(a) == find(b))
          successes++;
        else
          fails++;
      }
    }
    System.out.println(successes + "," + fails);
  }

  private static void union(int root1, int root2) {
    if (array[root2] < array[root1]) {
      array[root1] = root2;
    } else {
      array[root2] = root1;
    }
  }

  private static int find(int x) {
    if (array[x] < 0) {
      return x;
    } else {
      array[x] = find(array[x]);
      return array[x];
    }
  }
}
