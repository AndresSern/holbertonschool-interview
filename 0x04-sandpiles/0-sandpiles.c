#include "sandpiles.h"
#include <stdio.h>


/**
 * checkSandPiles - Funcion that sum two grid and check if there are toppling
 * @grid1: Left grid 3x3
 * @grid2: Right grid 3x3
 *
 * Return: Return 1 if there are numbers bigger than 4
 *         Return 0 if There are not number bigger than 4
 */
int checkSandPiles(int grid1[3][3], int grid2[3][3])
{
	int i, j, c = 0;

	for (i = 0; i < 3; i++)
	{
		for (j = 0; j < 3; j++)
		{
			grid1[i][j] = grid1[i][j] + grid2[i][j];
			if (grid1[i][j] > 3)
				c++;
		}
	}
	if (c == 0)
		return (0);
	return (1);
}

/**
 * sumSandPiles - Sum grid1 to the new grid called grid2
 * @grid1: Left grid 3x3
 *
 * Return: Return 1 if there are numbers bigger than 4
 *         Return 0 if There are not number bigger than 4
 */

int sumSandPiles(int grid1[3][3])
{
	int grid2[3][3] = {
		{0, 0, 0},
		{0, 0, 0},
		{0, 0, 0}
	};
	int i, j;

	for (i = 0; i < 3; i++)
	{
		for (j = 0; j < 3; j++)
		{
			if (grid1[i][j] > 3)
			{
				if (i - 1 >= 0)
					grid2[i - 1][j] += 1;
				if (i + 1 <= 2)
					grid2[i + 1][j] += 1;
				if (j + 1 <= 2)
					grid2[i][j + 1] += 1;
				if (j - 1 >= 0)
					grid2[i][j - 1] += 1;
				grid1[i][j] -= 4;
			}
		}
	}
	return (checkSandPiles(grid1, grid2));
}

/**
 * print_grid - Print the grid
 *
 * @grid: Left 3x3 grid
 *
 */

static void print_grid(int grid[3][3])
{
	int i, j;

	for (i = 0; i < 3; i++)
	{
		for (j = 0; j < 3; j++)
		{
			if (j)
				printf(" ");
			printf("%d", grid[i][j]);
		}
		printf("\n");
	}
}

/**
 * sandpiles_sum - Computes the sum of two sandpiles
 * @grid1: Left 3x3 grid
 * @grid2: Right 3x3 grid
 *
 */
void sandpiles_sum(int grid1[3][3], int grid2[3][3])
{
	int check = checkSandPiles(grid1, grid2);

	while (check)
	{
		printf("=\n");
		print_grid(grid1);
		check = sumSandPiles(grid1);
	}
}
