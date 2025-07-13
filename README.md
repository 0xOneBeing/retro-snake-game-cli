# 🐍 Retro Snake Game

A classic snake game built for the command line with retro ASCII graphics!

## Features

- **Splash/Welcome Screen**: Stylish ASCII art introduction with game title and instructions
- **Retro ASCII Graphics**: Beautiful terminal-based visuals with classic snake characters
- **Smooth Gameplay**: Responsive controls with adjustable game speed
- **Score Tracking**: Keep track of your high scores
- **Game Over Detection**: Collision detection with walls and self
- **Restart Functionality**: Play multiple rounds without restarting the program

## Requirements

- Python 3.6+
- Terminal with cursor key support
- Unix-like system (macOS, Linux) or Windows with proper terminal

## How to Play

### Installation & Running

```bash
# Make the game executable
chmod +x snake_game.py

# Run the game
python3 snake_game.py
```

### Controls

- **Arrow Keys**: Move the snake (↑ ↓ ← →)
- **Q**: Quit the game
- **R**: Restart after game over
- **Any Key**: Continue from splash screen to start the game

### Splash Screen

When you first run the game, you'll be greeted with a stylish welcome screen featuring:
- ASCII art game title
- Brief game instructions
- Visual preview of game elements
- "Press any key to continue" prompt

This screen sets the retro mood and prepares you for the classic snake gaming experience!

### Gameplay

1. Control the snake using arrow keys
2. Eat diamonds (♦) to grow and increase your score
3. Avoid hitting walls (█) or the snake's own body
4. Try to achieve the highest score possible!

## Game Elements

- `●` - Snake head
- `○` - Snake body
- `♦` - Food (diamonds)
- `█` - Walls/borders

## Tips

- Plan your moves ahead to avoid trapping yourself
- The snake grows longer with each food item eaten
- The game speed is optimized for smooth gameplay
- Try to create patterns to maximize your score

## Technical Details

- Built with Python's `curses` library for terminal graphics
- Object-oriented design with clean separation of concerns
- Collision detection and game state management
- Cross-platform terminal compatibility

## Troubleshooting

If you encounter issues:

1. **Terminal too small**: Resize your terminal window
2. **Key input not working**: Ensure your terminal supports cursor keys
3. **Display issues**: Try different terminal applications

Enjoy the game! 🎮
