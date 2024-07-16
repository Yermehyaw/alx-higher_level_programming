#include <stdio.h>
#include "search_algos.h"

int divide_and_conquer(int *sorted_arr, size_t size, int value);
void print_array(int *array, size_t size);
int *right_arr(int *sorted_arr, size_t size, int mid_right);
int *left_arr(int *sorted_arr, size_t size, int mid_left);

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
	found = divide_and_conquer(array, size, value);
	return (found);  /*if -1, value was not found in the array*/
}


/**
 * divide_and_conquer - Inplement the recursioms needed in the algorithm
 * @sorted_arr: array sorted in increasing order
 * @size: size of the array
 * @value: value to find in array
 *
 * Return: The index where the value is located, otherwise, -1
 */

int divide_and_conquer(int *sorted_arr, size_t size, int value)
{
	int *new_arr;
	int mid_idx;

	mid_idx = (size / 2) - 1; /* -1 to place index in a valid range */
	/* Base-cases, forgive the many if, else ifs.... ;) */
	if (sorted_arr[mid_idx] == value)
		return (mid_idx);
	else if (sorted_arr[mid_idx + 1] == value)
		return (mid_idx + 1);
	else if (sorted_arr[mid_idx - 1] == value)
		return (mid_idx - 1);
	/**
	 *  value is not in the array if both mid_idx+1 and mid_idx-1 are greater than
	 *  value or less than value
	 */
	/*else if ((sorted_arr[mid_idx - 1] < value) && */
			/*(sorted_arr[mid_idx + 1] < value))*/
		/*return (-1);*/ /* both value at the indices are less than */
	/*else if ((sorted_arr[mid_idx - 1] > value) && */
			/*(sorted_arr[mid_idx + 1] > value))*/
		/*return (-1);*/ /* both are greater than */
	/* Recursive calls */
	if (sorted_arr[mid_idx + 1] < value) /*if yes, take right hand side of arr*/
	{
		/**
		 * the array is sorted in ascending order, so the if the value
		 * right of the mid_idx is less than the value of interest, it shows
		 * that the value of interest is large and thus at the right
		 * hand side of the array
		 */
		print_array(sorted_arr, size);
		new_arr = right_arr(sorted_arr, size, mid_idx + 1);
		divide_and_conquer(new_arr, size - mid_idx, value);
	}
	else if (sorted_arr[mid_idx - 1] > value)/*if yes, take the left arr*/
	{
		print_array(sorted_arr, size);
		new_arr = left_arr(sorted_arr, size, mid_idx - 1);
		divide_and_conquer(new_arr, size - (mid_idx + 1), value);
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
	size_t i;

	/*This printing format is a task req*/
	if (size >= 1) /*If the array has at least one element*/
	{
		printf("Searching in array: %d", array[0]);
		for (i = 1; i <= size; ++i) /*print remining elem on the same line*/
		{
			printf(" ,%d", array[i]);
			if ((i == size) /*print a newline at the last iteration*/
				printf("\n");
		}
	}
	else /*not sure if still needed*/
		printf("Searching in array:");
}


/**
 * right_arr - copies an array from @mid_right till end of the array
 * @sorted_arr: the array
 * @size: size of @sorted_arr
 * @mid_right: the value, right of the middle index
 *
 * Return: a partitioned array
 */

int *right_arr(int *sorted_arr, size_t size, int mid_right)
{
	static int new_arr[10]; /* 10 is just a placeholder */
	size_t i;

	for (i = 0; i < size; ++i, ++mid_right)
		new_arr[i] = sorted_arr[mid_right];
	return (new_arr); /**
			   * non-dynamically allocated  arrays can only be
			   * returned if declared as static */
}


/**
 * left_arr - copies an array from @mid_left till end of the array
 * @sorted_arr: the array
 * @size: size of @sorted_arr
 * @mid_left: the value, left of the middle index
 *
 * Return: a partitioned  array
 */

int *left_arr(int *sorted_arr, size_t size, int mid_left)
{
	static int new_arr[10]; /* 10 is just a placeholder */
	size_t i;

	for (i = 0; i < size; ++i, ++mid_left)
		new_arr[i] = sorted_arr[mid_left];
	return (new_arr);
}
