#include "lists.h"

/**
 * insert_node -This Function Inserts a number into a sorted singly-linked list.
 * @head: The pointer the head of the linked list.
 * @number: The number to insert.
 * 13. Insert in sorted linked list task
 * Return: This returns If the function fails - NULL.
 * Otherwise - the pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *nodevariable = *head, *newvariable;

	newvariable = malloc(sizeof(listint_t));
	if (newvariable == NULL)
		return (NULL);
	newvariable->n = number;

	if (nodevariable == NULL || nodevariable->n >= number)
	{
		newvariable->next = nodevariable;
		*head = newvariable;
		return (newvariable);
	}

	while (nodevariable && nodevariable->next && nodevariable->next->n < number)
		nodevariable = nodevariable->next;

	newvariable->next = nodevariable->next;
	nodevariable->next = newvariable;

	return (newvariable);
}
