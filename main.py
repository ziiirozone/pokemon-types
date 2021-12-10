import pygame
from tkinter import Tk

pygame.init()


def window(tile_size):
    pygame.display.set_caption("pokemon types")
    return pygame.display.set_mode((tile_size*23, tile_size*19))


def calculate_efficiency():
    if chosen_defender2:
        return [font.render(str(types_grid[chosen_defender1-1][x]*types_grid[chosen_defender2-1][x]),1,(255,255,255)) for x in range(18)]
    else:
        return [font.render(str(types_grid[chosen_defender1-1][x]),1,(255,255,255)) for x in range(18)]


class Assets:
    def __init__(self, x_size, y_size, path):
        self.image = pygame.transform.smoothscale(pygame.image.load(path).convert_alpha(), (x_size, y_size))
    def interaction(self, x, y):
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


# listes for types affinity and misc variables
types_grid=[[1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1], # normal
[1, 0.5, 2, 0.5, 1, 0.5, 1, 1, 2, 1, 1, 0.5, 2, 1, 1, 1, 0.5, 0.5], # fire
[1, 0.5, 0.5, 2, 2, 0.5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0.5, 1], # water
[1, 2, 0.5, 0.5, 0.5, 2, 1, 2, 0.5, 2, 1, 2, 1, 1, 1, 1, 1, 1], # grass
[1, 1, 1, 1, 0.5, 1, 1, 1, 2, 0.5, 1, 1, 1, 1, 1, 1, 0.5, 1], # electric
[1, 2, 1, 1, 1, 0.5, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1], # ice
[1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 0.5, 0.5, 1, 1, 0.5, 1, 2], # fighting
[1, 1, 1, 0.5, 1, 1, 0.5, 0.5, 2, 1, 2, 0.5, 1, 1, 1, 1, 1, 0.5], # poison
[1, 1, 2, 2, 0, 2, 1, 0.5, 1, 1, 1, 1, 0.5, 1, 1, 1, 1, 1], # ground
[1, 1, 1, 0.5, 2, 2, 0.5, 1, 0, 1, 1, 0.5, 2, 1, 1, 1, 1, 1], # flying
[1, 1, 1, 1, 1, 1, 0.5, 1, 1, 1, 0.5, 2, 1, 2, 1, 2, 1, 1], # psychic
[1, 2, 1, 0.5, 1, 1, 0.5, 1, 0.5, 2, 1, 1, 2, 1, 1, 1, 1, 1], # bug
[0.5, 0.5, 2, 2, 1, 1, 2, 0.5, 2, 0.5, 1, 1, 1, 1, 1, 1, 2, 1], # rock
[0, 1, 1, 1, 1, 1, 0, 0.5, 1, 1, 1, 0.5, 1, 2, 1, 2, 1, 1], # ghost
[1, 0.5, 0.5, 0.5, 0.5, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2], # dragon
[1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 0, 2, 1, 0.5, 1, 0.5, 1, 2], # dark
[0.5, 2, 1, 0.5, 1, 0.5, 2, 0, 2, 0.5, 0.5, 0.5, 0.5, 1, 0.5, 1, 0.5, 0.5], # steel
[1, 1, 1, 1, 1, 1, 0.5, 2, 1, 1, 1, 0.5, 1, 1, 0, 0.5, 2, 1]] # fairy
chosen_defender1 = 0
chosen_defender2 = 0
chosen_attacker = 0
column=[0 for _ in range(18)]

tile_size = Tk().winfo_screenheight()//38 if Tk().winfo_screenheight()//19< Tk().winfo_screenwidth()//23 else Tk().winfo_screenwidth()//46
screen = window(tile_size)

# loading assets and hit boxes if needed
background = Assets(23*tile_size, 19*tile_size, "assets/background.png")
off_switch = Assets(tile_size, tile_size, "assets/off_switch.png")
off_switch.interaction(tile_size*22, tile_size*18)
chosen = Assets(tile_size, tile_size, "assets/tiles/chosen.png")
efficiency = {0: Assets(tile_size, tile_size, "assets/tiles/inefficient.png"), 0.25: Assets(tile_size, tile_size, "assets/tiles/extremely_inefficient.png"), 0.5: Assets(tile_size, tile_size, "assets/tiles/super_inefficient.png"), 1: Assets(tile_size, tile_size, "assets/tiles/efficient.png"), 2: Assets(tile_size, tile_size, "assets/tiles/super_efficient.png"), 4: Assets(tile_size, tile_size, "assets/tiles/extremely_efficient.png")}
font=pygame.font.Font(None,tile_size)

running = True
clock=pygame.time.Clock()
pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)

while running:
    clock.tick(30)
    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x_tile, mouse_y_tile = event.pos[0]//tile_size, event.pos[1]//tile_size
            if off_switch.rect.collidepoint(event.pos):
                running = False
            elif not mouse_y_tile and 0<mouse_x_tile<19:
                if not chosen_defender1:
                    chosen_defender1 = mouse_x_tile
                elif chosen_defender1 == mouse_x_tile:
                    chosen_defender1 = chosen_defender2
                    chosen_defender2 = 0
                elif not chosen_defender2:
                    chosen_defender2 = mouse_x_tile
                elif chosen_defender2 == mouse_x_tile:
                    chosen_defender2 = 0
                else:
                    chosen_defender2 = 0
                    chosen_defender1 = mouse_x_tile
            elif not mouse_x_tile and mouse_y_tile > 0:
                if chosen_attacker != mouse_y_tile:
                    chosen_attacker = mouse_y_tile
                else:
                    chosen_attacker = 0
            collumn=calculate_efficiency()
    # updating screen
    screen.blit(background.image, (0, 0))
    screen.blit(off_switch.image, (tile_size*22, tile_size*18))
    if chosen_attacker:
        screen.blit(chosen.image, (0, chosen_attacker * tile_size))
    if chosen_defender1:
        screen.blit(chosen.image, (chosen_defender1 * tile_size, 0))
    if chosen_defender2:
        screen.blit(chosen.image, (chosen_defender2 * tile_size, 0))
    if chosen_defender1:
        if chosen_attacker:
            screen.blit(efficiency[column[chosen_attacker-1]].image, (19 * tile_size, tile_size * chosen_attacker))
        else:
            for y in range(18):
                #screen.blit(efficiency[column[y]].image, (19 * tile_size, tile_size * (y + 1)))
                screen.blit(collumn[y],(19 * tile_size, tile_size * (y + 1)))
    pygame.display.flip()
pygame.quit()