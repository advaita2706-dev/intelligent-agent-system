"""Base Agent Module

This module defines the base class for all intelligent agents in the system.
It provides core functionality for perception, action, and decision-making.
"""

from abc import ABC, abstractmethod
from typing import Any, List, Dict


class BaseAgent(ABC):
    """Abstract base class for intelligent agents.
    
    This class provides the fundamental structure for creating intelligent
    agents that can perceive their environment and take actions.
    
    Attributes:
        name (str): The name/identifier of the agent
        environment (Any): The environment in which the agent operates
        performance (float): Performance measure of the agent
    """
    
    def __init__(self, name: str, environment: Any = None):
        """Initialize the base agent.
        
        Args:
            name: Unique identifier for the agent
            environment: The environment object the agent interacts with
        """
        self.name = name
        self.environment = environment
        self.performance = 0.0
        self.history = []
    
    @abstractmethod
    def perceive(self) -> Dict[str, Any]:
        """Perceive the current state of the environment.
        
        Returns:
            Dictionary containing perceived information about the environment
        """
        pass
    
    @abstractmethod
    def decide(self, percepts: Dict[str, Any]) -> Any:
        """Make a decision based on percepts.
        
        Args:
            percepts: Information perceived from the environment
            
        Returns:
            The action to be taken
        """
        pass
    
    @abstractmethod
    def act(self, action: Any) -> None:
        """Execute the chosen action in the environment.
        
        Args:
            action: The action to be executed
        """
        pass
    
    def run(self) -> None:
        """Main execution loop for the agent.
        
        This method orchestrates the perceive-decide-act cycle.
        """
        percepts = self.perceive()
        action = self.decide(percepts)
        self.act(action)
        self.update_performance()
    
    def update_performance(self) -> None:
        """Update the performance measure of the agent."""
        # Implement performance tracking logic
        pass
    
    def get_performance(self) -> float:
        """Get the current performance measure.
        
        Returns:
            Current performance value
        """
        return self.performance
    
    def reset(self) -> None:
        """Reset the agent to its initial state."""
        self.performance = 0.0
        self.history = []
    
    def __str__(self) -> str:
        return f"Agent({self.name}, Performance: {self.performance:.2f})"
    
    def __repr__(self) -> str:
        return self.__str__()
