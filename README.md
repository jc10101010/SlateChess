# SlateChess - Advanced Python Chess Engine with Minimax, Alpha-Beta Pruning, Move Ordering, and Quiescence Search

**SlateChess** is a sophisticated chess engine written in Python, designed to play chess competitively using a combination of advanced algorithms such as **minimax**, **alpha-beta pruning**, **move ordering**, and **quiescence search**. With modular components and high customizability, SlateChess can be a strong chess opponent or a versatile tool for improving your game.

## Key Features

- **Minimax (Negamax) Algorithm**: At the core of SlateChess is the minimax algorithm (implemented as negamax), which evaluates possible positions for both sides to determine the best move based on future consequences.
  
- **Alpha-Beta Pruning**: Reduces the number of positions evaluated in the game tree by skipping over branches that won't affect the final decision, greatly improving the engine's efficiency.

- **Move Ordering**: To further enhance alpha-beta pruning, SlateChess orders moves based on their potential impact, with captures, checks, and threats prioritized. This results in faster and deeper searches.

- **Quiescence Search**: Extends the search process in tactical situations involving captures or checks, ensuring that the engine doesn't miss critical variations due to shallow evaluations. This technique minimizes the horizon effect by searching until the position stabilizes.

- **Customizable Search Depth**: Control the depth of the search tree, adjusting the strength and speed of the engine to match your requirements. Higher search depths produce stronger play but require more computation time.

- **Static Evaluation Function**: The evaluation function considers material, positional factors, and other heuristics, assigning each position a score. This helps guide the engine towards favorable positions while avoiding poor ones.

- **Tactical Awareness**: The engine is highly tactical, able to calculate deep combinations and respond accurately to threats, captures, and checkmate sequences.

## How to Play

To play against SlateChess, run the following command:

```bash
python ChessGame.py
```

You'll be prompted to choose your side (White or Black), and the game will proceed with moves being input in standard chess notation (e.g., `e2e4` for moving a pawn from e2 to e4).

SlateChess can also play against itself by modifying the game setup in the `ChessGame.py` script.

## Project Structure

The project is organized into the following components:

- **ChessGame.py**: Manages the gameplay interface, handling input, turn logic, and game flow. This script serves as the user’s entry point into SlateChess.

- **ChessBoard.py**: Contains the board representation, move generation, piece movement logic, and static evaluation functions. It enforces the rules of chess and provides utilities for board state visualization and notation conversion.

- **Negamax.py**: Implements the basic negamax algorithm, a specialized version of minimax, which evaluates the game tree. It serves as the foundation for the more advanced versions.

- **NegamaxAlphaBeta.py**: Extends the basic negamax implementation by introducing alpha-beta pruning, which significantly improves efficiency by pruning unnecessary branches in the game tree.

- **NegamaxAlphaBetaMoveOrder.py**: Enhances the previous implementation with move ordering, allowing the engine to prioritize high-impact moves such as captures and checks, further improving alpha-beta pruning.

- **NegamaxAlphaBetaMoveOrderQuiescenceSearch.py**: The most advanced version of the engine, incorporating quiescence search to handle tactical positions. This reduces the horizon effect, ensuring that captures and checks are not prematurely cut off by the depth limit.

## Algorithms and Optimizations

### 1. **Negamax with Alpha-Beta Pruning**

Negamax is a simplified version of minimax that assumes symmetry between players, making it more efficient. Alpha-beta pruning is used to eliminate branches of the game tree that are not worth exploring. The combination allows SlateChess to calculate deeper within a reasonable amount of time.

### 2. **Move Ordering**

Before evaluating positions, SlateChess orders moves to ensure the most promising ones (captures, checks, and promotions) are examined first. By focusing on these moves, the engine can trigger alpha-beta cutoffs earlier, speeding up the search process.

### 3. **Quiescence Search**

Quiescence search addresses the problem of evaluating positions with tactical complexities (like a sequence of captures). In these positions, SlateChess continues to search beyond the standard depth until the position reaches a stable state, where no immediate captures or checks are possible.

### 4. **Static Evaluation Function**

The static evaluation function scores a given board position based on various heuristics:

- **Material Balance**: Counts the relative value of pieces on both sides.
- **Positional Factors**: Includes considerations like piece mobility, king safety, and pawn structure.
- **Tactical Motifs**: Factors in tactical threats such as attacks on major pieces, checkmate threats, and exposed kings.

This evaluation helps guide the engine's decision-making during the search.

## Customization and Tuning

SlateChess is built to be flexible, allowing for easy modifications to improve performance or adjust playing style:

- **Search Depth**: You can change the search depth by modifying the `maxDepth` parameter in the engine's configuration. Higher depth will improve the engine's strength but increase computation time.
  
- **Evaluation Function**: The static evaluation function in `ChessBoard.py` can be expanded to include more complex heuristics (e.g., improved king safety, pawn structure evaluation, or piece activity).

- **Quiescence Search and Pruning**: The depth of the quiescence search and the thresholds for alpha-beta pruning can be adjusted in the `NegamaxAlphaBetaMoveOrderQuiescenceSearch.py` script, offering fine-tuning options for experienced developers.
