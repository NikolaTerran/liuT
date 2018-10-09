all: main.o print_list.o linkedlist.h insert_front.o
	gcc main.o print_list.o insert_front.o

main.o: main.c
	gcc -c main.c

print_list.o: print_list.c
	gcc -c print_list.c

insert_front.o: insert_front.c
	gcc -c insert_front.c

run:
	./a.out

clean:
	rm *.o
