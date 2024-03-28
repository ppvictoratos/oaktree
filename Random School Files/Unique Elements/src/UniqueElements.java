/**
 * UniqueElements.java 1.0 Sep 14, 2018
 * 
 * Copyright (c) 2018 Peter P. Victoratos. All Rights Reserved
 * 319 W Trollinger Ave, Elon, NC 27244
 */

/**
 * Start each class or interface with summary description line

 * @author Peter
 * @version 1.0
 *
 */
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class UniqueElements {

  /**
   * Determines whether all the elements in a given array are distinct
   * 
   * @param An array A[0...n-1]
   * @return
   * @return "true" if all elements in A are distinct and "false" otherwise
   * @throws FileNotFoundException
   */
  public static void main(String[] args) throws FileNotFoundException {
    File file = new File("pa1_input.txt");

    if (UniqueElements(file) == true)
      System.out.println("True");
    else {
      System.out.println("False");
    }

  }

  public static boolean UniqueElements(File file) throws FileNotFoundException {
    long start = System.currentTimeMillis();
    Scanner scnr = new Scanner(file);
    int L = 0;
    int n = 0;
    scnr.useDelimiter("\t");

    // Figure out loop so that it resets n everytime a new line is reached
    while (scnr.hasNext()) {
      L += 1;

    }
    n = scnr.nextInt();
    for (int i = 0; i < n - 2; i++) {
      for (int j = i + 1; j < n - 1; j++) {
        if (A[i] == A[j]) {
          return false;
        }
      }
      return true;
    }

    System.out.println("Scanner Closing");
    scnr.close();
    System.out.println("Scanner Closed");

    long end = System.currentTimeMillis();
    long elapsed = end - start;
    System.out.println("For input size " + n + ", elapsed time was " + elapsed + " ms");
    return true;
  }
}
