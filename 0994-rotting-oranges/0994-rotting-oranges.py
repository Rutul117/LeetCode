class Queue:
    def __init__(self):
        self.queue = []
        self.front = 0

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.isEmpty():
            return None
        item = self.queue[self.front]
        self.front += 1
        return item

    def isEmpty(self):
        return self.front >= len(self.queue)

    def size(self):
        return len(self.queue) - self.front


class Solution:
    def orangesRotting(self, grid):

        # Get the number of rows in the grid
        rows = len(grid)

        # Get the number of columns in the grid
        cols = len(grid[0])

        # Create a queue to perform BFS
        q = Queue()

        # Count the total number of fresh oranges
        fresh = 0

        # Traverse every cell in the grid
        for r in range(rows):
            for c in range(cols):

                # If the current orange is rotten, add its position to the queue
                if grid[r][c] == 2:
                    q.enqueue((r, c))

                # If the current orange is fresh, increase the fresh count
                elif grid[r][c] == 1:
                    fresh += 1

        # If there are no fresh oranges initially, no time is required
        if fresh == 0:
            return 0

        # Variable to store the total minutes elapsed
        minutes = 0

        # Four possible directions: Up, Down, Left, Right
        directions = [
            (-1, 0),   # Up
            (1, 0),    # Down
            (0, -1),   # Left
            (0, 1)     # Right
        ]

        # Continue BFS until there are no more rotten oranges to process
        while not q.isEmpty():

            # Number of rotten oranges present at the current minute
            level_size = q.size()

            # Tracks whether at least one fresh orange becomes rotten this minute
            infected = False

            # Process all rotten oranges of the current minute
            for _ in range(level_size):

                # Remove one rotten orange from the queue
                row, col = q.dequeue()

                # Check all four adjacent cells
                for dr, dc in directions:

                    # Compute the coordinates of the neighboring cell
                    nr = row + dr
                    nc = col + dc

                    # Check whether the neighbor is inside the grid
                    # and contains a fresh orange
                    if (
                        nr >= 0 and nr < rows and
                        nc >= 0 and nc < cols and
                        grid[nr][nc] == 1
                    ):

                        # Convert the fresh orange into a rotten orange
                        grid[nr][nc] = 2

                        # One less fresh orange remains
                        fresh -= 1

                        # At least one orange was infected this minute
                        infected = True

                        # Add the newly rotten orange to the queue
                        # It will infect others in the next minute
                        q.enqueue((nr, nc))

            # Increase the minute only if some orange became rotten
            if infected:
                minutes += 1

        # If every fresh orange became rotten, return the total time
        if fresh == 0:
            return minutes

        # Otherwise, some fresh oranges could never be reached
        return -1