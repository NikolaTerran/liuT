#include <stdio.h>
#include "linkedlist.h"

//struct node { int i; struct node *next;};

void print_list(struct node *list){
	struct node *count = list;	
	do{	
		printf("%d\n",list->i);
		printf("%d\n",123);
		if(count->next){count->next = list->next;};
	}while(count->next);
}
