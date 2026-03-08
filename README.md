<!-- README.md is generated from README.Rmd. Please edit that file -->

# Amazing Race Maze Solver

## By: Saul Varshavsky

<!-- badges: start -->
<!-- badges: end -->


### Project Description

This project aims to create a solution for the user when navigating a maze.


### Project Setup

- **Running the project:**
    - python maze_solver.py

- **Testing Code:**
    - The folder "mazes" contains 10 txt files with different maze configurations
        - In main(), provide the name of the txt file to be tested
    - Refer to the "test_maze_solver.py" file for the exact test cases for each of those 10 maze configurations

- **Running the tests:**
    - python -m unittest test_maze_solver.py

- **Setting Up GitHub Repository:**
    - git init
    - git remote add origin https://github.com/username/repositoryName.git
        - e.g. git remote add origin https://github.com/svarsha4/Amazing_Race_Maze_Solver.git
    - git add .
    - git commit -m "message"
        - e.g. git commit -m "Started implementing maze solver"
    - git push -u origin master

- **Pushing Updates:**
    - Click on the Source Control icon in VS Code
    - Write commit message and then click on the blue Commit button
        - To commit only certain updated files, stage the files to commit
        - A file gets staged when the + icon is clicked to the right of the file in the Source Control panel
    - Click on the blue Sync Changes button
    

### Important Considerations

- **Queue & Breadth First Search:**
    - The BFS algorithm is used in this function to find the shortest path through the maze. BFS is implemented here by exploring all the possible paths than can be taken by level.
    - First, all the possible paths that are 1 step away from the starting position are explored. Next, all the possible paths that are 2 steps away from the starting position get explored. This process continues until the last row of the maze is reached.
    - Therefore, a queue is particularly useful for implementing BFS, because it ensures that FIRST the paths one step away are FIRST removed from the queue and analyzed (i.e. "first in first out principle"). Next, the paths that are two steps away get removed and  analyzed. In essence, this process continues until the final step is reached.
