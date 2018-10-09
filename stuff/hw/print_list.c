#include <stdio.h>

//struct node { int i; struct node *next;};

void print_list(struct node *list){
	struct node *count = list->next;	
	do{	
		print("%d\n",list->i);
		count = list->next 
	}while(count.next);
