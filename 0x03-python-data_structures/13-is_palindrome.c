#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to head of list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *ptr = NULL;
	unsigned int i = 0, j = 0, k = 0, len = 0;
	int array[BUFSIZ], a, b;

	if (*head == NULL)
		return (1);
	ptr = *head;
	while (ptr != NULL)
	{
		array[i] = ptr->n;
		ptr = ptr->next;
		i++;
	}
	k = i - 1;
	for (j = 0; j < (i / 2); j++, k--)
	{
		a = array[j];
		b = array[k];
		if (a != b)
			len++;
	}
	if (len == 0)
		return (1);
	else
		return (0);
}