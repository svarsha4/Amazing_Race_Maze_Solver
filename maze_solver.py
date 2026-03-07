from collections import deque


def load_maze_from_file(filename):
    """
    This function does the following:
     1) Reads the maze provided in the txt file
     2) Converts that maze into a 2D list

    Parameters:
        filename (str): The txt file containing the maze

    Returns:
        list[list[int]]: The 2D list representation of the maze
    """
    maze = []

    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            row = [int(char) for char in line]
            maze.append(row)

    return maze


def start_position(maze):
    """
    This function finds the starting position in the maze, which is
    represented by the 1 in the first row of the maze.

    Parameters:
        maze (list[list[int]]): The 2D list representation of the maze

    Returns:
        tuple: The coordinates (row, col) of the maze's starting position
    """
    for col in range(len(maze[0])):
        # If the value at the current column of the first row in the maze is a 1, 
        # then return the coordinates of that position (i.e. it's the starting point)
        if maze[0][col] == 1:
            return (0, col)


def coordinates_to_path_steps(coordinates):
    """
    This function converts a list of coordinates (row, col) 
    from the maze into a path step (step, col+1)

    Parameters:
        coordinates (list[tuple]): A list of (row, col) coordinates

    Returns:
        list[tuple]: The path traveled in the maze.
    """
    path = []

    # Convert each coordinate (row, col) in the maze solution to a path step (step, col+1)
    for step, (row, col) in enumerate(coordinates, start=1):
        path.append((step, col + 1))

    return path


def print_detailed_path(coordinates):
    """
    This function converts a list of coordinates (row, col) 
    from the maze into the movement directions to take for each step (step, direction)

    Parameters:
        coordinates (list[tuple]): A list of (row, col)
    
    Returns: 
        void
    """
    steps = coordinates_to_path_steps(coordinates)

    print("Start")
    
    for i in range(1, len(coordinates)):
        # Compares the previous coordinates in the path to the current coordinates,
        # in order to determine which direction the user moved in the maze
        # (i.e. how the user got from the previous position to their current position)
        prev_row, prev_col = coordinates[i-1]
        row, col = coordinates[i]

        if row == prev_row + 1:
            direction = "Move Down"
        elif row == prev_row - 1:
            direction = "Move Up"
        elif col == prev_col + 1:
            direction = "Move Right"
        elif col == prev_col - 1:
            direction = "Move Left"
        
        print(f"Step {i}: {direction}")
    
    print("End")


def solve_maze(maze, start_row, start_col, visited, path):
    """
    This function uses a Breadth First Search algorithm
    to find the shortest solution path through the maze.

    Parameters:
        maze (list[list[int]]): The 2D list representation of the maze
        start_row (int): The row of the starting coordinate (row, col) of the maze
        start_col (int): The column of the starting coordinate (row, col) of the maze
        visited (set): A set used to keep track of which coordinates were already VISITED in the maze
        path (list[tuple]): A list to store the coordinates (row, col) in the path taken through the maze

    Returns:
        list[tuple]: The solution through the maze,
        which is a list of all the coordinates (row, col) in the path taken through the maze
    """
    rows = len(maze)
    cols = len(maze[0])

    # Initializes the queue, which contains the coordinates (row, col)
    # of the current position in the maze, as well as the path taken to get to that position
    queue = deque([ ( (start_row, start_col), [(start_row, start_col)] ) ])
    
    visited.add((start_row, start_col))

    # Defines the directions when moving through the maze:
    # right (0,1) (i.e. iterate to the next col)
    # left (0,-1) (i.e. go back to the previous col)
    # down (1,0) (i.e. iterate to the next row)
    # Up (-1,0) (i.e. go back to the previous row)
    path_directions = [(0,1), (0,-1), (1,0), (-1,0)]

    while queue:
        # Retrieve the current coordinates and path that was currently taken from the queue
        # (i.e. "first in, first out" order)
        (row, col), current_path = queue.popleft()

        if row == rows-1:
            return current_path
        
        for vertical_step, horizontal_step in path_directions:
            new_row = row + vertical_step
            new_col = col + horizontal_step

            # Ensures that the new coordinates are within the bounds of the maze
            if ((0 <= new_row < rows) and (0 <= new_col < cols)):
                # If the new coordinates of the maze is represented by a "1", then that
                # means the user can move to that new position.
                # Furthermore, the new coordinates CANNOT be coordinates the user
                # has VISITED previously in the maze.
                if (maze[new_row][new_col] == 1 and (new_row, new_col) not in visited):
                    visited.add((new_row, new_col))
                    new_path = current_path + [(new_row, new_col)]
                    queue.append(( (new_row, new_col), new_path ))
    return None


def main():
    # Calls the function to convert the maze from the txt file into a 2D list
    # ----- ADJUST THE FILE NAME TO CORRESPOND WITH THE EXAMPLE YOU'RE TESTING -----
    maze = load_maze_from_file("mazes/maze1.txt")

    # Calls the function to find the starting position in the maze
    start_row, start_col = start_position(maze)

    visited = set()
    path = []

    # Calls the function to provide the solution to the maze
    solution = solve_maze(maze, start_row, start_col, visited, path)
    # Calls the function to convert the coordinates in the path to the steps needed to take
    # the path through the maze
    solution_steps = coordinates_to_path_steps(solution)

    for step_num, col in solution_steps:
        print(f"({step_num}, {col})")
    print_detailed_path(solution)


if __name__ == "__main__":
    main()