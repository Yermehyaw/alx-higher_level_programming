#include <stdio.h>y
#include "search_algos.h"

int divide_and_conquer(int *sorted_arr, size_t size);
void print_array(int *array, size_t size);

/**
 * binary_search - Implements tge binary search algo. on an array
 * @array: the array to search
 * @size: size of the array
 * @value: value to find in the array
 *
 * Return: Index where value is located (Success). Otherwise, -1
 */

int binary_search(int *array, size_t size, int value)
{
	int found;

	if (array == NULL || size == 0)
		return (-1);
	if (size == 1)  /* Array of size 1*/
		return (0);
	found = divide_and_conquer(array, size);
	return (found);  /*if -1, value was not foind in the array*/
}


/**
 * divide_and_conquer - Inplement the recursioms needed in the algorithm
 * @sorted_arr: array sorted in increasing order
 * @size: size of the array
 *
 * Return: The index where the value is located, otherwise, -1
 */

int divide_and_conquer(int *sorted_arr, size_t size)
{
	int mid;

	mid = size / 2;
	/* Base-cases, forgive the many if, else ifs.... ;) */
	if (sorted_arr[mid] == value)
		return (mid - 1); /*index starts from 0, mid mist reduce by 1*/
	else if (sorted_arr[mid + 1] == value)
		return ((mid + 1) - 1); /* or just return mid */
	else if (sorted_arr[mid - 1] == value)
		return ((mid - 1) - 1); /* or mid - 2 */
	/**
	 *  value is not in the array if both mid+1 and mid-1 are greater than
	 *  or less than value
	 */
	else if (sorted_arr[mid - 1] < value && sorted_arr[mid + 1] < value)
		return (-1); /* both value at the indices are less than */
	else if (sorted_arr[mid - 1] > value && sorted_arr[mid + 1] > value)
		return (-1); /* botha re greater than */
	/* Recursive calls */
	if (sorted_arr[mid + 1] < value) /*if yes, take right hand side of arr*/
	{
		/**
		 * the array is sorted in ascending order, so the if the value
		 * right of the mid is less than the value of interest, it shows
		 * that the value of interest is large and thus at the right
		 * hand side of the array
		 */
		print_array(sorted_arr, size);
		divide_and_conquer(sorted_arr[mid + 1], size - mid)
	}
	else if (sorted_arr[mid - 1] > value)/*if yes, take the left arr*/
	{
		print_array(sorted_arr, size);
		divide_and_conquer(sorted_arr[mid - 1], size - (mid + 1));
	}
	return (-1);  /* control flow may never reach here ;) */
}


/**
 * print_array - prints an array of ints
 * @array: array
 * @size: size of the array
 */

void print_array(int *array, size_t size)
{
	int i;

	printf("Searching in array:");
	for (i = 0; i < size; ++i)
	{
		printf(" ,%d", array[i]);
		if ((i + 1) == size) /* Last iteration */
			printf("\n");
	}
}
