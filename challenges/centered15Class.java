// . An array is called centered-15 if some consecutive sequence of elements of the array sum to
// 15 and this sequence is preceded and followed by the same number of elements. For example
// {3, 2, 10, 4, 1, 6, 9} is centered-15 because the sequence 10, 4, 1 sums to 15 and the
// sequence is preceded by two elements (3, 2) and followed by two elements(6,9).
// Write a method called isCentered15 that returns 1 if its array argument is centered-15, otherwise
// it returns 0.

// Contributors: Marvin Kweyu(twitter: @marvinus_j)

import java.util.Arrays;

public class centered15Class {
    public static void main(String args[]) {
        int[] myArray = { 2, 10, 4, 1, 6, 9 };
        System.out.println("the array is centered: " + isCentered15(myArray));

    }

    public static int isCentered15(int[] a) {
        int arrayLength = a.length;
        int left = 0;
        int right = arrayLength - 1;
        int isCentered = 0;

        // check for edge cases

        if (arrayLength == 0) {
            return 0;
        }

        if (arrayLength == 3 && a[1] == 15) {
            return 1;

        }

        while (left < right) {
            int[] newArray = Arrays.copyOfRange(a, left, right);
            int sum = 0;
            for (int num : newArray) {
                sum += num;
            }

            if (sum == 15) {
                isCentered = 1;
                return 1;
            }
            if (sum < 15) {

                left++;
            } else {

                right--;
            }

        }
        return isCentered;
    }
}
