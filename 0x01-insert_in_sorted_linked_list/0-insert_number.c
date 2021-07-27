#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = *head;
	listint_t *new = malloc(sizeof(listint_t));

    	if (new == NULL)
        	return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL || temp->n >= number)
	{
		new->next = *head;
		*head = new;
	}
	else
	{
		while(temp->next != NULL && temp->next->n <= number)
			temp = temp->next;
		if (temp->next != NULL)
			new->next = temp->next;
		temp->next = new;
	}
	return new;
}
