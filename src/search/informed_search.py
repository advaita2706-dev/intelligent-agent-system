"""Informed Search Algorithms Module

Implements A* and Greedy Best-First Search algorithms.
"""

import heapq
from typing import List, Tuple, Callable, Optional


class Node:
    """Represents a node in the search space."""
    
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.depth = 0 if parent is None else parent.depth + 1
    
    def __lt__(self, other):
        return self.path_cost < other.path_cost


class AStarSearch:
    """A* Search Algorithm implementation."""
    
    def __init__(self, heuristic: Callable):
        self.heuristic = heuristic
        self.nodes_expanded = 0
    
    def search(self, initial_state, goal_test: Callable, get_successors: Callable) -> Optional[List]:
        """Perform A* search.
        
        Args:
            initial_state: Starting state
            goal_test: Function to test if state is goal
            get_successors: Function returning list of (action, state, cost) tuples
            
        Returns:
            List of actions to reach goal, or None if no solution
        """
        frontier = []
        initial_node = Node(initial_state)
        heapq.heappush(frontier, (self.heuristic(initial_state), initial_node))
        
        explored = set()
        
        while frontier:
            _, node = heapq.heappop(frontier)
            
            if goal_test(node.state):
                return self._reconstruct_path(node)
            
            explored.add(str(node.state))
            self.nodes_expanded += 1
            
            for action, successor_state, step_cost in get_successors(node.state):
                if str(successor_state) not in explored:
                    child = Node(
                        successor_state,
                        parent=node,
                        action=action,
                        path_cost=node.path_cost + step_cost
                    )
                    f_value = child.path_cost + self.heuristic(successor_state)
                    heapq.heappush(frontier, (f_value, child))
        
        return None
    
    def _reconstruct_path(self, node: Node) -> List:
        """Reconstruct path from goal node to start."""
        path = []
        while node.parent is not None:
            path.append(node.action)
            node = node.parent
        return list(reversed(path))


class GreedyBestFirstSearch:
    """Greedy Best-First Search implementation."""
    
    def __init__(self, heuristic: Callable):
        self.heuristic = heuristic
        self.nodes_expanded = 0
    
    def search(self, initial_state, goal_test: Callable, get_successors: Callable) -> Optional[List]:
        """Perform Greedy Best-First search."""
        frontier = []
        initial_node = Node(initial_state)
        heapq.heappush(frontier, (self.heuristic(initial_state), initial_node))
        
        explored = set()
        
        while frontier:
            _, node = heapq.heappop(frontier)
            
            if goal_test(node.state):
                return self._reconstruct_path(node)
            
            explored.add(str(node.state))
            self.nodes_expanded += 1
            
            for action, successor_state, _ in get_successors(node.state):
                if str(successor_state) not in explored:
                    child = Node(successor_state, parent=node, action=action)
                    h_value = self.heuristic(successor_state)
                    heapq.heappush(frontier, (h_value, child))
        
        return None
    
    def _reconstruct_path(self, node: Node) -> List:
        path = []
        while node.parent is not None:
            path.append(node.action)
            node = node.parent
        return list(reversed(path))
