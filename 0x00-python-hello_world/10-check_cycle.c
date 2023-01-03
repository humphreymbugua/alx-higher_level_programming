#include "lists.h"

/**
 * check_cycle - Function to check for cycle in singly linked list
 * @list: argument of type listint_t *
 * Return: 1 if True
 * 0 if False
 */

int check_cycle(listint_t *list)
{
	listint_t *hare, *tortoise;

	hare = list;
	tortoise = list;

	while ((hare != NULL) && (hare->next != NULL))
	{
		hare = hare->next->next;
		tortoise = tortoise->next;

		if (hare == tortoise)
		{
			return (1);
		}
	}
	return (0);
}
