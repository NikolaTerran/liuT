#include <stdio.h>
#include <string.h>

int main(){
	
	printf("\nDeclare a char array and initiate its value to \"abcdecdf.\"\n\n");
	
	char a[10] = "abcdecdf";
	
	printf("Declare a char variable and initiate its value to \"d.\"\n\n");
	
	char b = 'd';

	printf("Declare a char arry and initiate its value to \"cdf\"\n\n");

	char c[5] = "cdf";
	
	printf("**********************************************************\n\n");

	printf("\"strchr\" returns the pointer of letter \"%c\" in string \"%s\"\n\n",b,a);
	
	printf("The pointer value of \"%c\" in \"%s\" is %p.\n\n", b,a,strchr(a,b));

	printf("De-referenced value for %p is \'%c.\'\n\n",strchr(a,b),*strchr(a,b));
	printf("**********************************************************\n\n");
	printf("\"strstr\" returns the pointer of string \"%s\" in string \"%s.\"\n\n",c,a);

	printf("The pointer value of \"%s\" in \"%s\" is %p.\n\n", c,a,strstr(a,c));
        printf("Create a char pointer that stores the result of \"strstr\"\n\n");

	char *d = strstr(a,c);
	printf("De-referenced value for %p is \"%s\".\n\n",strstr(a,c),d);
	return 0;
}
