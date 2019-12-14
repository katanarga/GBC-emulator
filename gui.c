#include <SDL2/SDL.h>
#include <SDL2/SDL_image.h>
#include "constants.h"

int main (void){
        SDL_Window* window;
        SDL_Renderer* renderer;
        if(SDL_CreateWindowAndRenderer(WIDTH_WINDOW,HEIGHT_WINDOW,
          SDL_WINDOW_RESIZABLE,&window,&renderer))
			fprintf(stderr,"Erreur SDL_CreateWindowAndRenderer : %s\n",SDL_GetError());
		else{
            SDL_SetWindowTitle(window,"Emulateur GBC");
            SDL_Surface* window_icon=IMG_Load("images/gbc_pikachu.jpg");
            if(window_icon==NULL){
                printf("Erreur lors de la creation de l'icone : %s", IMG_GetError());
                return EXIT_FAILURE;
            }
            SDL_SetWindowIcon(window,window_icon);
            SDL_SetRenderDrawColor(renderer,69,206,247,255);
            SDL_RenderClear(renderer);
            SDL_Rect gameboy={200,50,700,800},
            menu={WIDTH_WINDOW-450,0,450,HEIGHT_WINDOW},
            rect_button_install={WIDTH_WINDOW-397,100,294,85},
            rect_button_load={WIDTH_WINDOW-397,400,294,85},
            rect_screen={250,100,600,450},
            cross_horizontal={250,650,150,50},
            cross_vertical={300,600,50,150},
            button_a={750,620,60,60},
            button_b={680,680,60,60},
            button_start={490,800,60,20},
            button_select={560,800,60,20};
            SDL_SetRenderDrawColor(renderer,121,18,130,255);
            SDL_Rect rects[]={gameboy,menu,button_a,button_b,button_start,button_select,cross_vertical,cross_horizontal};
            for(int i=0;i<8;i++){
                if(i==1)    SDL_SetRenderDrawColor(renderer,232,199,65,255);
                else if(i==2)    SDL_SetRenderDrawColor(renderer,0,0,0,255);
                SDL_RenderFillRect(renderer,&rects[i]);
            }
            SDL_Surface *button_install_game=IMG_Load("images/button_install_game.png"),
            *button_load_game=IMG_Load("images/button_load_game.png");
            SDL_Surface *surface_screen=SDL_CreateRGBSurface(0,100,100,32,0,0,0,0);
            if(surface_screen==NULL){
                printf("Erreur lors de la creation de la surface : %s", SDL_GetError());
                return EXIT_FAILURE;
            }
            SDL_Texture *texture=SDL_CreateTextureFromSurface(renderer,surface_screen);
                SDL_RenderCopy(renderer,texture,NULL,&rect_screen);
                texture=SDL_CreateTextureFromSurface(renderer,button_install_game);
                SDL_RenderCopy(renderer,texture,NULL,&rect_button_install);
                texture=SDL_CreateTextureFromSurface(renderer,button_load_game);
                SDL_RenderCopy(renderer,texture,NULL,&rect_button_load);
        SDL_RenderPresent(renderer);
            SDL_Event event;
            int loop=1,x,y;
            while(loop){
                while(SDL_PollEvent(&event)){
                    switch(event.type){
                        case SDL_QUIT:
                            loop=0;
                            break;
                        case SDL_MOUSEBUTTONDOWN:
                            x=event.button.x;
                            y=event.button.y;
                            if(x>=WIDTH_WINDOW-397 && x<=WIDTH_WINDOW-297){
                                if(y>=100 && y<=185)    printf("install\n");
                                else if(y>=400 && y<=485)    printf("load\n");
                            }
                            break;
                        case SDL_MOUSEMOTION:
                            break;
                    }
			    }
            }
            SDL_DestroyWindow(window);
        }
        return EXIT_SUCCESS;
}