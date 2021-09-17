#include "palindrome.h"
#include <stdio.h>

/**
 * is_palindrome - function that checks whether or not
 *                 a given unsigned integer is a palindrome.
 *
 * @n: n is the number to be checked
 *
 * Return: 1 if n is a palindrome, and 0 otherwise
 */

int is_palindrome(unsigned long n)
{
	unsigned long temp = n / 10, reversed = n % 10;

	while (temp > 0)
	{
		reversed = (reversed * 10) + temp % 10;
		temp = temp / 10;
	}
	if (reversed == n)
	{
		return (1);
	}

	return (0);
}
