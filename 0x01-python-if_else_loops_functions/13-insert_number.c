#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * insert_node - function to insert a number into a sorted singly linked list
 * @head: pointer to the beginning of the linked list
 * @number: value n of the inserted node
 * Return: address of the new_node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = malloc(sizeof(listint_t));
	listint_t *current = *head;

	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL || number < (*head)->n)
	{
		new_node->next = *head;
		*head = new_node;
	}
	else
	{
		while (current->next != NULL && current->next->n < number)
			current = current->next;
	}
	new_node = current->next;
	current->next = new_node;

	return (new_node);
}
