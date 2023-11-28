#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - function singly linked list
 * @nvariable: integer variable
 * @nextvariable: The points to the next node
 * List.hheader file
 * Description: The singly linked list node structure
 */
typedef struct listint_s
{
	int nvariable;
	struct listint_s *nextvariable;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head, const int nvariable);
void free_listint(listint_t *head);
int check_cycle(listint_t *list);

#endif
