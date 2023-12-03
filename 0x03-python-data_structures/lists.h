#include <stddef.h>

#ifndef LISTS_H
#define LISTS_H

/**
 * struct listint_s - function singly linked list
 * @n: (variable)integer
 * @next: (pointer)points to the next node
 * header file
 * Description: the singly linked list node structure
 * for project
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int n);
void free_listint(listint_t *head);

int is_palindrome(listint_t **head);

#endif
