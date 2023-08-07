#include "lists.h"

int check_cycle(listint_t *list)
{
    listint_t *ptr = list;

    if (ptr == NULL)
        return (0);

    while (ptr)
    {
        if (ptr->next == list)
            return (1);
        ptr = ptr->next;
    }
    return (0);
}
