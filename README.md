
# Coursework 1 for CSC325 course at Swansea University (2021):

This coursework involves building an AI agent that can play the Gomoku Game. This Agent will compete against other agents that were produced by students in a tournament. The coursework deadline is 5/3/2021.

## Progress So Far:
* Initial Commit for the helper files produced by lecturer
* Wrote down the basic functions for minmax algorithm in Player/player.py
* Agent now is able to play on a 3x3 board (tic-tac-toe)
* There is a bug with the algorithm since the agent loses to the random agent in some occasions (working on a fix)
-----------
* minmax algorithm apparently is now working fine, however it seems that the winning test in the utility function takes a lot of time for over 3 stones, but works just fine for two stones. The two stones game is very trivial but the AI seems to win every time it starts first and wins when the random agent doesn't score a win accidentally every time which is a good indicator that minmax is working just fine
* Therefore I will have to look into alpha beta pruning and test the result. It will be harder to determine if an error is coming about from the minmax algorithm or the alpha beta pruning however.
------------
* Pruning is now working
* minimax was working just fine, I spent years debugging a stupid bug with Alpha Beta pruning
* Working on evaluation function and depth cut off now to play on bigger board
------------

## Work that needs to be done:
* Fixing the minmax algoritm (DONE)
* Writing algorithm for pruing (DONE)
* Evaluation and Depth Cut Off

## Notes:
* The coursework will be submitted as soon as the agent is able to play games on the full 11x11 board
* Further optimization will be done and submitted afterwards

