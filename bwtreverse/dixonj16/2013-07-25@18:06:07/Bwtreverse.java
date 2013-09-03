import java.io.FileReader;
import java.io.BufferedReader;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.List;
import java.util.ArrayList;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Bwtreverse {
  public static void main(String[] args) throws Exception {
    final BufferedReader br = new BufferedReader(new FileReader(args[0]));
    while (br.ready()) {
      final String[] line = br.readLine().split(" ");
      int j = Integer.parseInt(line[0]);
      final int l = line[1].length();
      final int[] pos = new int[l];
      final Map<Byte, List<Integer>> byteCount = new HashMap<Byte, List<Integer>>();

      final byte[] word = line[1].getBytes();
      Arrays.sort(word);
      for (int i = 0; i < l; i++) {
        final byte b = word[i];
        if (!byteCount.containsKey(b)) {
          List<Integer> z = new ArrayList<Integer>(2);
          z.add(0);
          z.add(i);
          byteCount.put(b, z);
        }
      }

      for (int i = 0; i < l; i ++) {
        final byte b = (byte)line[1].charAt(i);
        List<Integer> z = byteCount.get(b);
        pos[i] = z.get(0) + z.get(1);
        z.set(0, z.get(0) + 1);
      }

      final byte[] out = new byte[l];
      for (int i = l-1; i >= 0; i--) {
        out[i] = (byte)line[1].charAt(j);
        j = pos[j];
      }
      System.out.println(new String(out));
    }
  }
}