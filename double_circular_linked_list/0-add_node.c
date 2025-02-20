#include "list.h"

/**
 * string_length - finds the length of a string
 * @str: the string to find the length of
 *
 * Return: the int count of length of the string
 */
int string_length(char *str)
{
    int count = 0;

    for (count = 0; str[count]; count++)
        continue;
    return (count);
}

/**
 * add_node_end - adds a new node to the end
 * of a double circular linked list
 * @list: double circularly linked list to modify
 * @str: the string to copy into the new node
 *
 * Return: the address of the new node or NULL on failure
 */
List *add_node_end(List **list, char *str)
{
    List *new_node = NULL;
    int i = 0;

    if (list == NULL)
        return (NULL);

    new_node = malloc(sizeof(List *));
    if (new_node == NULL)
        return (NULL);

    new_node->str = malloc(sizeof(char) * (string_length(str) + 1));
    if (new_node->str == NULL)
    {
        free(new_node);
        return (NULL);
    }
    for (i = 0; str[i]; i++)
        new_node->str[i] = str[i];
    new_node->str[i] = '\0';

    if ((*list) == NULL)
    {
        new_node->prev = new_node;
        new_node->next = new_node;
        (*list) = new_node;
    }
    else
    {
        new_node->prev = (*list)->prev;
        (*list)->prev->next = new_node;
        (*list)->prev = new_node;
        new_node->next = (*list);
    }

    return (new_node);
}

/**
 * add_node_begin - adds a new node to the beginning
 * of a double circular linked list
 * @list: double circularly linked list to modify
 * @str: the string to copy into the new node
 *
 * Return: the address of the new node or NULL on failure
 */
List *add_node_begin(List **list, char *str)
{
    List *new_node = NULL;
    int i = 0;

    if (list == NULL)
        return (NULL);

    new_node = malloc(sizeof(List *));
    if (new_node == NULL)
        return (NULL);

    new_node->str = malloc(sizeof(char) * (string_length(str) + 1));
    if (new_node->str == NULL)
    {
        free(new_node);
        return (NULL);
    }
    for (i = 0; str[i]; i++)
        new_node->str[i] = str[i];
    new_node->str[i] = '\0';

    if ((*list) == NULL)
    {
        new_node->prev = new_node;
        new_node->next = new_node;
    }
    else
    {
        new_node->prev = (*list)->prev;
        (*list)->prev->next = new_node;
        (*list)->prev = new_node;
        new_node->next = (*list);
    }
    (*list) = new_node;

    return (new_node);
}