Java лр5 	
public class MaxElement {
    public static int findMax(int[] arr, int size) {
        if (size == 1) {
            return arr[0];
        } else {
            int maxRest = findMax(arr, size - 1);
            return (arr[size - 1] > maxRest) ? arr[size - 1] : maxRest;
        }
    }

    public static void main(String[] args) {
        int[] numbers = {3, 7, 2, 8, 5};
        int max = findMax(numbers, numbers.length);
        System.out.println("Максимальный элемент: " + max);
    }
}
