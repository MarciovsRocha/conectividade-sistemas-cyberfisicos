#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[]){
	if (argc < 2) 
		printf("Você esqueceu um argumento");
	else{
		int mem = atoi(argv[1]);
		void *buffer = malloc(mem);
		if(buffer == NULL)
			printf("Você pediu memória demais");
		else{
			memset(buffer,1,mem);
		}
		printf("<ENTER> para encerrar");
		getchar();
	}
}
