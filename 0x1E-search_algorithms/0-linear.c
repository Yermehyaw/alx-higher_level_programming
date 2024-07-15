#include <stdio.h>
#include "search_algos.h"

/**
 * linear_search - Search for an integer in an array using linear search algo
 * @array: the array
 * @size: size of the array
 * @value: value to find in the array
 *
 * Return: The index where @value is found, otherwise, -1 (Success)
 */

int linear_search(int *array, size_t size, int value)
{
	int i;

	if (array == NULL || size == 0)
		return (-1);
	if (size == 1)
		return (0);  /* Index 0 */
	for (i = 0; i < size; i++)
	{
		if (array[i] == value)
		{
			printf("Found %d at index: %d", value, i)
			return (i);
		}
		else
			printf("Value checked array[%d] = [%d]", i, array[i]);
	}
	return (-1);
}
