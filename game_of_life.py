import numpy as np
import pygame


def create_grid(grid_size, cell_size):
    return np.random.choice([0, 1], size=grid_size, p=[0.8, 0.2])


def create_cell_surface(cell_size, alive):
    color = (0, 128, 0) if alive else (0, 0, 0)
    surface = pygame.Surface((cell_size, cell_size))
    surface.fill(color)
    return surface


def draw_grid(screen, grid, cell_size):
    for x in range(grid.shape[0]):
        for y in range(grid.shape[1]):
            cell_surface = create_cell_surface(cell_size, grid[x, y] == 1)
            screen.blit(cell_surface, (x * cell_size, y * cell_size))


def update_grid(grid, grid_size):
    center_grid = grid[1:-1, 1:-1]

    neighbors = (
        grid[:-2, :-2]
        + grid[:-2, 1:-1]
        + grid[:-2, 2:]
        + grid[1:-1, :-2]
        + grid[1:-1, 2:]
        + grid[2:, :-2]
        + grid[2:, 1:-1]
        + grid[2:, 2:]
    )

    alive_cells = center_grid == 1
    dead_cells = ~alive_cells

    min_neighbours = 1
    max_neighbours = 4

    # apply Conway's Game of Life rules
    underpopulated_or_overpopulated = (neighbors < min_neighbours) | (
        neighbors > max_neighbours
    )
    reproduction = (dead_cells) & (neighbors == max_neighbours)

    center_grid[alive_cells & underpopulated_or_overpopulated] = 0
    center_grid[dead_cells & reproduction] = 1


def main():
    pygame.init()
    screen_w, screen_h = 1280, 900
    cell_size = 5
    grid_size = (screen_w // cell_size, screen_h // cell_size)
    screen = pygame.display.set_mode((screen_w, screen_h))
    pygame.display.set_caption("Conway's Game of Life")
    clock = pygame.time.Clock()

    grid = create_grid(grid_size, cell_size)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                    running = False
                    break

        screen.fill((0, 0, 0))
        draw_grid(screen, grid, cell_size)
        update_grid(grid, grid_size)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
