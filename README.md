
# Coursework 1 for CSC325 course at Swansea University (2021):

This coursework involves building an AI agent that can play the Gomoku Game. This Agent will compete against other agents that were produced by students in a tournament. The coursework deadline is 5/3/2021.

Minimum coursework ready for sumbission. Due to time constraint and health issues, the solution is very minimalistic and can be improved. Ways to improve the algorithm are discussed later.

The Algorithm starts off with a list of moves that are close to a move that has been made by either players on the board
It then proceeds through the minimax algorithm, with a depth cutoff of 2 which is very bad given how little time I had to construct a solution
The evaluation funtion discourages when the opponent has 3 stones in a row and encourages when the agent has 3 stones in a row
This results in semeingly a very defensive behavior by the AI

With more time we could try improving the algorithm by doing the following:
* Developnig a better evaluation function
* Developing a transposition lookup table
* Looking into initial node selection in a better way
* Optimizing the low level computations that don't impact decision making

## Future Work:
* Developnig a better evaluation function
* Developing a transposition lookup table
* Looking into initial node selection in a better way
* Optimizing the low level computations that don't impact decision making 


## Extending The project:
In this section I will discuss long term improvements for the project where it can become a fully standalone project instead of being just a simple AI agent.
* Building a single page website that allows people to challenge the AI
* Improving the AI as mentioned above
* Building other AI agents that use other strategies
* Building other AI agents that use neural networks to learn to play the game
