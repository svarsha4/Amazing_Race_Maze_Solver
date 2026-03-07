import unittest

from maze_solver import (
    load_maze_from_file,
    start_position,
    coordinates_to_path_steps,
    solve_maze
)


class TestMazeSolver(unittest.TestCase):
    def run_maze_test(self, filename):
        visited = set()
        path = []

        maze = load_maze_from_file(filename)
        start_row, start_col = start_position(maze)
        solution = solve_maze(maze, start_row, start_col, visited, path)
        steps = coordinates_to_path_steps(solution)

        # Verifies that a solution is ACTUALLY found for the maze
        self.assertIsNotNone(solution)

        # Verifies that the row of the last coordinate in the maze solution is ACTUALLY
        # in the last row of the maze (i.e. the exit coordinate)
        end_row = len(maze) - 1
        self.assertEqual(solution[-1][0], end_row)

        # Verifies that every coordinate in the maze solution is ACTUALLY comprises a valid path 
        # (i.e. has a value of 1 in the maze)
        for row, col in solution:
            self.assertEqual(maze[row][col], 1)
        
        # Verifies that the number of coordinates ACTUALLY matches the
        # number of path steps in the maze solution
        self.assertEqual(len(steps), len(solution))
    
    # Test cases for each of the 10 txt files
    def test_maze1(self):
        self.run_maze_test("mazes/maze1.txt")
    def test_maze2(self):
        self.run_maze_test("mazes/maze2.txt")
    def test_maze3(self):
        self.run_maze_test("mazes/maze3.txt")
    def test_maze4(self):
        self.run_maze_test("mazes/maze4.txt")
    def test_maze5(self):
        self.run_maze_test("mazes/maze5.txt")
    def test_maze6(self):
        self.run_maze_test("mazes/maze6.txt")
    def test_maze7(self):
        self.run_maze_test("mazes/maze7.txt")
    def test_maze8(self):
        self.run_maze_test("mazes/maze8.txt")
    def test_maze9(self):
        self.run_maze_test("mazes/maze9.txt")
    def test_maze10(self):
        self.run_maze_test("mazes/maze10.txt")
