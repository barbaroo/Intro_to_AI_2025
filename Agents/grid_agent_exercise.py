"""
Grid World Agent Simulation
A simple agent that navigates a grid with obstacles to reach a goal.
"""

import matplotlib.pyplot as plt
import numpy as np
import random
import time

# Environment setup
grid_size = (5, 5)
goal_pos = (4, 4)
obstacles = [(2, 2), (3, 2)]

class GridWorld:
    def __init__(self, size, goal, obstacles):
        self.size = size
        self.goal = goal
        self.obstacles = set(obstacles)

    def is_valid(self, pos):
        x, y = pos
        return (0 <= x < self.size[0] and
                0 <= y < self.size[1] and
                pos not in self.obstacles)

    def is_goal(self, pos):
        return pos == self.goal

class Agent:
    def __init__(self, env):
        self.env = env
        self.pos = (0, 0)
        self.belief_state = set()
        self.path = [self.pos]

    def get_possible_moves(self):
        x, y = self.pos
        directions = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
        return [move for move in directions if self.env.is_valid(move)]

    def move(self):
        self.belief_state.add(self.pos)
        options = self.get_possible_moves()
        options = [opt for opt in options if opt not in self.belief_state]

        if not options:
            options = self.get_possible_moves()  # backtrack if stuck

        self.pos = random.choice(options)
        self.path.append(self.pos)

    def run_until_goal(self):
        while not self.env.is_goal(self.pos):
            self.move()
            self.visualize()
        print("Goal reached in", len(self.path)-1, "steps!")

    def visualize(self):
        grid = np.zeros(self.env.size)
        for obs in self.env.obstacles:
            grid[obs] = -1
        grid[self.env.goal] = 2
        grid[self.pos] = 1

        plt.clf()
        plt.imshow(grid, cmap='coolwarm', vmin=-1, vmax=2)
        for (i, j), val in np.ndenumerate(grid):
            if val == 1:
                plt.text(j, i, '🤖', ha='center', va='center', fontsize=14)
            elif val == 2:
                plt.text(j, i, '🏁', ha='center', va='center', fontsize=14)
            elif val == -1:
                plt.text(j, i, '🧱', ha='center', va='center', fontsize=14)

        plt.title("Agent Navigation")
        plt.xticks([])
        plt.yticks([])
        plt.pause(0.5)

if __name__ == "__main__":
    env = GridWorld(grid_size, goal_pos, obstacles)
    agent = Agent(env)
    plt.ion()
    agent.run_until_goal()
    plt.ioff()
    plt.show()
