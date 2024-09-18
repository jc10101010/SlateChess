#SlateChess - A Python-based Chess Bot with Minimax, Alpha-Beta Pruning, Move Ordering, and Quiescence Search

**SlateChess** is a chess engine written in Python, leveraging advanced algorithms to efficiently evaluate positions and play competitive chess. Built with the core principles of **minimax**, enhanced with **alpha-beta pruning**, **move ordering**, and **quiescence search**, this bot is designed to optimize its performance in chess matches. The implementation is modular and can be easily extended or improved.

##Features

- **Minimax Algorithm**: SlateChess uses the minimax algorithm as the core decision-making process, evaluating positions to choose the best move by simulating both players' actions.
  
- **Alpha-Beta Pruning**: Optimizes the search process by eliminating branches of the game tree that do not need to be explored, reducing computation time and improving efficiency.

- **Move Ordering**: Moves are sorted based on their potential impact, prioritizing captures and more valuable moves, allowing alpha-beta pruning to be more effective.

- **Quiescence Search**: Extends the search beyond the depth limit in tactical positions to avoid the "horizon effect," ensuring better evaluation during complex positions, especially when captures are involved.

- **Customizable Search Depth**: The depth of the search can be adjusted, allowing users to trade off between speed and playing strength.

- **Static Evaluation**: Provides a fast and heuristic-based evaluation of board positions, considering material and positional advantages.

##How to Play

To play SlateChess, run the following command:

```bash
python ChessGame.py
```

The **ChessGame** script is the entry point for playing the game, allowing you to interact with the bot. You can either play as White or Black against SlateChess, or pit the engine against itself.

##Structure

The project is composed of the following core components:

- **ChessGame.py**: This is the main entry point where the game is played. It manages the game flow and player interactions, as well as the integration with the chess engine.
  
- **Negamax.py**: Contains the negamax algorithm implementation, the key decision-making logic used by SlateChess. This includes alpha-beta pruning and the move evaluation process.

- **ChessBoard.py**: Manages all board-related functionality, including move generation, piece movement, and static evaluation functions. This module is also responsible for enforcing the rules of chess and providing utilities for converting between board coordinates and chess notation.

- **Alpha-Beta Pruning**: An optimized version of the negamax algorithm, implementing alpha-beta pruning to improve search efficiency.

- **Quiescence Search**: Enhances the engine’s tactical awareness by extending the search in positions involving captures to avoid shallow evaluations in dynamic positions.

- **Move Ordering**: Improves the effectiveness of alpha-beta pruning by sorting moves before they are evaluated, prioritizing captures and checks.

##Key Algorithms and Optimizations

###1. **Negamax with Alpha-Beta Pruning**
The primary search algorithm, negamax, is optimized using alpha-beta pruning. This allows SlateChess to explore fewer positions by cutting off branches that don't need further investigation.

###2. **Move Ordering**
Before evaluating moves, SlateChess orders them to ensure the most promising moves (like captures, checks, or promotions) are evaluated first. This greatly enhances the effectiveness of alpha-beta pruning.

###3. **Quiescence Search**
This technique prevents the engine from making poor evaluations in highly dynamic positions by extending the search when captures or checks are involved, reducing the horizon effect.

###4. **Static Evaluation Function**
The engine evaluates a position using a combination of material balance and positional heuristics. It assigns a numerical value to positions to help guide the search toward the best moves.

##Configuration and Customization

SlateChess is designed to be easily customizable:

- **Adjust Search Depth**: Modify the `maxDepth` parameter to control how deeply the engine searches in the game tree. Increasing depth will improve playing strength at the cost of speed.

- **Evaluation Tweaks**: You can modify the evaluation function in `ChessBoard.py` to include additional heuristics, such as king safety or pawn structure, to make the engine more sophisticated.

- **Engine Tuning**: The quiescence search depth, move ordering criteria, and alpha-beta pruning settings can all be fine-tuned for performance improvements.
