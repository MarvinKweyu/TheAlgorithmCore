// An array can hold the digits of a number. For example the digits of the number 32053 are stored in the array {3, 2, 0, 5, 3}. 
// Write a method call repsEqual that takes an array and an integer and returns 1 if 
// the array contains only the digits of the number in the same order that they appear in the number. Otherwise it returns 0.

// where len is the number of elements in the array.

public class repsEqualClass {
    public static void main(String args[]) {
        int[] myArray = { 3, 2, 0, 5, 3 };
        int myNumber = 32053;

        System.out.println("repsEqual: " + repsEqual(myArray, 5, myNumber));

    }

    public static int repsEqual(int a[], int len, int n) {

        char[] integerChars = Integer.toString(n).toCharArray();

        // check if they are the same length
        if (len != integerChars.length) {
            return 0;
        }

        for (int i = 0; i < len; i++) {

            // * thought: characters are identified differently within conversion. Nota Rust
            // unicode conversion
            // if (Integer.toString(a[i]) != Character.toString(integerChars[j])) {
            // return 0;
            // }

            // solution to above
            if (!Integer.toString(a[i]).equals(Character.toString(integerChars[i]))) {
                return 0;
            }

            if (a[i] != Character.getNumericValue(integerChars[i])) {

                return 0;
            }

        }

        return 1;

    }
}
