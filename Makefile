CC=gcc
CFLAGS= -Wall -Wextra -g 
LIBS= -lSDL2 -lSDL2_image
SRCS=$(wildcard *.c)
OBJS=$(SRCS:.c=.o)
PROG=gbc_emulator
all: $(PROG)
$(PROG): $(OBJS)
	$(CC) $(CFLAGS) -o $(PROG) $(OBJS) $(LIBS)
depend: .depend
.depend: $(SRCS)
	rm -f ./.depend
	$(CC) $(CFLAGS) -MM $^ > ./.depend;
include .depend
clean:
	rm -f *o *~ $(PROG)