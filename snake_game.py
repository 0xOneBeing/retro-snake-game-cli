#!/usr/bin/env python3
"""
Retro Snake Game for CLI
A classic snake game with ASCII graphics
"""

import curses
import random
import time
from enum import Enum
from typing import List, Tuple

class Direction(Enum):
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)

class SnakeGame:
    def __init__(self, width: int = 60, height: int = 20):
        self.width = width
        self.height = height
        self.snake = [(height // 2, width // 2)]  # Start in center
        self.direction = Direction.RIGHT
        self.food = self._generate_food()
        self.score = 0
        self.game_over = False
        
    def _generate_food(self) -> Tuple[int, int]:
        """Generate food at random position not occupied by snake"""
        while True:
            food = (random.randint(1, self.height - 2), 
                   random.randint(1, self.width - 2))
            if food not in self.snake:
                return food
    
    def move_snake(self) -> bool:
        """Move snake in current direction. Returns False if game over."""
        head_y, head_x = self.snake[0]
        dy, dx = self.direction.value
        new_head = (head_y + dy, head_x + dx)
        
        # Check wall collision
        if (new_head[0] <= 0 or new_head[0] >= self.height - 1 or
            new_head[1] <= 0 or new_head[1] >= self.width - 1):
            return False
            
        # Check self collision
        if new_head in self.snake:
            return False
            
        self.snake.insert(0, new_head)
        
        # Check if food eaten
        if new_head == self.food:
            self.score += 10
            self.food = self._generate_food()
        else:
            self.snake.pop()  # Remove tail if no food eaten
            
        return True
    
    def change_direction(self, new_direction: Direction):
        """Change snake direction if not opposite to current direction"""
        current_dy, current_dx = self.direction.value
        new_dy, new_dx = new_direction.value
        
        # Prevent reversing into itself
        if (current_dy + new_dy != 0) or (current_dx + new_dx != 0):
            self.direction = new_direction

def draw_game(stdscr, game: SnakeGame):
    """Draw the game state on screen"""
    stdscr.clear()
    
    # Draw border
    for i in range(game.height):
        for j in range(game.width):
            if i == 0 or i == game.height - 1 or j == 0 or j == game.width - 1:
                stdscr.addch(i, j, '█')
    
    # Draw snake
    for i, (y, x) in enumerate(game.snake):
        if i == 0:  # Head
            stdscr.addch(y, x, '●')
        else:  # Body
            stdscr.addch(y, x, '○')
    
    # Draw food
    food_y, food_x = game.food
    stdscr.addch(food_y, food_x, '♦')
    
    # Draw score and instructions
    stdscr.addstr(game.height + 1, 0, f"Score: {game.score}")
    stdscr.addstr(game.height + 2, 0, "Use arrow keys to move, 'q' to quit")
    stdscr.addstr(game.height + 3, 0, "═" * 40)
    
    stdscr.refresh()

def show_game_over(stdscr, score: int):
    """Display game over screen"""
    stdscr.clear()
    
    # ASCII art game over
    game_over_art = [
        "  ██████   █████  ███    ███ ███████     ██████  ██    ██ ███████ ██████  ",
        " ██       ██   ██ ████  ████ ██         ██    ██ ██    ██ ██      ██   ██ ",
        " ██   ███ ███████ ██ ████ ██ █████      ██    ██ ██    ██ █████   ██████  ",
        " ██    ██ ██   ██ ██  ██  ██ ██         ██    ██  ██  ██  ██      ██   ██ ",
        "  ██████  ██   ██ ██      ██ ███████     ██████    ████   ███████ ██   ██ "
    ]
    
    height, width = stdscr.getmaxyx()
    start_y = height // 2 - len(game_over_art) // 2 - 3
    
    for i, line in enumerate(game_over_art):
        x = max(0, (width - len(line)) // 2)
        try:
            stdscr.addstr(start_y + i, x, line)
        except curses.error:
            pass  # Handle terminal too small
    
    # Score and restart info
    score_text = f"Final Score: {score}"
    restart_text = "Press 'r' to restart or 'q' to quit"
    
    stdscr.addstr(start_y + len(game_over_art) + 2, 
                 (width - len(score_text)) // 2, score_text)
    stdscr.addstr(start_y + len(game_over_art) + 4, 
                 (width - len(restart_text)) // 2, restart_text)
    
    stdscr.refresh()

def show_splash_screen(stdscr):
    """Display splash/welcome screen with retro styling and blinking prompt"""
    stdscr.clear()
    
    # Retro-style title with block characters
    retro_title = [
        "██████╗ ███████╗████████╗██████╗  ██████╗ ",
        "██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██╔═══██╗",
        "██████╔╝█████╗     ██║   ██████╔╝██║   ██║",
        "██╔══██╗██╔══╝     ██║   ██╔══██╗██║   ██║",
        "██║  ██║███████╗   ██║   ██║  ██║╚██████╔╝",
        "╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ",
        "",
        "   ███████╗███╗   ██╗ █████╗ ██╗  ██╗███████╗",
        "   ██╔════╝████╗  ██║██╔══██╗██║ ██╔╝██╔════╝",
        "   ███████╗██╔██╗ ██║███████║█████╔╝ █████╗  ",
        "   ╚════██║██║╚██╗██║██╔══██║██╔═██╗ ██╔══╝  ",
        "   ███████║██║ ╚████║██║  ██║██║  ██╗███████╗",
        "   ╚══════╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝"
    ]
    
    height, width = stdscr.getmaxyx()
    start_y = max(2, height // 2 - len(retro_title) // 2 - 8)
    
    # Draw retro title
    for i, line in enumerate(retro_title):
        x = max(0, (width - len(line)) // 2)
        try:
            stdscr.addstr(start_y + i, x, line)
        except curses.error:
            pass
    
    # Game info with retro styling
    game_info = [
        "",
        "▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓",
        "▓                                             ▓",
        "▓  🎮 CLASSIC ARCADE EXPERIENCE 🎮            ▓",
        "▓                                             ▓",
        "▓  CONTROLS:                                  ▓",
        "▓  ↑ ↓ ← → : Navigate your snake              ▓",
        "▓  Q : Quit game                              ▓",
        "▓                                             ▓",
        "▓  OBJECTIVE:                                 ▓",
        "▓  • Eat diamonds (♦) to grow                 ▓",
        "▓  • Avoid walls (█) and yourself             ▓",
        "▓  • Achieve the highest score!               ▓",
        "▓                                             ▓",
        "▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓"
    ]
    
    # Draw game info
    info_start_y = start_y + len(retro_title) + 2
    for i, line in enumerate(game_info):
        x = max(0, (width - len(line)) // 2)
        try:
            stdscr.addstr(info_start_y + i, x, line)
        except curses.error:
            pass
    
    # Blinking prompt setup
    blink_counter = 0
    show_prompt = True
    
    # Static instructions
    static_instructions = [
        "",
        "Press 'Q' to quit"
    ]
    
    prompt_y = info_start_y + len(game_info) + 2
    
    # Draw static instructions
    for i, line in enumerate(static_instructions):
        x = max(0, (width - len(line)) // 2)
        try:
            stdscr.addstr(prompt_y + 2 + i, x, line)
        except curses.error:
            pass
    
    stdscr.refresh()
    
    # Main loop with blinking prompt
    while True:
        # Handle blinking effect (soft blink every ~30 frames)
        blink_counter += 1
        if blink_counter >= 30:
            show_prompt = not show_prompt
            blink_counter = 0
        
        # Draw or clear the blinking prompt
        prompt_text = ">>> Press 'S' to START! <<<"
        x = max(0, (width - len(prompt_text)) // 2)
        
        try:
            if show_prompt:
                # Show prompt with retro styling
                stdscr.addstr(prompt_y, x, "▓" * len(prompt_text))
                stdscr.addstr(prompt_y + 1, x, prompt_text)
            else:
                # Clear prompt area
                stdscr.addstr(prompt_y, x, " " * len(prompt_text))
                stdscr.addstr(prompt_y + 1, x, " " * len(prompt_text))
        except curses.error:
            pass
        
        stdscr.refresh()
        
        # Check for key input
        key = stdscr.getch()
        if key == ord('s') or key == ord('S'):
            return True  # Start game
        elif key == ord('q') or key == ord('Q'):
            return False  # Quit game
        
        time.sleep(0.05)  # Control blink speed and reduce CPU usage

def main(stdscr):
    """Main game loop"""
    # Setup curses
    curses.curs_set(0)  # Hide cursor
    stdscr.nodelay(1)   # Non-blocking input
    stdscr.timeout(100) # Refresh rate
    
    # Show splash screen - exit if user chooses to quit
    if not show_splash_screen(stdscr):
        return
    
    while True:
        # Initialize game
        game = SnakeGame()
        
        # Game loop
        while not game.game_over:
            draw_game(stdscr, game)
            
            # Handle input
            key = stdscr.getch()
            if key == ord('q'):
                return
            elif key == curses.KEY_UP:
                game.change_direction(Direction.UP)
            elif key == curses.KEY_DOWN:
                game.change_direction(Direction.DOWN)
            elif key == curses.KEY_LEFT:
                game.change_direction(Direction.LEFT)
            elif key == curses.KEY_RIGHT:
                game.change_direction(Direction.RIGHT)
            
            # Move snake
            if not game.move_snake():
                game.game_over = True
            
            time.sleep(0.1)  # Control game speed
        
        # Game over screen
        show_game_over(stdscr, game.score)
        
        # Wait for restart or quit
        while True:
            key = stdscr.getch()
            if key == ord('q'):
                return
            elif key == ord('r'):
                break  # Restart game

if __name__ == "__main__":
    try:
        curses.wrapper(main)
    except KeyboardInterrupt:
        print("\nThanks for playing!")
    except Exception as e:
        print(f"Error: {e}")
        print("Make sure your terminal supports the required features.")
