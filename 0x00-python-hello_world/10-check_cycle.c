#include "lists.h"

/**
 * check_cycle -  checks if a singly linked list has a cycle in it.
 * @list: linked list to check.
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *s1, *s2;

	if (!list || !list->next)
		return (0);

	s1 = list->next;
	s2 = list->next->next;
	while (s1 && s2 && s2->next)
	{
		if (s1 == s2)
			return (1);

		s1 = s1->next;
		s2 = s2->next->next;
	}
	return (0);
}
