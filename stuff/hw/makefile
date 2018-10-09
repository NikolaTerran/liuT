all: main.o print_list.o struct.h
	gcc main.o print_list.o

main.o: main.c
	gcc -c main.c

print_list.o: print_list.c
	gcc -c print_list.c

run:
	./a.out

clean:
	rm *.o
