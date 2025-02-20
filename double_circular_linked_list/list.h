#ifndef LIST_H
#define LIST_H

/* INCLUDED LIBRARIES */
#include <stdio.h>
#include <stdlib.h>

/* DEFINITIONS AND STRUCTS */
/**
 * struct List - doubly linked list
 * @str: string - (malloc'ed string)
 * @prev: points to the previous node
 * @next: points to the next node
 *
 * Description: doubly linked list node structure
 * for Holberton project
 */
typedef struct List
{
    char *str;
    struct List *prev;
    struct List *next;
} List;

/* FUNCTION PROTOTYPES */
/* function to determine the length of a string */
int string_length(char *str);
/* function to add new node to end of a double circular linked list */
List *add_node_end(List **list, char *str);
/* function to add new node to beginning of a double circular linked list */
List *add_node_begin(List **list, char *str);

#endif