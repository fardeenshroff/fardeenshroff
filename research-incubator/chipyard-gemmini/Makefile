CC ?= cc
CFLAGS ?= -std=c11 -O2 -Wall -Wextra -pedantic
.PHONY: all test clean
all: matmul_reference
matmul_reference: src/matmul_reference.c
	$(CC) $(CFLAGS) $< -o $@
test: matmul_reference
	./matmul_reference 8
	./matmul_reference 16
clean:
	rm -f matmul_reference

