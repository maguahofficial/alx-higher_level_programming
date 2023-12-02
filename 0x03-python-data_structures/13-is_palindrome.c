#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
*add_nodeint - function adds a new node at the beginning of a listint_t list
*@head: head of listint_t
*@n: int (int variable) to add in listint_t list
*Return: returns address of the new element, or NULL if it failed
*/
listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = n;
	new->next = *head;
	*head = new;
	return (new);
}
/**
*is_palindrome - function identify if a syngle linked list is palindrome
*@head: (pointer)head of listint_t
*Return: 1 if it is palindrome else 0
*/
int is_palindrome(listint_t **head)
{
	listint_t *head2vrb = *head;
	listint_t *auxvrb = NULL, *aux2vrb = NULL;

	if (*head == NULL || head2vrb->next == NULL)
		return (1);
	while (head2vrb != NULL)
	{
		add_nodeint(&auxvrb, head2vrb->n);
		head2vrb = head2vrb->next;
	}
	aux2vrb = auxvrb;
	while (*head != NULL)
	{
		if ((*head)->n != aux2vrb->n)
		{
			free_listint(auxvrb);
			return (0);
		}
		*head = (*head)->next;
		aux2vrb = aux2vrb->next;
	}
	free_listint(auxvrb);
	return (1);
}
