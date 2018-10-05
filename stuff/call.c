#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(){
	printf("\ncalloc -- allocates the requested memory and returns a pointer to the allocated memory, or NULL if the request fails.\n\n");

	printf("void *calloc(size_t nitems, size_t size\n\n");
	
	int i = 10;
	int j;	

	int *a = (int*)calloc(i, sizeof(int));

	for(j = 0; j<i;j++){
		srand(time(NULL)+j);
		a[j] = rand();
	}

	printf("I requested memory to store 10 random int, assigned a pointer to it, and this is what I got:\n");

	for(j = 0; j<i;j++){
		printf("%d\n",a[j]);
	}
	printf("===================================================================\n");
	printf("realloc attempts to resize the memory block allocated by calloc by using a pointer.\n\n");
	printf("void *realloc(void *ptr, size_t size)\n\n");
	a = realloc(a,5);
	printf("I resized the mem-block to 5 int so this is what I got:\n");
	
	for(j = 0; j<i;j++){
		printf("%d\n",a[j]);
	}	
	printf("huh, nothing changed, maybe the unused data is not erased yet.\n");

	return 0;
}		
