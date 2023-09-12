#include "lists.h"

/**
* list_len -Function: finds elements in a linked list.
* @h: pointer to linked list.
*
* Return: number of elements in linked list.
*/
size_t list_len(listint_t *h)
{
	size_t  n_d = 0;

	if (h == NULL)
		return (0);
	while (h != NULL)
	{
		n_d++;
		h = h->next;
	}
	return (n_d);
}

/**
* is_palindrome -Checks whether a singly linked list is palindrome
* @head: double pointert to head of d-list.
*
* Return: 1 if palindrome, 0 otherwise - (Elsewhere)
*/
int is_palindrome(listint_t **head)
{
	int *nArr, i = 0, j = 0, len = 0;
	listint_t *temp;

	if (*head == NULL)
		return (1);
	temp = *head;
	len = list_len(temp);
	nArr = (int *)malloc(sizeof(int) * len);
	if (nArr == NULL)
		return (2);
	temp = *head;
	while (temp != NULL)
	{
		nArr[j] = temp->n;
		j++;
		temp = temp->next;
	}
	for (i = 0, j = len - 1; i < j; i++, j--)
	{
		if (nArr[i] != nArr[j])
			return (0);
	}
	return (1);
}
