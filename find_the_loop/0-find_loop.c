#include "lists.h"

/**
 * find_listint_loop - Function finds the loop in a linked list
 * @head: Pointer to head of the list
 *
 * Return: The address of the node where the loop starts, or NULL if there
 * is no loop
 */
listint_t *find_listint_loop(listint_t *head)
{
    listint_t *tortoise, *hare;

    if (!head || !head->next)
        return (NULL);

    tortoise = head->next;
    hare = head->next->next;

    while (hare && hare->next)
    {
        if (tortoise == hare)
        {
            tortoise = head;
            while (tortoise != hare)
            {
                tortoise = tortoise->next;
                hare = hare->next;
            }
            return (tortoise);
        }
        tortoise = tortoise->next;
        hare = hare->next->next;
    }

    return (NULL);
}