# Course-Project-Algorithms
Course Project - Algorithms (Graph Algorithms)

Course: CS 325 - Analysis of Algorithms

Term: Summer 2021

**Course Description:**

Recurrence relations, combinatorics, recursive algorithms, proofs of correctness.

My Grade: A (99.08%)

# Project Name: Puzzle Solved by Graph Algorithm
**Project Description**

You are given a 2-D puzzle of size MxN, that has N rows and M column (N>=3 ; M >= 3; M and N can be different). Each cell in the puzzle is either empty or has a barrier. An empty cell is marked by ‘-’ (hyphen) and the one with a barrier is marked by ‘#’. You are given two coordinates from the puzzle (a,b) and (x,y). You are currently located at (a,b) and want to reach (x,y). You can move only in the following directions.
* L: move to left cell from the current cell
* R: move to right cell from the current cell
* U: move to upper cell from the current cell
* D: move to the lower cell from the current cell

You can move to only an empty cell and cannot move to a cell with a barrier in it. Your goal is to find the minimum number of cells that you have to cover to reach the destination cell (do not count the starting cell and the destination cell). The coordinates (1,1) represent the first cell; (1,2) represents the second cell in the first row. If there is not possible path from source to destination return None.

Sample Input Puzzle Board: [[-,-,-,-,-],[-,-,#,-,-],[-,-,-,-,-],[#,-,#,#,-],[-#,-,-,-]]

Examples:
* Example 1: (a,b) : (1,3) ; (x,y): (3,3) 
  * Output: 3
  * One possible direction to travel: LDDR (1,3) →(1,2) → (2,2) → (3,2)→(3,3)
* Example 2: (a,b): (1,1) ; (x,y): (5,5) 
  * Output: 7
  * One possible direction to travel: DDRRRRDD
(1,1) →(2,1)→(3,1)→(3,2)→(3,3)→(3,4)→(3,5)→(4,5)→(5,5)
* Example 3: (a,b): (1,1); (x,y) : (5,1) 
  * Output: None

**Extra Credit**

For the above puzzle in addition to the output return a set of possible
directions as well in the form of a string.

* Example 1: (a,b) : (1,3) ; (x,y): (3,3) 
  * Output: 3, LDDR
  * One possible direction to travel: LDDR (1,3) →(1,2) → (2,2) → (3,2)→(3,3)

**My Idea**

Get inspiration from Breadth-First Search Applications provided in the Exploration: Graph Introduction and Traversal. I choose to apply the BFS algorithm to find the minimum number of cells (by tracking the level) to cover to reach the destination cell.

In Breadth-First Search, we start at the source and traverse across each level until we reach the destination. I use queue data structures to implement. (Details refer to code)

[Time Complexity]

My implementation is based on the BFS algorithm, which has a time complexity of O(|V|+|E|). (Without the extra credit helper method, only return the number of cells) 

Note: Here |V| means the number of cells without barriers, and |E| means the number of "-" that represents the unit edge.

For extra credit, I use an extra credit helper method to compute a set of possible directions in the form of a string. Besides, instead of only returning the minimum number of cells, I call the extra credit helper method and return a tuple (number of cells, a set of possible directions in the form of a string).
