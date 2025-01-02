# Tic-Tac-Toe MiniMax Algorithm

This repository contains an implementation of the Tic-Tac-Toe game using the MiniMax algorithm and its optimization through Alpha-Beta Pruning. The game allows players to choose between human vs. computer or computer vs. computer modes. The computer opponent uses either the standard MiniMax algorithm or the optimized MiniMax with Alpha-Beta Pruning to decide its moves.

## Features:
- **MiniMax Algorithm**: A decision-making algorithm to select the best possible move for the computer.
- **Alpha-Beta Pruning**: An optimization technique for the MiniMax algorithm that reduces the number of nodes evaluated in the search tree.
- **Two Modes**: 
  - Human vs. Computer
  - Computer vs. Computer

## How to Run:
To run the game, use the command line interface. The script takes three arguments:
1. **Algorithm**: Choose between '1' for MiniMax or '2' for Alpha-Beta Pruning.
2. **First Player**: Choose between 'X' or 'O' for which player goes first.
3. **Mode**: Choose between:
   - '1' for human vs. computer
   - '2' for computer vs. computer

### Example Usage:
To run the game with MiniMax, where 'X' goes first and it's a human vs. computer game:
```bash
python Pranav_Kuchibhotla_CS480_P01_A20511026.py 1 X 1
```

  Copyright (c) 2025 Pranav Kuchibhotla
