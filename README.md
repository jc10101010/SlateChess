# **SlateChess**  
**Python Chess Engine with Minimax, Alpha-Beta Pruning, Move Ordering, and Quiescence Search**

SlateChess is a well optimized chess engine built with advanced algorithms like **minimax**, **alpha-beta pruning**, **move ordering**, and **quiescence search**.

## **Features**

- **Negamax Algorithm**: The core engine uses the negamax variant of minimax to efficiently evaluate positions for both sides.
- **Alpha-Beta Pruning**: Reduces unnecessary evaluations in the game tree, improving search efficiency.
- **Move Ordering**: Prioritizes high-impact moves (captures, checks) to enhance alpha-beta pruning and speed up decision-making.
- **Quiescence Search**: Handles tactical sequences, preventing shallow evaluations in complex positions by searching until the situation stabilizes.

## **How to Play**

1. **Run SlateChess**:
   ```bash
   python ChessGame.py
   ```

## **Project Structure**

- **`ChessGame.py`**: The main script to start the game. Handles user input, game flow, and turn management.
- **`ChessBoard.py`**: Manages the board representation, move generation, and rule enforcement. Includes utilities for visualizing the board and converting chess notation.
- **`Negamax.py`**: Basic negamax algorithm implementation.
- **`NegamaxAlphaBeta.py`**: Enhances `Negamax.py` by introducing alpha-beta pruning for greater search efficiency.
- **`NegamaxAlphaBetaMoveOrder.py`**: Adds move ordering to improve alpha-beta pruning by evaluating captures, checks, and threats first.
- **`NegamaxAlphaBetaMoveOrderQuiescenceSearch.py`**: The most advanced engine, adding quiescence search to handle tactical situations and minimize the horizon effect.

## **Algorithms and Optimizations**

1. **Negamax with Alpha-Beta Pruning**  
   Negamax simplifies minimax by exploiting symmetry between players. Alpha-beta pruning reduces unnecessary evaluations, allowing deeper searches.

2. **Move Ordering**  
   High-impact moves (captures, checks, promotions) are evaluated first, triggering more efficient alpha-beta cutoffs and improving search speed.

3. **Quiescence Search**  
   Extends the search in positions with tactical complexity, ensuring accurate evaluations in situations involving captures or checks, preventing premature cutoffs.

4. **Static Evaluation Function**  
   Positions are scored based on:
   - **Material**: Piece values and balance.
   - **Positional Factors**: Piece activity, mobility, and king safety.
