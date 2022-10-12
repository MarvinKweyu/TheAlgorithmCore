// The function below

/*
 * The function below is an implementation of the bubble sort algorithm
 * Time complexity: O(n) worst case complexity O(n^2)
 * Contributors: Marvin Kweyu(twitter: @marvinus_j)
 **/

public class bubbleSort {
    public static void main(String[] args) {
        int[] nums = { 99, -10, 100123, 18, -978,
                5623, 463, -9, 287, 49 };

        sortingAlgorithm(nums);

        for (int item : nums) {
            System.out.println("The item is: " + item);
        }

    }

    static void sortingAlgorithm(int[] unsortedArray) {
        // this is the bubble sort

        for (int i = 1; i < unsortedArray.length; i++) {
            for (int j = unsortedArray.length - 1; j >= i; j--) {
                if (unsortedArray[j - 1] > unsortedArray[j]) {
                    // exchange/ swap occurs
                    int item = unsortedArray[j - 1];
                    unsortedArray[j - 1] = unsortedArray[j];
                    unsortedArray[j] = item;
                }
            }
        }

    }
}
