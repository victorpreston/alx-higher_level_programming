#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/****************************START*****************************/
/**
 * insert_node - function: inserts a number into a linked list
 * @head: Points to the head of the linked lists
 * @number: refers to the digit or number to insert
 *
 * Return: If fail - NULL.
 *         Else - a pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (node == NULL || node->n >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	new->next = node->next;
	node->next = new;

	return (new);
}
/*************************STOP*********************************/
