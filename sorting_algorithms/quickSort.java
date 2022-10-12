
/* An implementation of the quick sort algorithm
 * Time complexity O(n(log (n)))
 * Contributors: Marvin Kweyu(twitter: @marvinus_j)
 */

import java.util.Random;

public class quickSort {
    public static void main(String[] args) {

        // generate 10 random numbers between 1 and 100
        Random rand = new Random();
        int numbers[] = new int[30];

        for (int i = 0; i < numbers.length; i++) {
            numbers[i] = rand.nextInt(200);
        }

        printArray(numbers);

        System.out.println("Sort the array: ...\n");

        qsort(numbers, 0, numbers.length - 1);
        printArray(numbers);

    }

    public static void qsort(int[] array, int lowIndex, int highIndex) {

        // if the array has one item

        if (lowIndex >= highIndex) {
            return;
        }
        int pivot = array[highIndex];

        int leftPointer = lowIndex;
        int rightPointer = highIndex;

        while (leftPointer < rightPointer) {
            while (array[leftPointer] <= pivot && leftPointer < rightPointer) {
                leftPointer++;
            }
            while (array[rightPointer] >= pivot && rightPointer > leftPointer) {
                rightPointer--;
            }

            swap(array, leftPointer, rightPointer);
        }

        swap(array, leftPointer, highIndex);

        qsort(array, lowIndex, leftPointer - 1);
        qsort(array, leftPointer + 1, highIndex);
    }

    private static void swap(int[] array, int index1, int index2) {
        int temp = array[index1];
        array[index1] = array[index2];
        array[index2] = temp;
    }

    private static void printArray(int[] array) {
        for (int item : array) {
            System.out.println(item);
        }
    }

}
