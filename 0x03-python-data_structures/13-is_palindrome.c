#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: pointer to the list.
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome or -1 (error).
 */
int is_palindrome(listint_t **head)
{
	listint_t *aux;
	int len, i, *copy;

	/* empty list */
	if (!*head || !head)
		return (1);
	/* calculate length of the list */
	aux = *head;
	for (len = 1; aux->next; len++)
		aux = aux->next;
	/* create a copy of the list in an array */
	copy = malloc(sizeof(int) * (len));
	if (!copy)
		return (-1);
	for (i = 0, aux = *head; i < len; i++, aux = aux->next)
		copy[i] = aux->n;
	/* checks if its a palindrome */
	for (i = 0; i < (len / 2); i++)
		if (copy[i] != copy[len - 1 - i])
		{
			free(copy);
			return (0);
		}
	free(copy);
	return (1);
}
