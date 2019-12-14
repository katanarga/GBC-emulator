#include "constants.h"

typedef struct {
    unsigned short pos_x;
    unsigned short pos_y;
    char r,g,b;
} Pixel;

typedef struct {
    Pixel pixels[WIDTH_SCREEN][HEIGHT_SCREEN];
} Screen;

typedef struct{
    char button_a;
    char button_b;
    char button_start;
    char button_select;
    Screen screen;
    unsigned short program_counter;
    unsigned short stack[16];
    unsigned short stack_pointer;
    char memory[65536];
    char registers[8];
} Game_boy_color;