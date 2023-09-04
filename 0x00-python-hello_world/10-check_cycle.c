#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - function: checks for a singly linked list in a cycle.
 * @list: This is the sinly linked list.
 *
 * Return: No cycle - 0.
 *         A cycle - 1.
 */
int check_cycle(listint_t *list)
{
	listint_t *cycle_y;
	listint_t *cycle_n;

	if (list == NULL || list->next == NULL)
		return (0);

	cycle_y = list->next;
	cycle_n = list->next->next;

	while (cycle_y && cycle_n && cycle_n->next)
	{
		if (cycle_y == cycle_n)
			return (1);

		cycle_y = cycle_y->next;
		cycle_n = cycle_n->next->next;
	}

	return (0);
}
