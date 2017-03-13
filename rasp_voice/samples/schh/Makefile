#common makefile header

DIR_INC = ../../include
#DIR_BIN = ../../bin
DIR_LIB = ../../libs

TARGET	= schh
#BIN_TARGET = $(DIR_BIN)/$(TARGET)

CROSS_COMPILE = 
CFLAGS = -g -Wall -I$(DIR_INC)

ifdef RaspberryPi
LDFLAGS := -L$(DIR_LIB)/RaspberryPi
else
LDFLAGS := -L$(DIR_LIB)/x86 
endif
LDFLAGS += -lmsc -lrt -ldl -lpthread -lasound -lm -lwiringPi 

OBJECTS := $(patsubst %.c,%.o,$(wildcard *.c))

$(TARGET) : $(OBJECTS)
	$(CROSS_COMPILE)gcc $(CFLAGS) $^ -o $@ $(LDFLAGS)

%.o : %.c
	$(CROSS_COMPILE)gcc -c $(CFLAGS) $< -o $@ -lm
clean:
	@rm -f *.o $(TARGET)

.PHONY:clean

#common makefile foot
