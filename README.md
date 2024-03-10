# PyGame Conway's game of life

![Conway's Game of Life](https://upload.wikimedia.org/wikipedia/commons/e/e5/Gospers_glider_gun.gif)

## Introduction

This is a simple implementation of Conway's Game of Life using Pygame.
Conway's Game of Life is a cellular automaton devised by the mathematician John Conway.
The game is a zero-player game, meaning that its evolution is determined by its initial state,
with no further input from humans.

## Getting Started

### Prerequisites

Make sure you have Python and Pygame installed on your system.

- [Python](https://www.python.org/)
- [Pygame](https://www.pygame.org/) `python3 -m pip install pygame-ce`

### Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/your-username/pygame-conways-game-of-life.git
```

Navigate to the project and then run `python3 ./game_of_life.py`

## Rules

- Any live cell with fewer than two live neighbors dies (underpopulation).
- Any live cell with two or three live neighbors lives on to the next generation.
- Any live cell with more than three live neighbors dies (overpopulation).
- Any dead cell with exactly three live neighbors becomes a live cell (reproduction).

## Contributing

Feel free to contribute to the development of this project. You can fork the repository, make your changes, and submit a pull request.
