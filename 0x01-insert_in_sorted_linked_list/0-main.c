#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * main - check the code for Holberton School students.
 *
 * Return: Always 0.
 */
int main(void)
{
    listint_t *head, *test1;
    test1 = NULL;
    /*test2 = NULL;*/
    head = NULL;

    add_nodeint_end(&head, 0);
    add_nodeint_end(&head, 1);
    add_nodeint_end(&head, 2);
    add_nodeint_end(&head, 3);
    add_nodeint_end(&head, 4);
    add_nodeint_end(&head, 91);
    add_nodeint_end(&head, 403);
    add_nodeint_end(&head, 1024);

    print_listint(head);

    printf("-----------------\n");

    insert_node(&head, 100);
    print_listint(head);

    printf("-----------------\n");

    add_nodeint_end(&test1, -5);
    add_nodeint_end(&test1, 5);
    print_listint(test1);
    printf("-----------------\n");
    insert_node(&test1, 4);

    print_listint(test1);

    free_listint(head);
	/*while(temp->next != NULL)
	{
		if (number <= temp->next->n)
		{
			new->next = temp->next;
			temp->next = new;
			break;
		}
		temp = temp->next;
	}
	if (temp->next == NULL)
	temp->next = new;*/

    return (0);
}
